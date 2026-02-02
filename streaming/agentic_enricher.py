import json
from datetime import datetime
import random
import sys


def enrich_event(event):
    """
    Apply agentic decision logic to a base event.
    Decisions are additive and do not modify the original payload.
    """
    amount = event.get("payload", {}).get("attributes", {}).get("amount", 0)

    if amount > 300:
        decision = "flag_high_risk"
        priority = "high"
        risk_score = round(random.uniform(0.7, 0.9), 2)
        decision_reason = "high_transaction_amount"
    else:
        decision = "allow"
        priority = "low"
        risk_score = round(random.uniform(0.1, 0.3), 2)
        decision_reason = "normal_transaction"

    enriched_event = {
        "event_id": event["event_id"],
        "event_type": event["event_type"],
        "source_system": event["source_system"],
        "event_timestamp": event["event_timestamp"],

        "agent_metadata": {
            "decision": decision,
            "decision_reason": decision_reason,
            "risk_score": risk_score,
            "priority": priority,
            "confidence": round(random.uniform(0.8, 0.95), 2),
            "agent_version": "v1.0"
        },

        "payload": event["payload"],

        "processing_metadata": {
            "ingestion_time": datetime.utcnow().isoformat() + "Z",
            "processing_time": datetime.utcnow().isoformat() + "Z",
            "pipeline_version": "local-dev"
        }
    }

    return enriched_event


def main():
    """
    Read base events from stdin and emit agent-enriched events to stdout.
    This allows easy composition with upstream producers.
    """
    for line in sys.stdin:
        event = json.loads(line.strip())
        enriched = enrich_event(event)
        print(json.dumps(enriched))


if __name__ == "__main__":
    main()

