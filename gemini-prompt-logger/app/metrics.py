import json


def average_latency():

    total = 0

    count = 0

    try:

        with open(
            "logs/prompts.jsonl",
            encoding="utf-8"
        ) as file:

            for line in file:

                data = json.loads(
                    line
                )

                total += data["latency"]

                count += 1

        return round(
            total / count,
            2
        )

    except FileNotFoundError:

        return 0