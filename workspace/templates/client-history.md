# Client history

The report shown in the chat when someone asks for a client's full report or history: one client, every page, every year or period. How to pull, fill and save it: [../skills/reports.md](../skills/reports.md).

## Fill rules

- First, the rules for every HTML template: [CONTEXT.md](CONTEXT.md) ("HTML templates").
- Title: the client's name. Under it: client type, practitioner and office, as names, never slots. Pills: the client's Status, `Provisional: Yes` or `Provisional: No`, and Sign-up (Existing or New). Then one `class="f"` pill per filter ("Filters" in [../skills/reports.md](../skills/reports.md)).
- Tiles: one per page, in this order: Income Tax, Provisional Tax, Admin Penalty, FICA, Tax Clearance. Each shows how many years or periods are on file (singular for 1, plural otherwise: "1 period", "2 periods", "1 tax year"), how many are open (Set As Complete not ticked) and how many are complete.
- Sections: one per page, in the same order. One row per year or period on file, **newest first**. Provisional periods compare by year, then 1st before 2nd.
- Ticked: one `<li>` per ticked Status box option, in the page's path order ([../shared/work-pages.md](../shared/work-pages.md), "The options"). Side statuses get `class="side"`. KPI box options get `class="kpi"`. Statuses show the name in place of the slot, for example `Prep In Progress – <Name>`. Nothing ticked: `<span class="none">Nothing ticked</span>`.
- Still to happen, and the gap flag: as [../shared/work-pages.md](../shared/work-pages.md) says ("Workflow order"): the main-path steps after the furthest ticked one, ending with Set As Complete. `–` if Set As Complete is ticked. Add the `gap` line only when an earlier main-path step is not ticked. Side statuses are never listed as still to happen.
- Latest note: the last note in the entry, cut to about 80 characters (end with `…` if cut), then `<user> · <mm/dd>`. `–` if the entry has no notes.
- Complete is `✓` if Set As Complete is ticked, else `Open`.
- A page with nothing on file shows its `<section>` with the meta `nothing on file yet` and no table. A client with no Provisional Tax folder shows `not provisional` there instead.
- Full notes for a year are shown only when asked.

## HTML

