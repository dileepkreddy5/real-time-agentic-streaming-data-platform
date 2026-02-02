import json
import uuid
from datetime import datetime
import random
import time


def generate_event():
    """
    Generate a single base event that conforms to the base_event contract.
    """
    return {
        "event_id": str(uuid.uuid4()),
        "event_type": random.choice(["transaction", "login", "page_view"]),
        "source_system": "local_simulator",
        "event_timestamp": datetime.utcnow().isoformat() + "Z",
        "payload": {
            "attributes": {
                "amount": round(random.uniform(10.0, 500.0), 2),
                "currency": "USD",
                "user_id": random.randint(1000, 9999)
            }
        }
    }


def main():
    """
    Emit a fixed number of events for testing.
    """
    for _ in range(10):
        event = generate_event()
        print(json.dumps(event), flush=True)
        time.sleep(0.5)


if __name__ == "__main__":
    main()

