import json
import os
import sys
from datetime import datetime


OUTPUT_DIR = "data/enriched"


def persist_event(event):
    """
    Persist an enriched event to local storage using
    append-only, time-partitioned files.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    date_partition = datetime.utcnow().strftime("%Y-%m-%d")
    output_file = os.path.join(
        OUTPUT_DIR,
        f"events_{date_partition}.jsonl"
    )

    with open(output_file, "a") as f:
        f.write(json.dumps(event) + "\n")


def main():
    """
    Read enriched events from stdin and persist them locally.
    """
    for line in sys.stdin:
        event = json.loads(line.strip())
        persist_event(event)


if __name__ == "__main__":
    main()

