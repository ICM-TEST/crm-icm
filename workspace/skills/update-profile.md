# Update profile

## Inputs
- Read: [../shared/client-fields.md](../shared/client-fields.md), [../shared/error-500.md](../shared/error-500.md), [../templates/drive-context/page.md](../templates/drive-context/page.md).
- Data: `<Client Name> – Profile.md` and `<Client Name> – Log.md` in `clients/<Client Name>/`; `lists/names.md` for practitioner and office names.

## Steps
1. Find the client. If several match, ask which.
2. Check the request against [client-fields.md](../shared/client-fields.md). Income tax set to No: Error 500 with its reason line. Any value that isn't an option: answer as [error-500.md](../shared/error-500.md) "A value that isn't an option" says. Store practitioner and office as [work-pages.md](../shared/work-pages.md) says.
3. Read back: field, old value, new value. Sensitive fields too are shown in full, old and new, so a typo can be caught. (The log line still hides them.) Wait for a clear yes.
4. Write the change to the profile. First, if the client's folder holds a conflict copy, stop: [../shared/drive-layout.md](../shared/drive-layout.md) ("Conflict copies").
5. Append one line to the log: date and time, user name, Google account, description, worded as [client-fields.md](../shared/client-fields.md) says ("The client log"). Never edit or delete an earlier line.
6. Provisional tax No to Yes: if `Provisional Tax/` doesn't exist, create it with its `CONTEXT.md` from the page template. Yes to No: change only the field; keep the folder and its history.
7. Several fields in one request: one read-back, one log line per field.

## Output
One plain line saying what changed.

## Human check
Step 3: the staff member confirms the change before the profile or log is written.
