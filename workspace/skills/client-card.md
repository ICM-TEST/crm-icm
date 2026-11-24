# Client card

Show one client as the standard card when someone asks to "show me" or open a client, or see their profile. The card shows the **latest year** only. "The full report" or "the history" of a client, every page and every year, is [reports.md](reports.md), type (b).

## Inputs
- Read: [../templates/client-card.md](../templates/client-card.md), [../shared/work-pages.md](../shared/work-pages.md) (slots and names), [../shared/drive-layout.md](../shared/drive-layout.md).
- Data: `clients/<Client Name>/<Client Name> – Profile.md`; in each page folder, the latest year or period folder's entry; `lists/names.md`.

## Steps
1. Find the client. If several match, ask which. If none, say so.
2. Read the Profile, then the latest entry on each page, as the card template's fill rules say.
3. Fill the card template and render it in the chat, as [../CLAUDE.md](../CLAUDE.md) says ("How you talk to people"), as an HTML artifact titled `<Client Name>`. Nothing else in the reply but one short line, for example "Here's <Client Name>'s card."
4. Write nothing, and add no log line. The card is read only.

## After the card
A change asked for from the card goes to its own skill ([update-profile.md](update-profile.md), [statuses.md](statuses.md), [notes.md](notes.md)), with its own read-back. Show a fresh card only if asked.

## Human check
None: nothing is written.
