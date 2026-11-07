from groq_client import ask_groq


def generate_lesson(topic, previous_feedback=None, retry_feedback=None):
    previous_feedback = previous_feedback or []
    retry_feedback = retry_feedback or []

    prompt = f"""
Write a standalone beginner lesson about: {topic}

AUDIENCE:
A learner in India who has completed school, is new to AI, and prefers simple English.
Assume the learner has never heard of this topic.

Include:
1. A simple title
2. What RAG is, in plain language
3. Why RAG is useful and what problem it solves
4. How it works step by step
5. One everyday example with a small story
6. One simple AI-related example
7. Key technical terms explained in simple words
8. What RAG does NOT do / a common misunderstanding
9. A short recap
10. Three simple questions with answers

ACCURACY RULES:
- Explain that retrieval finds useful external information and generation uses it to form an answer.
- Explain this flow: documents -> chunks -> embeddings -> search -> retrieved context -> language model -> answer.
- Explain that RAG does not automatically retrain or update model weights during retrieval.
- Do not assume the learner knows Python, databases, vectors, or machine learning.
- Use short sentences and familiar examples.
- Explain technical words before or when you use them.
- Do not invent facts or sources.

FEEDBACK FROM EARLIER RUNS:
{chr(10).join(previous_feedback[-5:]) if previous_feedback else "No saved feedback yet."}

FIX THESE FAILURES FROM THE LAST ATTEMPT:
{chr(10).join(retry_feedback) if retry_feedback else "No retry feedback. This is the first attempt."}

Return only the lesson in Markdown. Do not include scores.
"""
    return ask_groq([
        {"role": "system", "content": "You are a careful instructional designer teaching AI to absolute beginners."},
        {"role": "user", "content": prompt}
    ], temperature=0.4)
