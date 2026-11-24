# Population guide: loading existing clients (one time, at setup)

For whoever sets up a practice: the system provider, or the person they name. You do this **once**, after the
[onboarding](onboarding.md) steps 1–4 and before staff start working in the CRM. It moves the practice's existing
clients and their recent work out of the old CRM and into `CLAUDE WORKSPACE FILES`.

It runs in two phases, in this order:

| Phase | What comes over | When |
|---|---|---|
| **1. Profiles** | Every client's profile: details, bank, classification, tax categories | First, from a CSV export |
| **2. Work pages** | Income Tax, Provisional Tax, Admin Penalty, FICA, Tax Clearance: ticked statuses, Set As Complete and notes for the **last 2–3 tax years** | Once the old CRM's page export is worked out |

Older years stay in the old CRM. Keep it readable after go-live.

> **Status:** the import tools (`tools/import_profiles.py`, then a pages tool) are not built yet. They will be built
> from the sample export (step 3) and released with the version notes. Until then, follow steps 1–4 only.

## Ground rules

- **Client data never goes into this repo, an email or a chat.** The exports, the mapping and the check reports stay
  in one private folder on the Mac that runs the load, `~/crm-import/`, and nowhere else. That folder is outside Google
  Drive and outside this repo.
- **Never fix a client by hand in the output.** If something is wrong, fix the export or the mapping and run the load
  again.
- **Nothing is overwritten.** A client already on the Drive is skipped and listed in the check report.
- **One Mac, Drive online, nobody else working.** That way the load can't create duplicate copies of files.

## Before you start: checklist

- [ ] Onboarding steps 1–4 are done: `CLAUDE WORKSPACE FILES` exists, is shared and has synced.
- [ ] `lists/names.md` is filled in: staff, practitioners and offices. The import needs it to turn names into slots.
- [ ] You know the old CRM's name and who at the practice can run its exports.
- [ ] The Mac has Python 3 (`python3 --version`) and this repo cloned: `git clone <repo URL> ~/crm-icm`.
- [ ] You've made the private folder: `mkdir -p ~/crm-import`.
- [ ] You've agreed a **switch day** with the practice, the day the old CRM stops being changed.

## Phase 1: profiles

### 1. Export the clients
In the old CRM, export **all clients, Active and Inactive**, with every field it offers, as CSV. Save the file as
`~/crm-import/clients.csv`. If the CRM only exports to Excel, save it from Excel as **CSV UTF-8**.

### 2. Check the export
Open it and check:
- **one row per client** and a header row;
- the row count matches the old CRM's client count;
- the ID, tax and bank numbers are in full. Excel can turn them into `8.00101E+12` or drop leading zeros. If that
  happens, export again and open it in a text editor, not Excel.

### 3. Send the sample
Send the system provider **only the header row** plus **two made-up rows** in the same shape, never real clients. From
that they build the mapping and the import tool.

### 4. Approve the mapping
The system provider sends `mapping.md`, which pairs each old column with a profile field. For example, `Cell` becomes
Phone, `Category` becomes Client type, and `Consultant` becomes Practitioner. It also turns each old value into one of
the CRM's fixed options: for example `Yachtie` becomes Crew Yachty, and an old consultant's label becomes their
practitioner slot. Read every line. Anything marked **?** needs your answer. Save the approved file as
`~/crm-import/mapping.md`.

### 5. Dry run
Nothing is written. Run:

```bash
python3 ~/crm-icm/tools/import_profiles.py --csv ~/crm-import/clients.csv --mapping ~/crm-import/mapping.md --data "<path to CLAUDE WORKSPACE FILES>" --dry-run
```

It writes `~/crm-import/check-report.md`:

| Section | What to do |
|---|---|
| Clients found | Must match the old CRM's count |
| Values with no option | Add them to the mapping, or correct them in the old CRM and export again |
| Missing name or tax number | Fill them in the old CRM and export again |
| Possible duplicates (same name or ID number) | Decide in the old CRM which is right. Two real people with the same name get a middle initial |
| Already on the Drive | These get skipped. That's expected only when you re-run |

Repeat steps 1 and 5 until the report shows **0** in every section except "Clients found".

### 6. Test load
Load into an empty test folder first, never the real one:

```bash
mkdir -p ~/crm-import/test-load
python3 ~/crm-icm/tools/import_profiles.py --csv ~/crm-import/clients.csv --mapping ~/crm-import/mapping.md --data ~/crm-import/test-load
```

Then link `~/crm-import/test-load` to a spare Cowork project in place of `CLAUDE WORKSPACE FILES`, and check:
- [ ] **10 clients**, picked across offices and client types, including one Inactive client: "Show me <client>". Every
      field on the card matches the old CRM.
- [ ] One client with provisional tax Yes has a Provisional Tax folder, and one with No doesn't.
- [ ] "Show me <client>'s log" shows one line: `Imported from the old CRM`.
- [ ] A client list for each office (type d report): the counts match the old CRM.

If anything is wrong, delete `~/crm-import/test-load`, fix the mapping or export, and go back to step 5.

### 7. Real load (switch day)
1. Ask staff to stop changing the old CRM.
2. Export again (step 1), so the file is current, and repeat the dry run (step 5) until it's clean.
3. Run the same command with `--data` set to the real `CLAUDE WORKSPACE FILES`.
4. Wait until Google Drive for desktop says it's up to date.
5. Repeat the checks from step 6 on the real folder, from **a different staff Mac**. This proves the files synced.

## Phase 2: work pages (last 2–3 tax years)

Done after phase 1. The steps are the same: export, check, sample, mapping, dry run, test load, real load. These
differ:

- **One export per page**, if the old CRM allows it. Each needs client name, tax year or period, each ticked status
  with who and when if available, Complete, and the notes with who and when.
- **The mapping** also pairs the old CRM's status names with the fixed options in `workspace/shared/work-pages.md`. Old
  labels that differ, for example a staff nickname, map to the right slot.
- **What the import stamps:** if the old CRM doesn't export who and when, entries are stamped `Import` with the switch
  date. Imported notes carry "Imported from the old CRM" in place of a status snapshot.
- **The checks:** for 10 clients, the client history report (one client, every page and year) matches the old CRM. A
  status report for the current year has the same counts as the old CRM.

> The page import tool is designed once the old CRM's page export is known. This section gets its exact commands then.

## After the load

- [ ] Delete `~/crm-import/` (the exports, mapping and reports). It holds client data and isn't needed any more:
      `rm -rf ~/crm-import`.
- [ ] Delete `~/crm-import/test-load` and the spare Cowork project, if not already gone.
- [ ] Tell staff to start in the new CRM. New clients from now on are added in the chat ("add a new client").
- [ ] Keep the old CRM readable, but not edited, for the years older than the 2–3 that came over.
