import google.generativeai as genai
import time

from app.config import (
    GEMINI_API_KEY,
    MODEL_NAME
)

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    MODEL_NAME
)

def ask_gemini(prompt: str):

    try:

        start = time.perf_counter()

        response = model.generate_content(
            prompt
        )

        duration = round(
            time.perf_counter() - start,
            2
        )

        return {
            "response": response.text,
            "duration": duration
        }

    except Exception as ex:

        print(
            f"Gemini Error: {ex}"
        )

        return {
            "response": "ERROR",
            "duration": 0
        }