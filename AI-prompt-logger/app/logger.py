import json
from pathlib import Path

LOG_FILE = "logs/prompts.jsonl"

Path("logs").mkdir(exist_ok=True)

def save_log(log_data):

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_data.model_dump_json())
        file.write("\n")