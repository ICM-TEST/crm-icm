# Onboarding a practice: system provider only

Have [questionnaire.md](questionnaire.md) answered first. Every answer goes onto the practice's Drive, never into this repo.

Claude builds the CRM on the first run. Nobody creates files by hand: each person connects the repo and the folder, and starts working.

1. On each staff member's Mac, install Google Drive for desktop and sign in with their own Google account.
2. In the practice's Google Drive, create **one empty folder** named exactly `CLAUDE WORKSPACE FILES`. Put nothing in it. Share it with each staff member, with edit access, and wait until it shows as synced on their Mac.
3. For each staff member, in Claude Cowork on their Mac:
   1. Create a Cowork project.
   2. Connect this repo to the **project** (not a single chat) and tick only `workspace/`. Link the folder `CLAUDE WORKSPACE FILES` (read and write). Allow access when Cowork asks, and choose to always allow it for this project if offered.
   3. Paste their instruction from [project-instructions.md](project-instructions.md) into **Instructions**, with the three placeholders filled.
   4. Start a new chat and ask "What folders can you see?". Both `workspace` and `CLAUDE WORKSPACE FILES` must be listed by name.
4. First run, **one person only** (the practice administrator): open a new chat. Claude sees the empty folder, asks for the staff, practitioner and office names (questionnaire answers 2, 5 and 6), reads them back, and on a yes builds the folders and `lists/names.md` ([../workspace/skills/setup.md](../workspace/skills/setup.md)). Everyone else waits until Google Drive shows the folder as up to date on their Mac.
5. First-run checks, for each staff member:
   1. Ask "Who do you work for?". The answer is their own name.
   2. Add a test client, then ask to see their client card. Confirm it renders as a visual in the chat, not as text or a file.
   3. Pull a small report, for example all clients in one office. Confirm it renders in the chat.
   4. Make one change and read the client's log. Confirm the line is stamped with their name.
   5. Remove the test client's files by hand on the Drive afterwards (Claude never deletes).
6. Off-topic and system-change checks (push checklist B5): an off-topic question and a request to change a rule both get the Error 500 line, the second with the system provider's contact line.
7. Load the existing clients from the old CRM, once, before staff start: [population-guide.md](population-guide.md).
8. Updates: the system provider makes a release with `python3 tools/release.py --note "what changed"` and tells the practice. Each staff member then presses **Sync** on their Cowork project. If folders in `workspace/` moved, they re-tick only `workspace/`.
