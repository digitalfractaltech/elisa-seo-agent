# Gmail API Notes

Use the active runtime's Gmail connector/API if available. Otherwise implement through the official Gmail API using credentials retrieved via `sessions_manager.py` from Bitwarden.

Typical capabilities needed:
- create drafts
- send messages
- read sent messages/threads
- read replies
- create/apply labels where available

Do not hard-code OAuth credentials or tokens. Store only Bitwarden secret references in the project vault.

Prefer `draft_only` mode for initial campaigns. Use `send_approved` only after explicit approval.
