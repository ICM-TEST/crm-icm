# Page across years

The report shown in the chat when someone asks for one page across all years: all active clients, every year or period on file. How to pull, fill and save it: [../skills/reports.md](../skills/reports.md).

## Fill rules

- First, the rules for every HTML template: [CONTEXT.md](CONTEXT.md) ("HTML templates").
- Title: `<Page> · <years or periods on file, oldest to newest>`. Pills: `Active clients only` (plus `Provisional: Yes` for provisional tax), then one `class="f"` pill per filter, as "Filters" in [../skills/reports.md](../skills/reports.md) says. Names, never slots.
- **Filters:** all counts follow them; show the scope block only when filters are on.
- **In scope:** the active clients the report covers. For provisional tax: active clients with provisional tax Yes.
- Provisional tax uses periods (`1st Provisional 2027`, `2nd Provisional 2027`) in place of years, oldest to newest.
- Year cards: one per year or period on file, oldest to newest.
  - **Started** means the client has an entry for that year. The card says `<started> of <in scope> clients started · <percent>%` (whole number).
  - Complete: started clients with Set As Complete ticked. Open: started clients without it. Not started: in scope minus started.
  - Stage bars: one per main-path step of the page ([../shared/work-pages.md](../shared/work-pages.md), "Workflow order"), in path order, ending with Set As Complete (the last main-path step). Leave out a step no client is at. Each client counts once, at the **furthest** main-path step ticked in its entry for that year. Count is `<clients at that step> / <started>`, and bar width is that same share as a percent. A step is named without its slot: `Prep In Progress`, `Prepped` for Prepped File, Prepped Full or E-filing Prepped Only. An entry with only side statuses ticked is counted in started but at no step.
- Table: one row per client, sorted by client name, with the practitioner as a name, and one column per year or period, oldest to newest.
  - A cell shows the furthest main-path step ticked. A complete entry's furthest step is Set As Complete, so its cell shows only `✓ Complete` (`class="st done"`). An entry with only side statuses shows them as dashed chips (`class="side"`), never `–`. `<span class="none">–</span>` means no entry at all.
  - The meta says `furthest main-path step per year · <shown> of <in scope> shown`.
- **Large lists:** if more than 200 clients are in scope, show the year cards and leave the table out, unless the request narrows it. Replace the table `<section>` with one line, and say in the foot how to narrow it: by practitioner, office, client type, or open only.

## HTML

