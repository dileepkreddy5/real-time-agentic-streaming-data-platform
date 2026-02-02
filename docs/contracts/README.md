# Event and Agent Decision Contracts

This directory defines the data contracts used by the Real-Time Agentic Streaming Data Platform.

The goal of these contracts is to establish a clear and stable interface between event producers, streaming processing, and downstream consumers.

---

## Base Event Contract

The base event contract represents the minimal interface between event producers and the platform.

Design principles:
- Capture raw facts only
- Avoid embedded business logic
- Keep the schema stable and extensible

This allows producers to evolve independently without breaking downstream systems.

---

## Agent-Enriched Event Contract

The agent-enriched contract extends the base event with autonomous decision metadata generated during streaming processing.

Key characteristics:
- Decisions are additive, not destructive
- Raw event payload remains unchanged
- Decision metadata is explicit, auditable, and versioned

This enables downstream analytics and GenAI systems to reason not only over events, but over the decisions applied to those events.

---

## Why This Matters

Treating decisions as first-class data enables:
- Transparent and explainable decision pipelines
- Safer evolution of decision logic
- Stronger governance and auditability

This contract-first approach is critical for scalable, AI-ready data platforms.

