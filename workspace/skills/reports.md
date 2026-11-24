# Reports

A report is a live view: it is looked at, not kept. Nothing is saved unless the person asks.

## Report types

| Type | Asked as | Template |
|---|---|---|
| (a) Status report | A list or count across clients, e.g. "all provisional clients that are submitted" | [../templates/report-dashboard.md](../templates/report-dashboard.md) |
| (b) Client history | "The full report" or "the history" of one client: every page, every year | [../templates/client-history.md](../templates/client-history.md) |
| (c) Page across years | One page for all clients, every year or period | [../templates/page-years.md](../templates/page-years.md) |
| (d) Client list | Clients by profile data, e.g. "all clients in one office" | [../templates/report-dashboard.md](../templates/report-dashboard.md), client list mode |

- **(a)** is the dashboard below: Inputs, "What a status report needs" and Steps are its own.
- **(b)** Find the client ([../shared/drive-layout.md](../shared/drive-layout.md), "Finding things"). Read that client's folder only: the profile and every entry. Fill `client-history.md`.
- **(c)** One page, all active clients (provisional tax: provisional Yes only), every year or period on file. Search that page's folders across `clients/` as "Finding things" says, and read only what the cards and the table need. Fill `page-years.md`.
- **(d)** Active clients matching the filters, with no page or status. Only the profile search is needed. Fill the dashboard in client list mode (the template's fill rules).

All four are shown in the chat as [../CLAUDE.md](../CLAUDE.md) says, are read only, are saved only when asked (see "Saving"), and take follow-up questions as "Follow-up questions" says. A single card of the latest year is [client-card.md](client-card.md), not (b).

## Filters

Every report type links here. Any report can be filtered by **any data shown on it**: office, practitioner, client type, rental income, sign-up, language, provisional, any ticked status or KPI option, Complete or still open, who last set a status, a date range for when it was set, and words in the latest note. **Filters combine.**

- **Apply them cheaply.** Profile filters go into the profile search. Status filters go into the entry search, as an exact line. "Last set by" and dates are read from the stamp lines. Note words come from searching the entry's Notes section. Never open every client.
- **The whole report follows the filters:** scope, tiles, bars, year cards and table count only the filtered clients. The in-scope sentence names the filters.
- **Chips** (`class="f"`, after the fixed chips such as "Active clients only") show only filters other than page, year or period and status, which are in the title: e.g. `Office: <name>`, `Rental income: Yes`.
- **A breakdown a filter fixes is swapped out.** Filtered to one office, the office bars give way to sign-up bars, then rental income, then language: the first one no filter fixes.
- **Client history** (one client) takes filters on its own data only, such as years, pages or open only. It still shows a chip for each.
- **Filters carry forward.** They stay on for follow-ups and narrower versions until the person changes them or says "clear filters". A new report starts with none, unless the person says "same filters".
- A value that isn't an option is answered as [error-500.md](../shared/error-500.md) ("A value that isn't an option") says.

## (a) Status report

### Inputs
- Read: [../templates/report-dashboard.md](../templates/report-dashboard.md), [../shared/work-pages.md](../shared/work-pages.md) (pages, options, slots and names), [../shared/client-fields.md](../shared/client-fields.md), [../shared/drive-layout.md](../shared/drive-layout.md) ("Finding things", "Conflict copies").
- Data: `lists/names.md`; the asked page's entries and the profiles of the clients that match, under `clients/`.

### What a status report needs

| Filter | Rule |
|---|---|
| Page | Required: one of the five pages |
| Year or period | Required, for example `2027` or `1st Provisional 2027` |
| What is asked | One of: one or more statuses, a KPI option, or Complete / not complete |
| Any other filter | Optional, see "Filters" |

- **Active clients only**, always.
- Provisional tax: only clients whose provisional tax is **currently Yes**.
- A KPI on a page without a KPI box is not an option (see "Filters"). If page, year or period is missing, ask.

### Steps
1. Work out the filters from the request. Resolve names to slots as [work-pages.md](../shared/work-pages.md) says.
2. **Pull the matches.** Search the asked page's entries for the exact stored status line, which starts `- <status as stored> —` (the status with its slot and bracketed name, as stored). Exact-line matching keeps "Submitted" from matching "Audit Submitted". For Complete, search the line `- Set As Complete: ticked`. For not complete, take the entries that lack it. Search only the page's folder for that year or period across `clients/`, as "Finding things" says.
3. **Check each match's profile** with a search too: `Status: Active`, and for provisional tax `Provisional tax: Yes`; for any other profile filter, that profile line, and the stamp and note filters from the entry. Drop clients that fail.
4. **Count what is in scope:** the active clients the report covers. For provisional tax, that means active clients with provisional tax Yes. Count from the profile search; do not open every client. Count it per practitioner, per office and per client type as well, from the same search, for the breakdown bars.
5. Read only the matching entries and profiles, for the ticked statuses, who set the newest one and when, the last note (in the same search, so no extra file is opened), Set As Complete, client type, practitioner and office.
6. **Compute** the counts, percentages and the breakdowns (practitioner, office, client type) as the dashboard template says.
7. **Show** the report: fill [../templates/report-dashboard.md](../templates/report-dashboard.md) and render it in the chat, as [../CLAUDE.md](../CLAUDE.md) says ("How you talk to people"). Nothing else in the reply but one line saying what was understood: "Here's <report title, with its filters>.", for example "Here's Provisional Tax · 1st Provisional 2027 · Submitted · <Office>." This applies to every report type.

A client with a conflict copy is still included; add the foot line ([drive-layout.md](../shared/drive-layout.md), "Conflict copies").

## Follow-up questions
Questions about a shown report are read only.
- Answer from the rows already pulled. Use one more small search only when the question needs data that wasn't pulled, for example rental income or a client's notes.
- "Those" or "them" means the most recent list given in the chat, narrowed ones included: after "which are still open?", "which of those are <practitioner>'s?" means the open ones.
- A number or a few names gets a plain line. A new or narrowed list gets a fresh dashboard.
- A change asked for from a report goes through its own skill, with its own read-back: [update-profile.md](update-profile.md), [statuses.md](statuses.md), [notes.md](notes.md).

## Saving
Only when the person asks ("save this report"). Write `outputs/reports/<yyyy-mm-dd hh-mm> <report title>.md`. The report title is the dashboard title with its filters, e.g. `Provisional Tax · 1st Provisional 2027 · Submitted · <Office> · <Practitioner>`, cut only if over 100 characters. It holds:
- the title and the filters,
- when it was pulled and the user name,
- the totals (the four tile figures),
- the client table in markdown, with the dashboard's columns.

Create `outputs/reports/` with its `CONTEXT.md` if it is missing. Never overwrite a saved report. Never edit or delete one: reply `Saved reports are kept as they are. Your administrator can remove them from the Drive.`

## Output
The dashboard in the chat. After a save, one plain line saying it was saved.

## Human check
None, unless saving: the person confirms the save, with the file name, before it is written.
