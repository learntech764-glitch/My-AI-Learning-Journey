from datetime import datetime

from app.gemini_client import ask_gemini
from app.models import PromptLog
from app.logger import save_log

PROMPTS = [

    "Explain embeddings",

    "What is RAG?",

    "Explain vector databases",

    "Difference between GPT and Gemini",

    "How attention works?"
]

def execute():

    for prompt in PROMPTS:

        result = ask_gemini(prompt)

        log_entry = PromptLog(
            timestamp=datetime.now(),
            prompt=prompt,
            response=result["response"],
            response_time_seconds=result["duration"]
        )

        save_log(log_entry)

        print("\n")
        print("=" * 60)
        print(prompt)
        print("=" * 60)
        print(result["response"])

if __name__ == "__main__":
    execute()