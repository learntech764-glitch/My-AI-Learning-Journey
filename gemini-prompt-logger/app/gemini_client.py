import asyncio
import time

import google.generativeai as genai

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


async def ask_gemini(prompt):

    start = time.perf_counter()

    response = await asyncio.to_thread(
        model.generate_content,
        prompt
    )

    latency = round(
        time.perf_counter() - start,
        2
    )

    return {
        "prompt": prompt,
        "response": response.text,
        "latency": latency
    }