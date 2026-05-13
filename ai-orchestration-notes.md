# AI Orchestration Notes (n8n + Azure OpenAI)

## Goal
Automate support-ticket triage with classification, routing, notifications, and analytics.

## High-Level Flow
1. Ingest ticket (email/form/helpdesk webhook)
2. Normalize payload fields
3. Classify intent/category/severity via LLM
4. Apply routing rules to team queues
5. Send notifications (Slack/Email/Teams)
6. Persist events for analytics dashboard

## Minimal Data Contract
- `ticket_id`
- `title`
- `description`
- `customer_tier`
- `predicted_category`
- `predicted_severity`
- `route_target`
- `confidence`
- `created_at`

## Reliability Controls
- Confidence thresholds with fallback to manual review
- Retry policy for transient LLM/API failures
- Idempotency key per ticket event
- Audit log of prompts, responses, and route decisions
