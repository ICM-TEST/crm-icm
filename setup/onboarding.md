# Onboarding a practice: system provider only

Have [questionnaire.md](questionnaire.md) answered first. Every answer goes onto the practice's Drive, never into this repo.

1. On each staff member's Mac, install Google Drive for desktop and sign in with their own Google account.
2. In the practice's Google Drive, create a top-level folder named exactly `CLAUDE WORKSPACE FILES` with `CONTEXT.md`, `lists/`, `clients/`, `outputs/` and `outputs/reports/`. Each folder gets its `CONTEXT.md` from the drive-context templates in `workspace/templates/drive-context/`, as `workspace/shared/drive-layout.md` says.
3. Fill `lists/names.md` from `workspace/templates/names.md`, using the questionnaire answers (`Staff 1` to `Staff 4`, `Practitioner 1` to `2`, `Office 1` to `2`). The practice administrator then owns that file and is the only one who edits it.
4. Share `CLAUDE WORKSPACE FILES` with each staff member, with edit access. Wait until it shows as synced on their Mac.
5. For each staff member, in Claude Cowork on their Mac:
   1. Create a Cowork project.
   2. Link two folders to the **project** (not a single chat), so every new chat has them: this repo's `workspace/` (read only) and `CLAUDE WORKSPACE FILES` (read and write). Allow access when Cowork asks, and choose to always allow it for this project if offered.
   3. Start a new chat and ask "What folders can you see?". Both must be listed by name.
   4. Paste their instruction from [project-instructions.md](project-instructions.md) into **Instructions**, with the three placeholders filled.
6. First-run checks, for each staff member:
   1. Ask "Who do you work for?". The answer is their own name.
   2. Add a test client, then ask to see their client card. Confirm it renders as a visual in the chat, not as text or a file.
   3. Pull a small report, for example all clients in one office. Confirm it renders in the chat.
   4. Make one change and read the client's log. Confirm the line is stamped with the Google account taken from the Drive path, or that it says "account not available".
   5. Remove the test client's files by hand on the Drive afterwards (Claude never deletes).
7. Load the existing clients from the old CRM, once, before staff start: [population-guide.md](population-guide.md).
8. Updates: the system provider makes a release with `python3 tools/release.py --note "what changed"` and tells the practice. Each staff member then presses **Sync** on their Cowork project. If folders in `workspace/` moved, they re-attach only `workspace/`.
