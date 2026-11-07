import argparse
import json
from datetime import datetime, timezone

from config import TOPIC
from generator import generate_lesson
from evaluator import evaluate_lesson
from memory import load_memory, save_run

MAX_RETRIES = 2


def main():
    parser = argparse.ArgumentParser(description="Self-evaluating beginner lesson generator")
    parser.add_argument("--topic", default=TOPIC, help="Topic to teach")
    parser.add_argument("--demo-failure", action="store_true",
                        help="Inject a known incorrect sentence on attempt one")
    args = parser.parse_args()

    try:
        memory = load_memory()
        previous_feedback = memory.get("useful_feedback", [])

        if not isinstance(previous_feedback, list):
            previous_feedback = []

    except Exception as e:
        print(f"Warning: Could not load memory: {e}")
        previous_feedback = []
    previous_feedback = memory.get("useful_feedback", [])
    retry_feedback = []
    rejection_log = []
    final_lesson = None
    final_evaluation = None
    print(f"Loaded {len(previous_feedback)} saved feedback items.")

    for feedback in previous_feedback:
        print("Previous feedback:", feedback)

    print(f"\nTopic: {args.topic}")
    for attempt in range(MAX_RETRIES + 1):
        print(f"\n--- Attempt {attempt + 1} of {MAX_RETRIES + 1} ---")
        lesson = generate_lesson(args.topic, previous_feedback, retry_feedback)

        if args.demo_failure and attempt == 0:
            lesson += "\n\n## Deliberate test statement\nRAG updates the model's weights during retrieval.\n"

        evaluation = evaluate_lesson(args.topic, lesson)
        print("Evaluation:", "PASS" if evaluation["overall_pass"] else "FAIL")

        if evaluation["overall_pass"]:
            final_lesson, final_evaluation = lesson, evaluation
            break

        failed = [c for c in evaluation["checks"] if not c["passed"]]
        rejection_log.append({
            "attempt": attempt + 1,
            "failed_checks": failed,
            "summary": evaluation.get("summary", "")
        })
        retry_feedback = [c["reason"] for c in failed]
        final_lesson, final_evaluation = lesson, evaluation

    if final_evaluation["overall_pass"]:
        with open("outputs/final_lesson.md", "w", encoding="utf-8") as f:
            f.write(f"# {args.topic}\n\n{final_lesson}")

    result = {
        "topic": args.topic,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "passed": final_evaluation["overall_pass"],
        "attempts_used": len(rejection_log) + (1 if final_evaluation["overall_pass"] else 0),
        "final_evaluation": final_evaluation,
        "rejection_log": rejection_log
    }
    with open("outputs/rejection_log.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    save_run(args.topic, result["passed"], rejection_log)
    print("\nSaved rejection log: outputs/rejection_log.json")
    if result["passed"]:
        print("Approved lesson: outputs/final_lesson.md")
    else:
        print("No lesson passed within the retry limit. Review the rejection log.")


if __name__ == "__main__":
    main()

