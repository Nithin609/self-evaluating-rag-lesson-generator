import json
from pathlib import Path

MEMORY_FILE = Path("memory/feedback.json")


def load_memory():
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not MEMORY_FILE.exists():
        return {"runs": [], "useful_feedback": []}
    try:
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"runs": [], "useful_feedback": []}


def save_run(topic, passed, rejection_log):
    memory = load_memory()
    reasons = []
    for attempt in rejection_log:
        reasons.extend(check["reason"] for check in attempt.get("failed_checks", []))

    memory["runs"].append({
        "topic": topic,
        "passed": passed,
        "rejection_log": rejection_log
    })
    for reason in reasons:
        if reason not in memory["useful_feedback"]:
            memory["useful_feedback"].append(reason)

    memory["useful_feedback"] = memory["useful_feedback"][-10:]
    MEMORY_FILE.write_text(json.dumps(memory, indent=2), encoding="utf-8")
