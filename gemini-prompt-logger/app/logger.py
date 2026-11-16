from pathlib import Path

Path("logs").mkdir(
    exist_ok=True
)

LOG_FILE = "logs/prompts.jsonl"


def save_log(log_entry):

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            log_entry.model_dump_json()
        )

        file.write("\n")