```html
<style>
:root{--bg:#eef1ef;--card:#ffffff;--fg:#1b2420;--muted:#62706a;--line:#dde3e0;--head:#173f33;--head-fg:#f1f7f4;--chip:#e4efe9;--chip-fg:#1d5c46;--bar:#2f8a69;--track:#e6ece9;--ok:#1f7a55;--open:#a1462b;--open-soft:#f6e5de;--warn:#8a6a12;--warn-soft:#f6efd9;
--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#111614;--card:#1a211e;--fg:#e4ebe7;--muted:#9eaba5;--line:#2d3632;--head:#0f2c23;--head-fg:#e9f4ef;--chip:#20352c;--chip-fg:#8fd3b4;--bar:#5cc39a;--track:#25302b;--ok:#5cc39a;--open:#e98a6c;--open-soft:#3a241d;--warn:#e5c25e;--warn-soft:#352c14;color-scheme:dark}}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:14px;line-height:1.45;padding-block:20px 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.rep{max-width:1000px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.head{background:var(--head);color:var(--head-fg);padding:18px 22px;display:flex;flex-wrap:wrap;gap:10px 20px;justify-content:space-between;align-items:flex-end}
.eyebrow{font-size:11px;letter-spacing:.09em;text-transform:uppercase;opacity:.75}
h1{margin:2px 0 0;font-size:22px;line-height:1.2;text-wrap:balance}
.sub{font-size:13px;opacity:.8;margin-top:3px}
.pills{display:flex;flex-wrap:wrap;gap:6px}.pills span{font-size:12px;padding:3px 10px;border-radius:999px;background:rgba(255,255,255,.14)}
.pills span.f{background:var(--head-fg);color:var(--head);font-weight:600}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;padding:16px 22px 6px}
.tile{border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:6px;min-width:0}
.tile .t{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.tile b{font-size:14px}.tile .yr{font-family:var(--mono);font-size:12px;color:var(--muted)}
.tile .v{font-size:26px;font-weight:650;font-variant-numeric:tabular-nums;line-height:1.1}
.tile .of{font-size:14px;font-weight:500;color:var(--muted)}
.tile .l{font-size:12px;color:var(--muted)}
section{border-top:1px solid var(--line);padding:16px 22px 18px;display:flex;flex-direction:column;gap:10px}
h2{margin:0;font-size:15px;display:flex;justify-content:space-between;gap:10px;align-items:baseline;flex-wrap:wrap}
h2 .meta{font-size:12px;font-weight:500;color:var(--muted)}
h3{margin:0 0 6px;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:600}
.tbl{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:13px}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:600}
td.yr{font-family:var(--mono);white-space:nowrap;font-weight:600}
td.nm{font-weight:600;white-space:nowrap}
.chips{display:flex;flex-wrap:wrap;gap:4px;margin:0;padding:0;list-style:none}
.chips li{font-size:12px;padding:1px 7px;border-radius:5px;background:var(--chip);color:var(--chip-fg);white-space:nowrap}
.chips li.kpi{background:transparent;border:1px solid var(--chip-fg)}
.chips li.side{background:transparent;color:var(--muted);border:1px dashed var(--line)}
.next{font-size:12px;color:var(--fg)}.gap{display:block;margin-top:3px;font-size:11px;padding:1px 6px;border-radius:4px;background:var(--warn-soft);color:var(--warn);width:fit-content}
td.note{min-width:200px;max-width:280px}.by{display:block;font-family:var(--mono);font-size:11px;color:var(--muted);margin-top:2px}
.ok{color:var(--ok);font-weight:700}.open{font-size:11px;font-weight:600;padding:1px 7px;border-radius:5px;background:var(--open-soft);color:var(--open);white-space:nowrap}
.none{color:var(--muted);font-size:12px}
.foot{border-top:1px solid var(--line);padding:10px 22px;font-size:12px;color:var(--muted);display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px}
.note-out{max-width:1000px;margin:12px auto 0;font-size:12px;color:var(--muted)}
.stage{display:grid;grid-template-columns:minmax(150px,auto) 1fr auto;gap:8px;align-items:center;font-size:12px;margin-bottom:4px}
.track{height:8px;background:var(--track);border-radius:4px;overflow:hidden}.fill{display:block;height:100%;background:var(--bar)}
.stage .n{font-variant-numeric:tabular-nums;color:var(--muted);white-space:nowrap}
.years{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}
.yearcard{border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:8px;min-width:0}
.yearcard .big{font-size:22px;font-weight:650;font-variant-numeric:tabular-nums}
.cell{display:flex;flex-direction:column;gap:3px;align-items:flex-start}
.cell .st{font-size:12px;padding:1px 7px;border-radius:5px;background:var(--chip);color:var(--chip-fg);white-space:nowrap}
.cell .st.done{background:transparent;color:var(--ok);font-weight:700;padding:0}
</style>
<div class="rep">
<div class="head"><div><div class="eyebrow">Client report · every page, every year</div><h1>{{client name}}</h1><div class="sub">{{client type}} · {{practitioner}} · {{office}}</div></div><div class="pills"><span>{{Active|Inactive}}</span><span>Provisional: {{Yes|No}}</span><span>{{Existing|New}}</span><!-- repeat: one span class="f" per filter --><span class="f">{{filter chip}}</span></div></div>
<div class="tiles">
<!-- repeat: one tile per page, in order -->
<div class="tile"><div class="t"><b>{{page}}</b><span class="yr">{{n}} {{tax year(s)|period(s)}}</span></div><div class="v">{{open count}}<span class="of"> open</span></div><div class="l">{{complete count}} complete</div></div>
<!-- end repeat -->
</div>
<!-- repeat: one section per page, in order -->
<section><h2>{{page}}<span class="meta">{{n}} {{tax years|periods}} · newest first</span></h2><div class="tbl"><table style="min-width:760px"><thead><tr><th>{{Year|Period}}</th><th>Ticked</th><th>Still to happen</th><th>Latest note</th><th>Complete</th></tr></thead><tbody>
<!-- repeat: one row per year or period, newest first -->
<tr><td class="yr">{{year or period}}</td><td><ul class="chips">
<!-- repeat: one li per ticked status; class="side" for a side status, class="kpi" for a KPI option -->
<li>{{status}}</li>
<!-- end repeat -->
</ul></td><td><span class="next">{{still to happen, comma separated, or –}}</span><!-- only if a gap: --><span class="gap">{{gap line}}</span></td><td class="note">{{latest note, about 80 characters, or –}}<span class="by">{{user}} · {{mm/dd}}</span></td><td><span class="{{ok|open}}">{{✓|Open}}</span></td></tr>
<!-- end repeat -->
</tbody></table></div></section>
<!-- end repeat -->
<!-- a page with nothing on file, in place of its section above: -->
<!-- <section><h2>{{page}}<span class="meta">{{nothing on file yet|not provisional}}</span></h2></section> -->
<div class="foot"><span>Read only · not saved · ask for any year's full notes</span><span>Pulled {{yyyy-mm-dd hh:mm}} for {{user name}}</span></div>
</div>
```
