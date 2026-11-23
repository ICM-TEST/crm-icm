# Look-up

Answer a read-only question about **one client**. Each kind of question gets one answer form. A list or count across clients is not a look-up: it goes to [reports.md](reports.md).

| Question | Answer |
|---|---|
| One profile fact, e.g. "what's Sam Naidoo's phone number?" | One plain line |
| The whole client or profile | The client card ([client-card.md](client-card.md)) |
| "What's ticked on X's <page> <year or period>?" | A short list of each ticked option with who set it and when, plus Set As Complete if ticked. If there is no entry: "Nothing yet for <page> <year>" |
| "What still needs to happen for X?" (a page and year or period) | Done so far, still to happen, any gap flagged, and the latest note, as [work-pages.md](../shared/work-pages.md) "Workflow order" says. One short block, read only |
| "Show the notes" for an entry | The notes in order, each with date, time, user and its snapshot |
| "Show me the log" | The log lines as a simple table: date and time, user, change. Leave out the Google account column unless asked |
| Several clients at once, e.g. "who is submitted?", "how many are open?" | [reports.md](reports.md) |

It writes nothing and adds no log line.

## Inputs
- Read: [../shared/work-pages.md](../shared/work-pages.md), [../shared/drive-layout.md](../shared/drive-layout.md) (including "Finding things"), [../shared/client-fields.md](../shared/client-fields.md).
- Data: `lists/names.md` (slot names); the client's profile, log, or `<Page>/<year or period>/` entry, as asked.

## Steps
1. Find the client. If several match, ask which.
2. Work out which kind of question it is, from the table.
3. Read only what that question needs. Show names, not slots, as [work-pages.md](../shared/work-pages.md) says ("Slots and names").
4. Answer in the form the table gives.

## Output
The answer in that form, in plain words.

## Human check
None, nothing is written.
