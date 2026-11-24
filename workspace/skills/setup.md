# First-run setup

Once per practice: turns the empty Data folder into the CRM.

## Inputs
- Read: [../shared/drive-layout.md](../shared/drive-layout.md) ("CONTEXT files"), [../templates/names.md](../templates/names.md).

## When
- No `CONTEXT.md` at the top of the Data folder, and nothing else in it: run this.
- No `CONTEXT.md` but other files: change nothing; say the CRM folder isn't empty and to contact the system provider.
- A `CONTEXT.md` exists: setup is done. Asked to redo it: Error 500.

## Steps
1. Say you'll set up the CRM, and that everyone else waits until it has synced to their Mac.
2. Ask, one group at a time: staff (up to 4, full names, put in alphabetical order), practitioners (up to 2), offices (up to 2). Unused slots stay blank. More than that is adding a slot: Error 500.
3. Read back the names table exactly as it will be written. Wait for a clear yes.
4. Create the top `CONTEXT.md`, then `lists/` with `names.md`, `clients/`, `outputs/` and `outputs/reports/`, each folder with its `CONTEXT.md`. Nothing else.

## Output
One line: the CRM is set up and they can add their first client.

## Human check
Step 3. This is the only time Claude writes `names.md`.
