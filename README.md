# crm-icm

A client CRM for a South African tax practice, run entirely through Claude. This repo holds the **structure only**:
rules, skills and templates. It holds **no client data** and names no practice or person. Every record lives in the
practice's own Google Drive, synced to each staff Mac by Google Drive for desktop and opened by Claude Cowork as a
local folder. No Google connectors are used.

One repo serves every practice. What differs per practice (its name, staff, practitioners, offices, clients) is a
value on that practice's Drive or in its Project instruction, never in here.

## What's in here

| Folder | Who reads it | Holds |
|---|---|---|
| `workspace/` | Each staff member's Claude | The rules. Markdown only. The one repo folder linked to a Cowork project, read only. Starts at `workspace/CLAUDE.md` |
| `setup/` | The system provider | How to set up a practice: questionnaire, onboarding, the Project instruction, loading clients from the old CRM |
| `tools/` | The system provider | `release.py` (ship a version), `scan.py` (personal-data check), and the tests every release runs |

## Setting up a new practice

1. Answer [setup/questionnaire.md](setup/questionnaire.md) with the practice.
2. Follow [setup/onboarding.md](setup/onboarding.md): their Drive folder, one Cowork project per staff member, the
   Project instruction from [setup/project-instructions.md](setup/project-instructions.md), first-run checks.
3. Load their existing clients once: [setup/population-guide.md](setup/population-guide.md).

## Changing the live system

Structure changes are made here and shipped with `python3 tools/release.py --note "what changed"` (scan, tests,
version bump, tag, push). Each practice is told, and each staff member presses **Sync** on their Cowork project.
Staff can change their records by chat; any change to the structure is answered with Error 500 and the system
provider's contact line.
