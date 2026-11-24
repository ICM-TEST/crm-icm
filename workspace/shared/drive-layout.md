# Drive layout

Everything lives under the `CLAUDE WORKSPACE FILES` folder named by `Data:` in the Project instruction: the practice's Google Drive, synced to this Mac and opened as a local folder. Every data file is a plain `.md` file. Build exactly this tree.

```
CLAUDE WORKSPACE FILES/
├─ CONTEXT.md
├─ lists/
│  ├─ CONTEXT.md
│  └─ names.md
├─ clients/
│  ├─ CONTEXT.md
│  └─ <Client Name>/
│     ├─ CONTEXT.md
│     ├─ <Client Name> – Profile.md
│     ├─ <Client Name> – Log – <user name>.md   (one per staff member, append only)
│     ├─ Income Tax/
│     │  ├─ CONTEXT.md
│     │  └─ <year>/
│     │     ├─ CONTEXT.md
│     │     └─ <Client Name> – Income Tax <year>.md
│     ├─ Provisional Tax/
│     │  ├─ CONTEXT.md
│     │  └─ <period>/
│     │     ├─ CONTEXT.md
│     │     └─ <Client Name> – <period>.md
│     ├─ Admin Penalty/     same shape: <year>/ with CONTEXT.md and <Client Name> – Admin Penalty <year>.md
│     ├─ FICA/              same shape: <Client Name> – FICA <year>.md
│     └─ Tax Clearance/     same shape: <Client Name> – Tax Clearance <year>.md
├─ outputs/
│  ├─ CONTEXT.md
│  └─ reports/
│     ├─ CONTEXT.md
│     └─ <yyyy-mm-dd hh-mm> <report title>.md   (only when someone asks to save a report)
└─ merged/      (spare copies after a merge, made on first use)
   └─ CONTEXT.md
```

## Naming

- A file's name is its title plus `.md`, for example `<Client Name> – Profile.md`, `<Client Name> – Income Tax 2026.md`, `CONTEXT.md`.
- The separator in every file name is an **en dash** with a space each side: ` – `. Never a hyphen.
- `<year>` is the four-digit tax year, for example `2027`.
- `<period>` is `<nth> Provisional <year>`, for example `1st Provisional 2027`, `2nd Provisional 2027`. A provisional period has no parent year folder.
- Page folder names are exactly: `Income Tax`, `Provisional Tax`, `Admin Penalty`, `FICA`, `Tax Clearance`.
- `<Client Name>` is the profile Name, written the same everywhere. Search for an existing client before creating one.

## CONTEXT files

Every folder holds one file named exactly `CONTEXT.md`. It says what the folder holds: what is here, what each file or subfolder is, how it is named. It holds no steps and no client data beyond the folder's own name. **A folder is created together with its CONTEXT.md, never without it.**

| Folder | Template |
|---|---|
| `CLAUDE WORKSPACE FILES/` | [../templates/drive-context/crm.md](../templates/drive-context/crm.md) |
| `lists/` | [../templates/drive-context/lists-folder.md](../templates/drive-context/lists-folder.md) |
| `clients/` | [../templates/drive-context/clients.md](../templates/drive-context/clients.md) |
| `<Client Name>/` | [../templates/drive-context/client.md](../templates/drive-context/client.md) |
| a page folder (`Income Tax/` etc.) | [../templates/drive-context/page.md](../templates/drive-context/page.md) |
| a year or period folder | [../templates/drive-context/year.md](../templates/drive-context/year.md) |
| `outputs/` | [../templates/drive-context/outputs.md](../templates/drive-context/outputs.md) |
| `outputs/reports/` | [../templates/drive-context/reports-folder.md](../templates/drive-context/reports-folder.md) |
| `merged/` | [../templates/drive-context/merged.md](../templates/drive-context/merged.md) |

[../skills/setup.md](../skills/setup.md) makes the top folders once per practice, each with its CONTEXT.md from the templates above. Every other folder is made by a skill ([../skills/CONTEXT.md](../skills/CONTEXT.md)).

## The names file

`lists/names.md` maps each slot to its display name: `Staff 1` to `Staff 4`, `Practitioner 1` to `Practitioner 2`, `Office 1` to `Office 2`. Shape: [../templates/names.md](../templates/names.md). It is filled once, by [../skills/setup.md](../skills/setup.md).

- Claude **reads** it to show and accept real names, as [work-pages.md](work-pages.md) says. After setup Claude never edits it. A request to change it or to add a slot is Error 500 ([error-500.md](error-500.md)).
- Only the practice's administrator edits that file by hand, on the system provider's say-so.
- The options themselves (statuses, client types, marital status and so on) are fixed in these rules, not on the Drive.

## Create on first use

- A year or period folder, and the entry file inside it, are created the first time someone ticks a status or writes a note for that year or period ([../skills/statuses.md](../skills/statuses.md), [../skills/notes.md](../skills/notes.md)). Never in advance.
- The Provisional Tax folder exists only for clients whose provisional tax is Yes. A client switched to No keeps the folder and its history.
- Inactive clients keep everything. Nothing is ever deleted when a client goes Inactive.

## Finding things

Find files and lines with a local text search over the folder, for example `grep -rl` for the files that hold a line, `grep -rn` for the lines. Search the narrowest folder that can hold the answer: a client's folder, or one page folder across `clients/`. Never open every client's files to answer a question; read only the files a search returns.

## Conflict copies

Google Drive for desktop can create a duplicate when two Macs change the same file before it syncs: the same name plus a suffix, for example `<Client Name> – Profile (1).md`, or a name containing "conflict". The file without the suffix is the original.
- **Reading** is fine. Reports include the client; their foot adds `<n> client(s) have a duplicate file: <names>.`
- **Before changing** a client with a copy, merge it, then carry on with the request:
  - **A log:** keep every line of both, drop exact duplicates, sort oldest first, save as the original. Tell the person: "I merged two copies of <Client>'s log; nothing was lost."
  - **A profile or entry:** lines in only one copy that are only added to (notes, log lines) are kept. For each field or tick that differs, show both in one read-back, for example "Office: <A> in one copy, <B> in the other. Which is right?", and wait for the answers. Save as the original and add the log line `Merged two copies of the <file>`. No answer: change nothing.
  - Move the spare copy to `merged/` as `<yyyy-mm-dd hh-mm> <file name>`. Never delete either copy.

`<file>` is the plain kind of file: "log", "profile" or "<page> <year or period> entry", never the file name.
