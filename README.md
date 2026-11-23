# crm-icm

A CRM run entirely through Claude. This repo holds the structure only: rules, skills and templates in `workspace/`,
which is the one folder attached to a Claude Project. It holds no client data; every record lives in the client's own
Google Drive, reached through the Google connectors.

## Changing the live system

Structure changes are made here and shipped with `python3 tools/release.py --note "what changed"`. Each user then
presses Sync on their Claude Project at a computer.
