# Self-Evaluating RAG Lesson Generator

A Python project for the GenAI Engineer - Content Systems assessment.

It generates a beginner lesson, evaluates it against six pass/fail checks, retries up to two times, and saves the lesson, rejection log, and feedback memory.

## Requirements
- Python 3.10+
- Groq API key
- VS Code

## Setup on macOS
1. Open this folder in VS Code.
2. Select Terminal -> New Terminal.
3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Copy `.env.example` and rename the copy to `.env`.
6. Put your real Groq key in `.env`:

   ```env
   GROQ_API_KEY=your_real_key_here
   GROQ_MODEL=openai/gpt-oss-120b
   ```

7. Run the project:

   ```bash
   python main.py
   ```

Change the topic:

   ```bash
   python main.py --topic "Introduction to vector databases"
   ```

## Demonstrate a rejected lesson
Run:

   ```bash
   python main.py --demo-failure
   ```

This adds a known false statement to the first lesson. A deterministic check rejects it, and the retry receives the rejection reason.

## Output files
- `outputs/final_lesson.md`: created only when all six checks pass.
- `outputs/rejection_log.json`: attempt history and final evaluation.
- `memory/feedback.json`: feedback retained between runs.

## Six pass/fail checks
1. Accuracy
2. Beginner-friendly language
3. Example quality
4. Jargon explained
5. Key points covered
6. Teaching flow

All six must pass. The system performs one initial generation and at most two retries.

## Architecture decision
The generator and evaluator are separate Python components. The evaluator returns structured JSON, allowing the program to make a clear pass/fail decision. A deterministic guard makes the deliberate-error demonstration repeatable. The memory file stores recent failure reasons and includes them in future generation prompts.

This first version uses a simple Python orchestration loop. LangGraph can be added later while keeping the same generator and evaluator responsibilities.
