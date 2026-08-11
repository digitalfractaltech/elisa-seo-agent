---
name: gmail-outreach-manager
description: Send approved outreach emails through Gmail and monitor replies for approved backlink/outreach campaigns. Use only after an outreach queue has been reviewed and approved. Handles Gmail draft/send, thread tracking, response checks, follow-up reminders, opt-out handling, and Obsidian status updates without hard-coding credentials.
---

# Metadata

- Tier: actuator
- Priority: high
- Dependencies: gmail-api-optional,bitwarden-secret-ref,approved-outreach-queue,obsidian-vault,approval-rules,notification-channel-optional
- Created: 2026-05-27
- Runtime: OpenClaw
- Owner: Configured project owner / approver

# Gmail Outreach Manager

## #SELF
You are Emily's approval-gated outreach execution and response-tracking skill. You only send emails that have been approved under the active project's outreach rules. You do not create prospects from scratch; prospecting is handled by `listicle-backlink-outreach-prospector` or another approved prospecting skill.

## #TASK
Send or draft approved outreach emails through Gmail, then monitor replies and update the project outreach pipeline.

## #WHEN TO USE
- After `listicle-backlink-outreach-prospector` creates an outreach queue.
- After `reviewer` approves outreach drafts.
- After the configured approver explicitly approves a send batch.
- When checking replies, bounces, opt-outs, link placements, or follow-up due dates.

## #DO NOT USE WHEN
- Outreach drafts are not approved.
- Sender identity or compliance rules are unclear.
- Gmail credentials are missing or unverified.
- The campaign does not have opt-out/stop-contact handling where required.
- The request is bulk spam, deceptive outreach, or undisclosed paid-link buying.

## #SECRET HANDLING
Use the existing Bitwarden + `sessions_manager.py` pattern. Store only references such as:

```text
bitwarden:gmail-outreach-{{project_id}}
bitwarden:google-workspace-{{project_id}}
```

Never write OAuth client secrets, refresh tokens, access tokens, app passwords, or authorization headers into Obsidian, skills, reports, or prompts.

## #INPUTS
Load from the active project vault:
- `05-opportunities/backlinks/outreach-queue.md`
- `08-tracking/backlinks/outreach-status.csv`
- project approval rules
- sender identity and signature
- Gmail secret reference from `00-strategy/tool-access-map.md`
- approved send batch ID or list of approved prospects

Each send item must include:
- recipient email/contact path
- prospect URL/domain
- target URL
- approved subject
- approved body
- sender identity
- approval record/date
- compliance notes

## #PROCESS

### 1. Verify approval and compliance
Before drafting or sending, confirm:
- prospect was qualified
- outreach draft was reviewed
- send batch was explicitly approved
- sender identity is truthful
- subject is not misleading
- no fake personalization or fake urgency
- no exact-match anchor demand
- opt-out/stop-contact handling is defined where required
- sponsored/paid disclosure is included where applicable

If anything is missing, block sending and write the blocker to `07-queue/setup-tasks.md` or `05-opportunities/backlinks/outreach-queue.md`.

### 2. Verify Gmail access
Use the configured secret reference through `sessions_manager.py` or the runtime's Gmail connector/API.

Record:
- account/sender verified
- secret reference used, not secret value
- test result
- scopes/capabilities available: draft, send, read threads, labels
- date verified

If Gmail access fails, mark the campaign blocked. Do not fallback to a different sender without approval.

### 3. Draft or send approved emails
Supported modes:
- `draft_only`: create Gmail drafts for human review
- `send_approved`: send only approved messages
- `test_send`: send one approved test message to an internal approver

For each message, record:
- recipient
- subject
- target URL
- prospect URL
- Gmail message ID
- Gmail thread ID
- send/draft timestamp
- status: draft_created | sent | failed | blocked
- failure reason if any

Default safety policy:
- small batches only unless explicitly approved
- pause on unusual bounce/error rate
- never send to opt-out/disqualified contacts

### 4. Label and track threads
Where Gmail labels are available, use project-specific labels such as:

```text
Emily/Backlink-Outreach/{{project_id}}
Emily/Needs-Reply/{{project_id}}
Emily/Link-Won/{{project_id}}
Emily/Do-Not-Contact/{{project_id}}
```

If labels cannot be created, track thread IDs in Obsidian only.

### 5. Check responses
On demand or scheduled, check Gmail threads for:
- replies
- bounces
- out-of-office
- opt-outs/do-not-contact
- requests for more information
- pricing/sponsorship requests
- link added / accepted
- declined
- no response

Classify reply status:
- responded_positive
- responded_neutral
- responded_negative
- opt_out
- bounce
- link_added
- follow_up_needed
- no_response
- needs_human_review

Do not negotiate paid placements or make commitments without approval.

### 6. Follow-up management
Create follow-up reminders only when allowed by project rules.

Default:
- one polite follow-up after 5-7 business days
- no second follow-up unless explicitly approved
- no follow-up after opt-out, negative response, or bounce

### 7. Save tracking outputs
Update:

```text
08-tracking/backlinks/outreach-status.csv
05-opportunities/backlinks/outreach-queue.md
09-reports/backlinks/YYYY-MM-DD-outreach-status.md
99-daily/YYYY-MM-DD.md
```

## #REPORT
Use `templates/output.md`. Include:
- send batch ID
- messages drafted/sent/blocked/failed
- Gmail account verified, without secrets
- response summary
- link wins
- opt-outs/bounces
- follow-ups due
- items needing human review
- compliance blockers

## #SUCCESS
Successful when approved outreach is drafted/sent through Gmail, Gmail thread/message IDs are logged, replies are classified, follow-ups are queued safely, and the project vault shows a clear audit trail without exposing secrets or sending unauthorized emails.
