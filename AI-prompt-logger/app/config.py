import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.1-flash-lite")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY missing")