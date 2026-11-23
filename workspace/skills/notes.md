# Notes

Add, correct or remove a note on a page entry. Not for the profile's own Notes section (that is a profile field: [update-profile.md](update-profile.md)).

## Inputs
- Read: [../shared/work-pages.md](../shared/work-pages.md), [../shared/drive-layout.md](../shared/drive-layout.md), [../templates/page-entry.md](../templates/page-entry.md), [../templates/drive-context/year.md](../templates/drive-context/year.md).
- Data: the client's `<Page>/<year or period>/` entry.

## Steps
1. Find the client, the page and the year or period. Open the entry. If it doesn't exist, say there are no notes yet and that this note will start the entry.
2. Add: take the note text as plain text, exactly as the person gave it. Build the snapshot: every status currently ticked in this entry (Status box and KPI box), stored as [work-pages.md](../shared/work-pages.md) says, or "none".
3. Read back the note with its date, time, user name and snapshot. Wait for a clear yes.
4. First, if the client's folder holds a conflict copy, stop: [../shared/drive-layout.md](../shared/drive-layout.md) ("Conflict copies"). If the year or period folder or entry doesn't exist (first use): create the folder with its `CONTEXT.md` from the year template, then the entry from the entry template.
5. Write the note at the end of the Notes section (newest last), headed `### <yyyy-mm-dd> <hh:mm> — <user>`, user name only, no Google account.
6. Correct: show the note and the new text, ask for a yes, replace the text. Keep its original date, time and snapshot; the user stamp stays, and add `(edited <yyyy-mm-dd hh:mm> by <user>)`.
7. Remove: show the note, ask for a clear yes, then remove it.

## Output
One plain line: note added, corrected or removed.

## Human check
Step 3 (and the yes in 6 and 7): the staff member confirms before the entry is written.
