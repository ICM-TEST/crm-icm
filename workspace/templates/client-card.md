# Client card

The card shown in the chat when someone asks to see a client. It is never saved to the Drive. How to fill and show it: [../skills/client-card.md](../skills/client-card.md).

## Fill rules

- Copy the HTML below exactly. Change only the `{{...}}` placeholders. Never change the styles, the layout, the order or the labels: every card looks the same.
- The HTML is the artifact's whole content, titled `<Client Name>`.
- `{{a|b}}`: write the one that applies, for example `active` or `inactive`.
- Every number is shown in full, as on the Profile.
- A blank field shows `–`.
- Practitioner and office show the name only (from the slot's bracketed name). Statuses show the option with the slot replaced by its name, for example `Prep In Progress – <Name>`.
- Work pages: one `.page` block per page, in this order: Income Tax, Provisional Tax, Admin Penalty, FICA, Tax Clearance.
  - The year or period is the latest one that has an entry. Provisional periods compare by year, then 1st before 2nd.
  - One `<li>` per ticked Status box option. One `<li class="kpi">` per ticked KPI box option. Leave the `<ul>` out if nothing is ticked, and write `<span class="none">Nothing ticked</span>` instead.
  - The `complete` line appears only if Set As Complete is ticked.
  - A page with no entry yet: year `–` and `<span class="none">Nothing yet</span>`.
  - A client with no Provisional Tax folder: leave that block in, add class `off` (`<div class="page off">`), year `–`, and `<span class="none">Not provisional</span>`.
- The foot shows the date and time the card was made and the user name from the Project instruction.

## HTML

```html
<style>
:root{--bg:#eef1ef;--card:#ffffff;--fg:#1b2420;--muted:#62706a;--line:#dde3e0;--head:#173f33;--head-fg:#f1f7f4;--chip:#e4efe9;--chip-fg:#1d5c46;--on:#1f7a55;--off:#a1462b;--off-soft:#f6e5de;--done:#1f7a55;
--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#111614;--card:#1a211e;--fg:#e4ebe7;--muted:#9eaba5;--line:#2d3632;--head:#0f2c23;--head-fg:#e9f4ef;--chip:#20352c;--chip-fg:#8fd3b4;--on:#5cc39a;--off:#e98a6c;--off-soft:#3a241d;--done:#5cc39a;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#111614;--card:#1a211e;--fg:#e4ebe7;--muted:#9eaba5;--line:#2d3632;--head:#0f2c23;--head-fg:#e9f4ef;--chip:#20352c;--chip-fg:#8fd3b4;--on:#5cc39a;--off:#e98a6c;--off-soft:#3a241d;--done:#5cc39a;color-scheme:dark}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:14px;line-height:1.45;padding:20px max(16px,env(safe-area-inset-left,0px))}
.card{max-width:760px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.head{background:var(--head);color:var(--head-fg);padding:20px 22px;display:flex;flex-wrap:wrap;gap:12px 20px;align-items:flex-end;justify-content:space-between}
.head h1{margin:0;font-size:24px;line-height:1.15;letter-spacing:-.01em}
.head .sub{margin-top:4px;font-size:13px;opacity:.8}
.pills{display:flex;flex-wrap:wrap;gap:6px}
.pill{font-size:12px;font-weight:600;padding:3px 10px;border-radius:999px;background:rgba(255,255,255,.14);color:var(--head-fg)}
.pill.active::before{content:"● ";color:#7fe0b4}
.pill.inactive::before{content:"● ";color:#f0a58c}
.body{padding:18px 22px 22px;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px 26px}
.group h2{margin:0 0 8px;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:600}
dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:5px 12px}
dt{color:var(--muted);white-space:nowrap}
dd{margin:0;min-width:0;overflow-wrap:anywhere}
.num{font-family:var(--mono);font-size:13px;font-variant-numeric:tabular-nums}
.yes{color:var(--on);font-weight:600}.no{color:var(--muted)}
.wide{grid-column:1/-1}
.notes{margin:0;padding:10px 12px;background:var(--bg);border-radius:8px;white-space:pre-wrap}
.pages{border-top:1px solid var(--line);padding:16px 22px 22px}
.pages > h2{margin:0 0 10px;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}
.page{border:1px solid var(--line);border-radius:10px;padding:10px 12px;display:flex;flex-direction:column;gap:6px;min-width:0}
.page .t{display:flex;justify-content:space-between;gap:8px;align-items:baseline}
.page b{font-size:14px}
.page .yr{font-family:var(--mono);font-size:12px;color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:4px;margin:0;padding:0;list-style:none}
.chips li{font-size:12px;padding:2px 8px;border-radius:5px;background:var(--chip);color:var(--chip-fg)}
.chips li.kpi{background:transparent;border:1px solid var(--chip-fg)}
.page .none{font-size:12px;color:var(--muted)}
.complete{font-size:12px;font-weight:600;color:var(--done)}
.page.off{opacity:.55}
.foot{border-top:1px solid var(--line);padding:10px 22px;font-size:12px;color:var(--muted);display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px}
</style>
<div class="card">
  <div class="head">
    <div>
      <h1>{{Name}}</h1>
      <div class="sub">{{Client type}}</div>
    </div>
    <div class="pills">
      <span class="pill {{active|inactive}}">{{Active|Inactive}}</span>
      <span class="pill">{{Existing|New}}</span>
      <span class="pill">{{English|Afrikaans}}</span>
    </div>
  </div>
  <div class="body">
    <div class="group">
      <h2>Contact</h2>
      <dl>
        <dt>Phone</dt><dd class="num">{{Contact number}}</dd>
        <dt>Other numbers</dt><dd class="num">{{Additional numbers, comma separated, or –}}</dd>
        <dt>Email</dt><dd>{{Email}}</dd>
        <dt>Other emails</dt><dd>{{Additional emails, or –}}</dd>
        <dt>Postal</dt><dd>{{Postal address}}</dd>
        <dt>Physical</dt><dd>{{Physical address}}</dd>
      </dl>
    </div>
    <div class="group">
      <h2>Identity and tax</h2>
      <dl>
        <dt>Marital status</dt><dd>{{Marital status}}</dd>
        <dt>Tax number</dt><dd class="num">{{Income tax number}}</dd>
        <dt>ID number</dt><dd class="num">{{ID number, or –}}</dd>
        <dt>Passport</dt><dd class="num">{{Passport number, or –}}</dd>
        <dt>Income tax</dt><dd class="yes">Yes</dd>
        <dt>Provisional</dt><dd class="{{yes|no}}">{{Yes|No}}</dd>
        <dt>Rental income</dt><dd class="{{yes|no}}">{{Yes|No}}</dd>
      </dl>
    </div>
    <div class="group">
      <h2>Bank</h2>
      <dl>
        <dt>Bank</dt><dd>{{Bank}}</dd>
        <dt>Holder</dt><dd>{{Account holder}}</dd>
        <dt>Account</dt><dd class="num">{{Account number}}</dd>
        <dt>Branch</dt><dd class="num">{{Branch code}}</dd>
        <dt>Type</dt><dd>{{Account type}}</dd>
      </dl>
    </div>
    <div class="group">
      <h2>Practice</h2>
      <dl>
        <dt>Client type</dt><dd>{{Client type}}</dd>
        <dt>Practitioner</dt><dd>{{Practitioner name}}</dd>
        <dt>Office</dt><dd>{{Office name}}</dd>
        <dt>Balance due</dt><dd class="num">{{Balance due, or –}}</dd>
      </dl>
    </div>
    <div class="group wide">
      <h2>Notes</h2>
      <p class="notes">{{Notes, or –}}</p>
    </div>
  </div>
  <div class="pages">
    <h2>Work pages · latest year or period</h2>
    <div class="grid">
      <!-- One .page block per page, in this order: Income Tax, Provisional Tax, Admin Penalty, FICA, Tax Clearance. -->
      <div class="page">
        <div class="t"><b>{{Page}}</b><span class="yr">{{latest year or period}}</span></div>
        <ul class="chips"><li>{{ticked status}}</li><li class="kpi">{{ticked KPI status}}</li></ul>
        <span class="complete">✓ Set As Complete</span>
      </div>
    </div>
  </div>
  <div class="foot"><span>Client card · read only</span><span>Shown {{yyyy-mm-dd hh:mm}} for {{user name}}</span></div>
</div>
```