```html
<style>:root{--bg:#eef1ef;--card:#ffffff;--fg:#1b2420;--muted:#62706a;--line:#dde3e0;--head:#173f33;--head-fg:#f1f7f4;--chip:#e4efe9;--chip-fg:#1d5c46;--bar:#2f8a69;--track:#e6ece9;--ok:#1f7a55;--open:#a1462b;--open-soft:#f6e5de;--warn:#8a6a12;--warn-soft:#f6efd9;--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#111614;--card:#1a211e;--fg:#e4ebe7;--muted:#9eaba5;--line:#2d3632;--head:#0f2c23;--head-fg:#e9f4ef;--chip:#20352c;--chip-fg:#8fd3b4;--bar:#5cc39a;--track:#25302b;--ok:#5cc39a;--open:#e98a6c;--open-soft:#3a241d;--warn:#e5c25e;--warn-soft:#352c14;color-scheme:dark}}body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:14px;line-height:1.45;padding-block:20px 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}.rep{max-width:1000px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}.head{background:var(--head);color:var(--head-fg);padding:18px 22px;display:flex;flex-wrap:wrap;gap:10px 20px;justify-content:space-between;align-items:flex-end}.eyebrow{font-size:11px;letter-spacing:.09em;text-transform:uppercase;opacity:.75}h1{margin:2px 0 0;font-size:22px;line-height:1.2;text-wrap:balance}.sub{font-size:13px;opacity:.8;margin-top:3px}.pills{display:flex;flex-wrap:wrap;gap:6px}.pills span{font-size:12px;padding:3px 10px;border-radius:999px;background:rgba(255,255,255,.14)}.pills span.f{background:var(--head-fg);color:var(--head);font-weight:600}.scope{padding:18px 22px 4px;display:flex;flex-direction:column;gap:8px}.sv{font-size:16px}.sv b{font-size:20px;font-variant-numeric:tabular-nums}.pct{margin-left:6px;font-size:13px;font-weight:600;padding:2px 8px;border-radius:999px;background:var(--chip);color:var(--chip-fg)}.track.big{height:12px;border-radius:6px}.sl{font-size:12px;color:var(--muted)}.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;padding:16px 22px 6px}.tile{border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:6px;min-width:0}.tile .t{display:flex;justify-content:space-between;align-items:baseline;gap:8px}.tile b{font-size:14px}.tile .yr{font-family:var(--mono);font-size:12px;color:var(--muted)}.tile .v{font-size:26px;font-weight:650;font-variant-numeric:tabular-nums;line-height:1.1}.tile .of{font-size:14px;font-weight:500;color:var(--muted)}.tile .l{font-size:12px;color:var(--muted)}section{border-top:1px solid var(--line);padding:16px 22px 18px;display:flex;flex-direction:column;gap:10px}h2{margin:0;font-size:15px;display:flex;justify-content:space-between;gap:10px;align-items:baseline;flex-wrap:wrap}h2 .meta{font-size:12px;font-weight:500;color:var(--muted)}h3{margin:0 0 6px;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:600}.tbl{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:13px}th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:600}td.yr{font-family:var(--mono);white-space:nowrap;font-weight:600}td.nm{font-weight:600;white-space:nowrap}.chips{display:flex;flex-wrap:wrap;gap:4px;margin:0;padding:0;list-style:none}.chips li{font-size:12px;padding:1px 7px;border-radius:5px;background:var(--chip);color:var(--chip-fg);white-space:nowrap}.chips li.kpi{background:transparent;border:1px solid var(--chip-fg)}.chips li.side{background:transparent;color:var(--muted);border:1px dashed var(--line)}.next{font-size:12px;color:var(--fg)}.gap{display:block;margin-top:3px;font-size:11px;padding:1px 6px;border-radius:4px;background:var(--warn-soft);color:var(--warn);width:fit-content}td.note{min-width:200px;max-width:280px}.by{display:block;font-family:var(--mono);font-size:11px;color:var(--muted);margin-top:2px}.ok{color:var(--ok);font-weight:700}.open{font-size:11px;font-weight:600;padding:1px 7px;border-radius:5px;background:var(--open-soft);color:var(--open);white-space:nowrap}.none{color:var(--muted);font-size:12px}.foot{border-top:1px solid var(--line);padding:10px 22px;font-size:12px;color:var(--muted);display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px}.note-out{max-width:1000px;margin:12px auto 0;font-size:12px;color:var(--muted)}.stage{display:grid;grid-template-columns:minmax(150px,auto) 1fr auto;gap:8px;align-items:center;font-size:12px;margin-bottom:4px}.track{height:8px;background:var(--track);border-radius:4px;overflow:hidden}.fill{display:block;height:100%;background:var(--bar)}.stage .n{font-variant-numeric:tabular-nums;color:var(--muted);white-space:nowrap}.years{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}.yearcard{border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:8px;min-width:0}.yearcard .big{font-size:22px;font-weight:650;font-variant-numeric:tabular-nums}.cell{display:flex;flex-direction:column;gap:3px;align-items:flex-start}.cell .st{font-size:12px;padding:1px 7px;border-radius:5px;background:var(--chip);color:var(--chip-fg);white-space:nowrap}.cell .st.done{background:transparent;color:var(--ok);font-weight:700;padding:0}</style>
<div class="rep">
<div class="head"><div><div class="eyebrow">Page report · every year</div><h1>{{page}} · {{years or periods, oldest to newest}}</h1></div><div class="pills">
<span>Active clients only</span>
<!-- repeat: one span per filter -->
<span class="f">{{filter chip}}</span>
<!-- end repeat -->
</div></div>
<!-- scope block: only when filters are on -->
<section style="border-top:0"><div class="scope"><div class="sv"><b>{{matches}}</b> of <b>{{all active}}</b> active clients match the filters <span class="pct">{{percent}}%</span></div><div class="track big"><span class="fill" style="width:{{percent}}%"></span></div><div class="sl">In scope: {{the filters, in words}}. Every number below counts only these {{matches}}.</div></div></section>
<section style="border-top:0"><div class="years">
<!-- repeat: one yearcard per year or period on file, oldest to newest -->
<div class="yearcard"><div class="t" style="display:flex;justify-content:space-between;align-items:baseline"><b style="font-family:var(--mono);font-size:16px">{{year or period}}</b><span class="none">{{started}} of {{in scope}} clients started · {{percent}}%</span></div><div style="display:flex;gap:18px"><div><div class="big" style="color:var(--ok)">{{complete}}</div><div class="none">complete</div></div><div><div class="big" style="color:var(--open)">{{open}}</div><div class="none">open</div></div><div><div class="big">{{not started}}</div><div class="none">not started</div></div></div><h3>Clients at each step</h3>
<!-- repeat: one stage bar per main-path step, in path order; width = clients at the step / started -->
<div class="stage"><span>{{step}}</span><span class="track"><span class="fill" style="width:{{percent}}%"></span></span><span class="n">{{clients at step}} / {{started}}</span></div>
<!-- end repeat -->
</div>
<!-- end repeat -->
</div></section>
<!-- omit this section when more than 200 clients are in scope and the request has not narrowed it -->
<section><h2>Where each client stands<span class="meta">furthest main-path step per year · {{shown}} of {{in scope}} shown</span></h2>
<div class="tbl"><table style="min-width:680px"><thead><tr><th>Client</th><th>Practitioner</th>
<!-- repeat: one th per year or period, oldest to newest -->
<th>{{year or period}}</th>
<!-- end repeat -->
</tr></thead><tbody>
<!-- repeat: one row per client, sorted by name -->
<tr><td class="nm">{{client name}}</td><td>{{practitioner}}</td>
<!-- repeat: one td per year or period, same order as the headings -->
<td><div class="cell"><span class="st">{{furthest step}}</span><span class="st done">✓ Complete</span></div></td>
<!-- no entry that year: <td><span class="none">–</span></td> ; Set As Complete not ticked: leave out the done span -->
<!-- end repeat -->
</tr>
<!-- end repeat -->
</tbody></table></div></section>
<div class="foot"><span>Read only · not saved · {{foot line: narrowing hint when the table is left out, else: large lists show the year summaries first; ask to narrow the client table}}</span><span>Pulled {{yyyy-mm-dd hh:mm}} for {{user name}}</span></div>
</div>
```
