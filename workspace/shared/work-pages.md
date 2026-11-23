# Work pages

A client has one page for each type of work. A page is a folder of entries: one **entry** (a `.md` file) per tax year, or per period for provisional tax. Layout and file names: [drive-layout.md](drive-layout.md). The pages, boxes and every option below are structure: users select options, they never add, rename or remove one. That request is Error 500.

| Page | Folder | Entry per | Status box | KPI box | Complete box | Notes |
|---|---|---|---|---|---|---|
| Income tax | `Income Tax` | tax year | yes | yes | yes | yes |
| Provisional tax | `Provisional Tax` | period | yes | yes | yes | yes |
| Admin penalty | `Admin Penalty` | tax year | yes | no | yes | yes |
| FICA | `FICA` | tax year | yes | no | yes | yes |
| Tax clearance | `Tax Clearance` | tax year | yes | no | yes | yes |

Every client has Income Tax, Admin Penalty, FICA and Tax Clearance. Only clients with provisional tax Yes get Provisional Tax; a client switched to No keeps it.

## The options

Boxes are tick boxes: several options can be ticked at once, in every box. `Staff 1` to `Staff 4` are slots, resolved as in "Slots and names" below. **Complete box, every page:** Set As Complete.

**Income tax, Status (21):** Access Received · Audit · Audit Prepped · Audit Submitted · Await Access · Dispute · Docs Partially Received · Docs Received · E-filing Prepped Only · Invoiced · New Clients · Prep In Progress – Staff 1 · Prep In Progress – Staff 2 · Prep In Progress – Staff 3 · Prep In Progress – Staff 4 · Prepped File · Prepped Full · Recon Sent · Self-Assessment Issued · Submitted · Unresponsive

**Income tax, KPI:** Prep Success – Staff 2 · Prep Success – Staff 3 · Prep Success – Staff 4 · Submitted – Staff 4

**Provisional tax, Status:** Docs Received · Invoiced · No Response – Table · Not Responded – Default Yes · Prepped · Submitted · Unresponsive / No Info · Yes Response

**Provisional tax, KPI:** Submitted – Staff 2 · Submitted – Staff 4

**Admin penalty, Status:** Await Client · Invoiced · Paid · Remittance Awarded · Remittance Denied · SARS Penalty Notice Issued · Submitted

**FICA, Status:** Await Client · Client Unresponsive · Invoiced · Requested By SARS · Submitted

**Tax clearance, Status:** Docs Partially Received · Invoiced · Requested · Submitted

A requested status that is not in the page's list above is answered as [error-500.md](error-500.md) "A value that isn't an option" says.

## Workflow order

The usual order of each page's main steps. Side statuses sit outside the path. **The path never restricts ticking:** any option can be ticked at any time, in any order, with any other. Never refuse, warn about or question a tick because of the path. It is used only to say where a client stands and what still needs to happen.

| Page | Main path | Side statuses |
|---|---|---|
| Income tax | New Clients → Await Access → Access Received → Docs Partially Received → Docs Received → Prep In Progress (any staff) → Prepped File, Prepped Full or E-filing Prepped Only → Submitted → Invoiced → Set As Complete | Recon Sent, Self-Assessment Issued, Unresponsive, Dispute. Audit branch: Audit → Audit Prepped → Audit Submitted |
| Provisional tax | Docs Received → Prepped → Submitted → Invoiced → Set As Complete | Yes Response, Not Responded – Default Yes, No Response – Table, Unresponsive / No Info |
| Admin penalty | SARS Penalty Notice Issued → Await Client → Submitted → Remittance Awarded or Remittance Denied → Invoiced → Paid → Set As Complete | none |
| FICA | Requested By SARS → Await Client → Submitted → Invoiced → Set As Complete | Client Unresponsive |
| Tax clearance | Requested → Docs Partially Received → Submitted → Invoiced → Set As Complete | none |

**What still needs to happen:** find the furthest main-path step that is ticked. The steps after it are still to happen. Earlier main-path steps that aren't ticked are not "still to happen": name them all together in one line, as a possible gap to check, for example "Not ticked, though later steps are: Docs Received, Prepped." Side statuses ticked are listed as they are.

## Slots and names

Options, and the profile's practitioner and office, use slots (`Staff 1`, `Practitioner 1`, `Office 1`). The real names are in `lists/names.md` in the data folder ([drive-layout.md](drive-layout.md)).

- **Reading:** a person may say a status or practitioner with a real name, for example "Prep In Progress <Name>". Look the name up in `names.md`, and use that slot.
- **Storing:** write the slot plus the name in brackets, for example `Prep In Progress – Staff 2 (<Name>)`, `Practitioner 1 (<Name>)`. The bracketed name is read from `names.md` at the time of writing. If the slot's name is blank, write the slot alone. This way an entry still reads correctly if `names.md` changes later. The repo holds only the slot.
- **Showing:** show the bracketed name in place of the slot. Never show a slot to a person when a name exists.
- **"For me", or a staff first name:** "me" or "for me" means the Staff slot whose name in `names.md` matches the user name in the Project instruction. A first name such as "Prep In Progress Ben" means the slot whose name matches. No match, or more than one: ask which staff member is meant, offering the names from `names.md`.
- Never edit `names.md`. A request to change a name, or to add a slot, is Error 500.

## Stamping

Every date and time stamp (ticks, notes, log lines, card foot) is the current date and time in South African time (SAST), at the moment of writing, in the form `yyyy-mm-dd hh:mm`. If you can't tell the current time, ask the person once in the chat and use their answer.

Each ticked status records who set it (user name) and the date and time, as `<status> — set by <user>, <yyyy-mm-dd hh:mm>`, with `<status>` stored as above. Unticking removes the line. A status ticked again gets a new stamp. No other dates, amounts or SARS references are kept on a page.

## Entry per year or period

The entry file ([../templates/page-entry.md](../templates/page-entry.md)) holds that year's ticked statuses and notes. It is created on first use, with its folder, for any year or period, including future ones. Period names: `1st Provisional 2027`, `2nd Provisional 2027`; no parent year.

## Notes

Per entry. Each note: date, time, user name only (no Google account), the note in plain text, and under it a snapshot of every status ticked in that entry at the moment it was written (stored as above). The snapshot is frozen: it records the ticks at that moment and is never updated afterwards. Unticking a status later doesn't change old snapshots, and correcting a note keeps its original snapshot. **Newest last.** Notes can be corrected or removed (unlike the client log). Steps: [../skills/notes.md](../skills/notes.md).
