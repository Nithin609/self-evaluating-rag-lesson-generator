import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
TOPIC = "Introduction to RAG"

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is missing. Create a .env file using .env.example.")
