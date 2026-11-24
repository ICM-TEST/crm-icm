# Report dashboard

The dashboard shown in the chat for a report. How to pull, fill and save it: [../skills/reports.md](../skills/reports.md).

## Fill rules

- First, the rules for every HTML template: [CONTEXT.md](CONTEXT.md) ("HTML templates").
- Title: `<Page> · <year or period> · <status filter>`, then every other filter, all in chip order, e.g. `Provisional Tax · 1st Provisional 2027 · Submitted · <Office> · <Practitioner>`. The status filter is the status or statuses (joined with "or"), the KPI option, or `Complete` / `Not complete`. Names, never slots.
- **Negative status** (e.g. "not submitted"): the matches are the in-scope clients **without** it. Tile 1 reads "Not at <status>" and tile 4 "At <status>".
- **No status filter** (only a note-word or profile filter): leave out tiles 1 and 4. The scope line reads `<matches> of <in scope> clients match`.
- Filter chips: always the fixed chip `Active clients only`, plus `Provisional: Yes` for provisional tax. Then one `class="f"` chip per filter. The filters, the scope sentence, the swapped breakdowns and the bars all follow "Filters" in [../skills/reports.md](../skills/reports.md).
- Scope line: `{{matches}}` of `{{in scope}}` clients in scope, and the percent (matches ÷ in scope, whole number). The progress bar width is that same percent. The line under the bar says what "in scope" means for this report and what the rest are not.
- The four tiles, each count / base and percent (whole numbers):
  1. matches / in scope.
  2. matches with Set As Complete ticked / matches.
  3. matches still open (Set As Complete not ticked) / matches.
  4. in scope but not matching / in scope.
- Breakdown bars: one block each for practitioner, office and client type (client type: top 5 only). Largest number of matches first, ties by name A–Z; the top 5 counts only groups with at least one match. Each bar compares that group's matches with that group's in-scope clients: the count is `<matches> / <group in scope> · <percent>%`, and bar width = matches ÷ group in scope, as a percent. The bar label is the name only, never a slot, exactly as in the table.
- Filters and sorting: the hint line, the `fbar` block and the `<script>` are copied exactly as written and never filled or changed. They work from the table's own text: a bar is clickable when its block heading starts "By practitioner", "By office" or "By client type", so keep those headings as written, keep bar labels identical to the table cells, and keep the table's eight columns in this order. Swapped-in blocks (sign-up, rental income, language) show but aren't clickable.
- Table: one row per match, sorted by client name. Ticked statuses are the entry's Status box options as chips; KPI box options get `class="kpi"`. Last set by is the user and date and time of the newest stamp in the entry, as `<user> · <mm/dd hh:mm>`. Latest note is the last note in the entry: its text cut to about 80 characters (end with `…` if cut), then `<user> · <mm/dd>`; `–` if the entry has no notes. Complete is `✓` if Set As Complete is ticked, else `Open`.
- No matches: leave the table body empty and add one row with `<td colspan="7">No clients match</td>`; every count is 0 and every bar width 0%.
- **For a client list (type (d)),** use the same HTML in client list mode, with changes.
  - Title: `<filters> clients`, e.g. `All <Office> clients`. Scope line: `<matches> of <all active> active clients`.
  - Leave out the four tiles, the hint line, the `fbar` block and the `<script>`.
  - Breakdowns: practitioner, provisional, client type (top 5), each as count / matches.
  - Table columns: Client, Client type, Practitioner, Office, Provisional, Sign-up. Only the profile search is needed.

## HTML

