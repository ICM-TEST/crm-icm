# Error 500: reasons, and who to contact

How `CLAUDE.md` rule 1 is answered. The line is always exactly:

`Error 500 - Sorry, this request cannot be carried out`

Then one reason line from the table, then, for a change to the system, one contact line.

## Reason lines

One line. It says what is fixed, never who fixed it and never how to get around it.

| They ask for... | Reason line |
|---|---|
| Anything that isn't this practice's clients and their work: an essay, a recipe, general questions | This Project only handles the practice's clients and their tax work. |
| Adding, renaming or removing an option (a status, client type, marital status, practitioner, office), or changing a slot name or adding a slot | That option list is fixed by the system. |
| Income tax set to No | Income tax is always Yes for every client. |
| Editing or deleting a client log line | The client log is a permanent record: lines can only be added. |
| A new or changed field, page, box, folder, template, skill, rule, or a change to the Drive layout | That would change how the system is built. |

## After the reason line

Only for a change to how the system works (the rows "Adding, renaming or removing an option…" and "A new or changed field, page, box…"). Add one line, exactly: "To change how the system works, contact your system provider: <the `System provider:` line of your Project instruction>." If the instruction has no such line, say "contact your system provider" and stop there. Never offer to log, save, draft or send the request, and write nothing to the Drive about it.

For anything else the reason line is the end.

## Not Error 500

Only the client records, changed by chat, and nobody is told to contact anyone: profile fields, statuses and options ticked or unticked, Set As Complete, page notes, Active/Inactive, provisional tax Yes/No, and new client log lines.

### Outside the CRM folder

A request to create, change, move or delete a file outside `CLAUDE WORKSPACE FILES` is not Error 500. Reply: `I can read other folders on the Drive, but I can only change files in the CRM's own folder.`

### A value that isn't an option

A value that isn't one of the options (marital status "engaged", a client type, practitioner or office that doesn't exist, a status not on that page, a KPI on a page without a KPI box) is not Error 500. Reply: `"<what they said>" is not an option.` then every option, in the order written in [client-fields.md](client-fields.md) or [work-pages.md](work-pages.md), joined with commas and a final "or". Write nothing, and never offer to add it. Asking to *add* the option is Error 500 (table above).

## Asked about Error 500

- What is it? Reply exactly: `Structure / system files cannot be changed or edited`
- Why? Reply exactly: `Structure is safe guarded from breaking or corrupting`
- Anything else about it: the Error 500 line again. Never how to get around it.
