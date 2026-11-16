import asyncio

from datetime import datetime

from app.models import PromptLog
from app.logger import save_log
from app.gemini_client import ask_gemini
from app.metrics import average_latency


PROMPTS = [
    "What is AI?",
    "What is RAG?",
    "What are embeddings?",
    "Explain transformers",
    "Explain FastAPI"
]


async def main():

    tasks = [
        ask_gemini(prompt)
        for prompt in PROMPTS
    ]

    results = await asyncio.gather(
        *tasks
    )

    for result in results:

        log = PromptLog(
            timestamp=datetime.now(),
            prompt=result["prompt"],
            response=result["response"],
            latency=result["latency"]
        )

        save_log(log)

    print(
        "Average Latency:",
        average_latency()
    )


if __name__ == "__main__":

    asyncio.run(main())