```html
<style>
/* Layout: one report panel in the client-card family: dark header band, count tiles, breakdown bars, then the client table */
:root{--bg:#eef1ef;--card:#ffffff;--fg:#1b2420;--muted:#62706a;--line:#dde3e0;--head:#173f33;--head-fg:#f1f7f4;--chip:#e4efe9;--chip-fg:#1d5c46;--bar:#2f8a69;--track:#e6ece9;--ok:#1f7a55;--open:#a1462b;--open-soft:#f6e5de;
--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#111614;--card:#1a211e;--fg:#e4ebe7;--muted:#9eaba5;--line:#2d3632;--head:#0f2c23;--head-fg:#e9f4ef;--chip:#20352c;--chip-fg:#8fd3b4;--bar:#5cc39a;--track:#25302b;--ok:#5cc39a;--open:#e98a6c;--open-soft:#3a241d;color-scheme:dark}}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:14px;line-height:1.45;padding-block:20px 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.rep{max-width:1000px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.head{background:var(--head);color:var(--head-fg);padding:18px 22px;display:flex;flex-wrap:wrap;gap:10px 20px;justify-content:space-between;align-items:flex-end}
.eyebrow{font-size:11px;letter-spacing:.09em;text-transform:uppercase;opacity:.75}
h1{margin:2px 0 0;font-size:22px;line-height:1.2;text-wrap:balance}
.filters{display:flex;flex-wrap:wrap;gap:6px}
.filters span{font-size:12px;padding:3px 10px;border-radius:999px;background:rgba(255,255,255,.14)}
.filters span.f{background:var(--head-fg);color:var(--head);font-weight:600}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;padding:12px 22px 6px}
.tile{border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.tile .v{font-size:30px;font-weight:650;font-variant-numeric:tabular-nums;line-height:1.1}
.tile .of{font-size:15px;font-weight:500;color:var(--muted)}
.scope{padding:18px 22px 4px;display:flex;flex-direction:column;gap:8px}
.sv{font-size:16px}.sv b{font-size:20px;font-variant-numeric:tabular-nums}
.pct{margin-left:6px;font-size:13px;font-weight:600;padding:2px 8px;border-radius:999px;background:var(--chip);color:var(--chip-fg)}
.track.big{height:12px;border-radius:6px}
.sl{font-size:12px;color:var(--muted)}
.tile .l{font-size:12px;color:var(--muted);margin-top:2px}
.tile.warn .v{color:var(--open)} .tile.good .v{color:var(--ok)}
.breakdowns{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px 26px;padding:14px 22px 18px}
.brk h3{margin:0 0 8px;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:600}
.bar{display:grid;grid-template-columns:minmax(80px,auto) 1fr auto;gap:8px;align-items:center;font-size:13px;margin-bottom:5px}
.bl{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.track{height:8px;background:var(--track);border-radius:4px;overflow:hidden}
.fill{display:block;height:100%;background:var(--bar);border-radius:4px}
.bv{text-align:right;white-space:nowrap;font-size:12px;font-variant-numeric:tabular-nums;color:var(--muted)}
.tbl{border-top:1px solid var(--line);overflow-x:auto}
table{border-collapse:collapse;width:100%;min-width:960px;font-size:13px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:600;position:sticky;top:0;background:var(--card)}
th:first-child,td:first-child{padding-left:22px}
td.nm{font-weight:600}
td.note{min-width:220px;max-width:300px;color:var(--fg)}
td.note .by{display:block;font-family:var(--mono);font-size:11px;color:var(--muted);margin-top:2px}
td.when{font-family:var(--mono);font-size:12px;color:var(--muted);white-space:nowrap}
td.c{text-align:center}
.chips{display:flex;flex-wrap:wrap;gap:4px;margin:0;padding:0;list-style:none}
.chips li{font-size:12px;padding:1px 7px;border-radius:5px;background:var(--chip);color:var(--chip-fg);white-space:nowrap}
.chips li.kpi{background:transparent;border:1px solid var(--chip-fg)}
.ok{color:var(--ok);font-weight:700}
.open{font-size:11px;font-weight:600;padding:1px 7px;border-radius:5px;background:var(--open-soft);color:var(--open)}
.foot{padding:10px 22px;font-size:12px;color:var(--muted);display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px}
.note{max-width:1000px;margin:12px auto 0;font-size:12px;color:var(--muted)}
.bar[data-col],.tile[data-col]{cursor:pointer;border-radius:6px}
.bar[data-col]:hover .bl,.bar.is-on .bl{color:var(--chip-fg);font-weight:600}
.bar.is-on .fill{background:var(--chip-fg)}
.tile[data-col]:hover{border-color:var(--chip-fg)}
.tile.is-on{border-color:var(--chip-fg);box-shadow:inset 0 0 0 1px var(--chip-fg)}
[data-col]:focus-visible,th.sort:focus-visible,.fbar button:focus-visible{outline:2px solid var(--chip-fg);outline-offset:2px}
.hint{font-size:12px;color:var(--muted);padding:0 22px 12px}
.fbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px 22px;border-top:1px solid var(--line);background:var(--chip);color:var(--chip-fg);font-size:13px}
.fbar[hidden],tbody tr[hidden]{display:none}
.fbar button{font:inherit;font-size:12px;padding:3px 10px;border-radius:999px;border:1px solid var(--chip-fg);background:transparent;color:var(--chip-fg);cursor:pointer}
th.sort{cursor:pointer;user-select:none}
th.sort::after{content:" ↕";opacity:.4}
th[aria-sort="ascending"]::after{content:" ↑";opacity:1}
th[aria-sort="descending"]::after{content:" ↓";opacity:1}
</style>
<div class="rep">
  <div class="head">
    <div><div class="eyebrow">Report · live view</div><h1>{{title}}</h1></div>
    <div class="filters"><!-- One span per filter chip, see the fill rules. --><span>{{fixed chip}}</span><!-- repeat: one span class="f" per filter --><span class="f">{{filter chip}}</span></div>
  </div>
  <div class="scope">
    <div class="sv"><b>{{matches}}</b> of <b>{{in scope}}</b> clients in scope <span class="pct">{{percent}}%</span></div>
    <div class="track big"><span class="fill" style="width:{{percent}}%"></span></div>
    <div class="sl">In scope: {{what in scope means for this report}}. The other {{in scope minus matches}} aren't {{filter}}.</div>
  </div>
  <div class="tiles">
    <div class="tile"><div class="v">{{matches}}<span class="of"> / {{in scope}}</span></div><div class="l">{{filter}} · {{percent}}% of in scope</div></div>
    <div class="tile good"><div class="v">{{complete count}}<span class="of"> / {{matches}}</span></div><div class="l">Set As Complete · {{percent}}%</div></div>
    <div class="tile warn"><div class="v">{{open count}}<span class="of"> / {{matches}}</span></div><div class="l">Still open · {{percent}}%</div></div>
    <div class="tile"><div class="v">{{not matching count}}<span class="of"> / {{in scope}}</span></div><div class="l">Not at {{filter}} · {{percent}}% of in scope</div></div>
  </div>
  <div class="breakdowns">
    <div class="brk"><h3>By practitioner · matches / their in-scope clients</h3><!-- One .bar per practitioner, largest first. width = matches / group in scope. --><div class="bar"><span class="bl">{{practitioner name}}</span><span class="track"><span class="fill" style="width:{{width}}%"></span></span><span class="bv">{{matches}} / {{group in scope}} · {{percent}}%</span></div></div>
    <div class="brk"><h3>By office · matches / in scope</h3><!-- One .bar per office, largest first. --><div class="bar"><span class="bl">{{office name}}</span><span class="track"><span class="fill" style="width:{{width}}%"></span></span><span class="bv">{{matches}} / {{group in scope}} · {{percent}}%</span></div></div>
    <div class="brk"><h3>By client type · matches / in scope</h3><!-- One .bar per client type, largest first, top 5 only. --><div class="bar"><span class="bl">{{client type}}</span><span class="track"><span class="fill" style="width:{{width}}%"></span></span><span class="bv">{{matches}} / {{group in scope}} · {{percent}}%</span></div></div>
  </div>
  <div class="hint">Tap a bar or tile to filter the table · tap a column heading to sort</div>
  <div class="fbar" hidden><span class="fl"></span><button type="button">Clear filters</button></div>
  <div class="tbl"><table>
    <thead><tr><th>Client</th><th>Client type</th><th>Practitioner</th><th>Office</th><th>Ticked</th><th>Last set by</th><th>Latest note</th><th>Complete</th></tr></thead>
    <tbody>
      <!-- One <tr> per matching client, sorted by name. -->
      <tr><td class="nm">{{client name}}</td><td>{{client type}}</td><td>{{practitioner name}}</td><td>{{office name}}</td><td><ul class="chips"><!-- One <li> per ticked Status option; <li class="kpi"> per ticked KPI option. --><li>{{status}}</li></ul></td><td class="when">{{user}} · {{mm/dd hh:mm}}</td><td class="note">{{latest note text, or –}}<span class="by">{{note user}} · {{mm/dd}}</span></td><td class="c">{{<span class="ok">✓</span>|<span class="open">Open</span>}}</td></tr>
    </tbody>
  </table></div>
  <div class="foot"><span>Not saved · say "save this report" to keep a copy in outputs/reports</span><span>Pulled {{yyyy-mm-dd hh:mm}} for {{user name}}</span></div>
</div>
<script>
(function(){
  var rep=document.querySelector('.rep'); if(!rep) return;
  var tb=rep.querySelector('tbody');
  var rows=[].slice.call(tb.querySelectorAll('tr')).filter(function(r){return r.children.length>=8;});
  var bar=rep.querySelector('.fbar'), lab=bar.querySelector('.fl');
  var f={}, dir={};
  function txt(el){return el?(el.textContent||'').trim():'';}
  function isDone(r){return txt(r.children[7]).indexOf('✓')>-1;}
  function apply(){
    var shown=0;
    rows.forEach(function(r){
      var ok=true;
      Object.keys(f).forEach(function(k){
        if(k==='7') ok=ok&&((f[k]==='done')===isDone(r));
        else ok=ok&&txt(r.children[+k])===f[k];
      });
      r.hidden=!ok; if(ok) shown++;
    });
    var keys=Object.keys(f);
    bar.hidden=!keys.length;
    lab.textContent='Showing '+keys.map(function(k){return k==='7'?(f[k]==='done'?'Set As Complete':'Still open'):f[k];}).join(' + ')+': '+shown+' of '+rows.length;
    [].forEach.call(rep.querySelectorAll('[data-col]'),function(el){el.classList.toggle('is-on',f[el.getAttribute('data-col')]===el.getAttribute('data-val'));});
  }
  function toggle(el){var c=el.getAttribute('data-col'),v=el.getAttribute('data-val'); if(f[c]===v) delete f[c]; else f[c]=v; apply();}
  function clickable(el,fn){
    el.tabIndex=0; el.setAttribute('role','button');
    el.addEventListener('click',fn);
    el.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();fn();}});
  }
  var colOf={practitioner:'2',office:'3','client type':'1'};
  [].forEach.call(rep.querySelectorAll('.brk'),function(b){
    var h=txt(b.querySelector('h3')).toLowerCase().replace(/^by\s+/,'').split('\u00b7')[0].trim();
    var col=colOf[h]; if(!col) return;
    [].forEach.call(b.querySelectorAll('.bar'),function(x){x.setAttribute('data-col',col);x.setAttribute('data-val',txt(x.querySelector('.bl')));});
  });
  var t=rep.querySelectorAll('.tile');
  if(t[1]){t[1].setAttribute('data-col','7');t[1].setAttribute('data-val','done');}
  if(t[2]){t[2].setAttribute('data-col','7');t[2].setAttribute('data-val','open');}
  [].forEach.call(rep.querySelectorAll('[data-col]'),function(el){clickable(el,function(){toggle(el);});});
  bar.querySelector('button').addEventListener('click',function(){f={};apply();});
  function key(r,i){
    var v=txt(r.children[i]);
    if(i===5) return (v.split('·')[1]||'').trim();
    if(i===7) return isDone(r)?'1':'0';
    return v.toLowerCase();
  }
  var ths=rep.querySelectorAll('thead th');
  [].forEach.call(ths,function(th,i){
    if(i===4) return;
    th.classList.add('sort');
    clickable(th,function(){
      dir[i]=dir[i]===1?-1:1;
      rows.sort(function(a,b){var x=key(a,i),y=key(b,i);return x<y?-dir[i]:x>y?dir[i]:0;});
      rows.forEach(function(r){tb.appendChild(r);});
      [].forEach.call(ths,function(h,j){h.setAttribute('aria-sort',j===i?(dir[i]===1?'ascending':'descending'):'none');});
    });
  });
})();
</script>
```
