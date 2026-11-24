# Statuses

Tick or untick statuses, or Set As Complete, on one page for one client and one year or period.

## Inputs
- Read: [../shared/work-pages.md](../shared/work-pages.md), [../shared/drive-layout.md](../shared/drive-layout.md), [../shared/error-500.md](../shared/error-500.md), [../templates/page-entry.md](../templates/page-entry.md), [../templates/drive-context/year.md](../templates/drive-context/year.md).
- Data: `lists/names.md` (slot names); the client's `<Page>/<year or period>/` entry.

## Steps
1. Find the client, the page and the year or period. Provisional tax needs a period such as `1st Provisional 2027`. If the client's provisional tax is No and no Provisional Tax folder exists, say so and stop. If the client's folder holds a conflict copy, merge it first: [../shared/drive-layout.md](../shared/drive-layout.md) ("Conflict copies").
2. Match each requested status to the page's options in [work-pages.md](../shared/work-pages.md), resolving names to slots there (including "for me" and first names: "Slots and names"). A status not in that list, or a KPI status on a page without a KPI box, is not ticked: answer as [error-500.md](../shared/error-500.md) "A value that isn't an option" says.
3. Open the entry. If it exists, show what is ticked now. If it doesn't, say nothing is ticked yet and that this tick will start the entry.
4. Read back what will change: statuses to tick, to untick, Set As Complete. Wait for a clear yes.
5. If the year or period folder or entry doesn't exist (first use): create the folder with its `CONTEXT.md` from the year template, then the entry from the entry template with the exact file name.
6. Tick: add the line `<status as stored> — set by <user>, <yyyy-mm-dd hh:mm>` in the right box, using the user name from the Project instruction. Untick: remove the line. Leave other ticks and their stamps untouched.
7. Set As Complete uses the same stamp in the Complete box.

## Output
One plain line: what is now ticked.

## Human check
Step 4: the staff member confirms the ticks and unticks before the entry is written.
