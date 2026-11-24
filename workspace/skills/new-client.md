# New client

## Inputs
- Read: [../shared/client-fields.md](../shared/client-fields.md), [../shared/drive-layout.md](../shared/drive-layout.md), [../templates/client-profile.md](../templates/client-profile.md), [../templates/client-log.md](../templates/client-log.md), [../templates/drive-context/client.md](../templates/drive-context/client.md), [../templates/drive-context/page.md](../templates/drive-context/page.md).
- Data: `lists/names.md` (to show practitioner and office names); `clients/` (to check the client doesn't exist, searching as [../shared/drive-layout.md](../shared/drive-layout.md) says, "Finding things").

## Steps
1. Search `clients/` for the name. If a folder exists, stop and say so.
2. Ask the fields one group at a time (personal, bank, classification). Offer the fixed options for client type, and the practitioner and office names from `names`. Store practitioner and office as [work-pages.md](../shared/work-pages.md) says. Provisional tax: ask Yes or No, never assume. Income tax is Yes, don't ask. Status, sign-up and Balance due start as [client-fields.md](../shared/client-fields.md) says ("Classification"); ask sign-up.
3. Read the whole profile back, grouped, every number in full, sensitive fields included, so a typo can be caught. Wait for a clear yes.
4. Create `clients/<Client Name>/`, with its `CONTEXT.md` from the client template.
5. Create `<Client Name> – Profile.md` from the profile template.
6. Create `<Client Name> – Log – <user name>.md` from the log template. First line: `Client created`, stamped with the user name and date and time.
7. Create the page folders `Income Tax`, `Admin Penalty`, `FICA`, `Tax Clearance`, and `Provisional Tax` only if provisional tax is Yes. Each gets its `CONTEXT.md` from the page template.
8. Create no year or period folders. They appear on first use.

## Output
One plain line: the client is set up, and whether Provisional Tax was included.

## Human check
Step 3: the staff member confirms every field before anything is written.
