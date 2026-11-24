# templates/

Each template is the markdown body of a data file. How a template becomes a file: copy its body into a new `.md` file with the exact name given in [../shared/drive-layout.md](../shared/drive-layout.md) (the title plus `.md`), filling every `<placeholder>` from what the person confirmed. Remove any line left as an unfilled placeholder only where the template says it is optional. Never save a template itself to the Drive.

| File | Becomes |
|---|---|
| [client-profile.md](client-profile.md) | `<Client Name> – Profile.md` |
| [client-log.md](client-log.md) | `<Client Name> – Log – <user name>.md` |
| [page-entry.md](page-entry.md) | The entry file of a year or period, for any page. Leave out the KPI section for pages without a KPI box |
| [client-card.md](client-card.md) | Not a file: the HTML card shown in the chat for a client, never saved to the Drive |
| [report-dashboard.md](report-dashboard.md) | Not a file: the HTML dashboard for a status report or client list |
| [client-history.md](client-history.md) | Not a file: the HTML report of one client's full history |
| [page-years.md](page-years.md) | Not a file: the HTML report of one page across all years |

The three reports are shown in the chat; only a markdown copy is ever saved, and only when asked ([../skills/reports.md](../skills/reports.md), "Saving").
| [names.md](names.md) | `lists/names.md`, made at setup. Claude never edits it |
| [drive-context/](drive-context/) | The `CONTEXT.md` of each Drive folder, one template per level (listed in [../shared/drive-layout.md](../shared/drive-layout.md)) |

## HTML templates

The card and the three reports. Copy the HTML exactly: change only the `{{...}}` placeholders and repeat the blocks the comments name. Never change the styles, layout, order or labels, so every card and report looks the same. `{{a|b}}`: write the one that applies, e.g. `active` or `inactive`. Names are shown, never slots. The foot shows the date and time it was made and the user name from the Project instruction.
