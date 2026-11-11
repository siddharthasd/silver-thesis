# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal investment research project tracking a **silver (precious metal) investment thesis** built around a "Nine Driver Framework" (documented in `references/Silver Nine Driver Framework August 2026.pdf`). The primary artefact is a single self-contained HTML dashboard file.

## Files

- `silver-thesis-key-milestones.html` — the full research dashboard; no build step, open directly in a browser
- `references/Silver Nine Driver Framework August 2026.pdf` — the underlying framework document this dashboard tracks

## The Nine Driver Framework

The thesis holds that silver is in a structural multi-year bull market driven by nine simultaneous demand/supply/monetary forces. The framework document is updated periodically; the timeline dashboard tracks events as they confirm, project, or stress-test each driver. **Exit discipline: hold to 2034 or $300/oz.**

| # | Driver | Status (as of Nov 10, 2026) | Dashboard categories |
|---|--------|------------------------------|---------------------|
| 1 | COMEX Registered & Eligible Drain | Active — 101.6 moz registered (Nov 9, goldsilver.ai/CME); just above 100 moz warn threshold; Reg/Eligible 0.44x; Reg/OI ~0.18x (OI 115,583, CFTC Nov 3); eligible 232.4 moz; flat for five weeks while silver fell | `price`, `macro` |
| 2 | SHFE Critically Low Deliverable Stocks | Active — 1,407t (45.3 moz, Sep 11 confirmed; carried forward Nov 10); well below pre-2026 norms; backwardation −8¢ spot–3M (12+ months sustained, CF) | `price`, `macro` |
| 3 | RBI Silver Collateral Monetisation Policy | Operative since 1 Apr 2026; IIBX ~90t/month (Aug confirmed; Sep–Nov CF); duty still 15% (no change found through Nov 11); DGFT eased licensing Oct 9/13; India FX reserves $721.0bn (week ended Oct 16, newer WSS not confirmed); USD/INR ~93.9 (H.10 Nov 6, firmer from ~95) | `india`, `duty` |
| 4 | ALMM-2 Solar Module Mandate | Operative since 1 Jun 2026; 12th revision ~Oct 8 (Gopin Semicon +402 MW TOPCon); ~37.4–37.8 GW approved domestic cell capacity; net-metering exemption expires Dec 31 2026 (no further extension reported as of Nov 11) | `almm` |
| 5 | Chinese VAT Rebate Removal on PV Exports | Operative since 1 Apr 2026; front-loading complete; export cost headwind structural | `macro` |
| 6 | Mexican Supply Frictions | Ongoing cartel disruption; no new supply response | `macro` |
| 7 | SEBI ETF/MF Valuation Circulars | Operative since 1 Apr 2026; MCX Silver ~₹187,000/kg (Nov 10 est., silver ~$52.4); USD/INR ~93.9 | `india` |
| 8 | Geopolitical Risk Premium (Hormuz) | **Easing** — oil reversed sharply: WTI ~$85, Brent ~$90 (lowest since August; was ~$101/$114 on Oct 29); cause not confirmed, so unwinding not resolved; silver did not benefit (rate/dollar legs dominate) | `macro`, `catalyst` |
| 9 | Stagflation / Monetary-System Stress | **Most active** — Oct payrolls +165k (Nov 6) and Oct CPI +0.4% m/m, core +0.3% (Nov 10) hot; Dec 9 hike ~fully priced (Fed funds 3.75–4.00% after Oct 28 hold, 10–2); UST 10Y 4.88%, 30Y 5.26%, 3Y 4.58% (H.15 Nov 9), TIPS 10Y 2.66%; JGB 10Y ~2.70% (BOJ held 1.25% Oct 30); RFI 0.44 (alarm 0.55); weak Nov 10 10Y auction (B/C 2.46); Oct CPI y/y not published (shutdown; Sep 3.7%); next FOMC Dec 9 | `fed`, `boj`, `credit`, `macro`, `cb` |

**Core pillar (added Nov 11 2026) — sustained & growing industrial deficit: IMPAIRED.** Previously assumed, not listed as a driver. Metals Focus (Oct 19 interview): 2026 deficit 35.4 Moz (WSS Apr: 46.3) turning to a theoretical **+37.3 Moz surplus in 2027**, industrial demand 618.2 Moz; Deutsche Bank (Oct 7): surplus as early as 2027, solar silver demand >20% lower in 2026, silver per cell −17%. Only 2027 is sourced; the Silver Demand Supply tab now carries 2027P–2030P projections (dashboard model: balance +37.3 / +38 / +45 / +50.5 Moz) plus scenarios A (deficit persists) / B (base) / C (accelerated substitution) and a critical evaluation (surplus is partly a fund-flow call; 2026 deficit may be overstated by ETF outflows; industrial sub-rows no longer sum to the total from 2024 — shown as an Unallocated row). **Scenario D (hard landing / depression, premise not forecast) added Nov 11 2026:** balance +163 / +205 / +138 / +84 Moz 2027P–2030P; cumulative 2021–26E deficit refilled by ~2029P. **Exit discipline rewritten:** hold to 2034 or $300/oz rule unchanged, but $300 is explicitly conditional on the monetary leg alone (needs gold ~$9,000–15,000 at gold/silver 30–50, or ~$23,100 at today’s ~77, plus fund inflows and silver outperforming gold). $60 monthly-close invalidation is breached and under review. Next: mid-Nov Metals Focus / Silver Institute interim review.

**Driver 9 sub-threads:**
- **9a** Fed policy — Sep 16–17 FOMC: +25bps unanimous hike to 4.00% (first hike since 2023). Oct 28 FOMC: hold at 3.75–4.00%, 10–2 (Cook and Hammack dissented for a hike). **Hot Oct NFP (+165k vs ~65k, unemployment 4.1%) and Oct CPI (+0.4%, core +0.3%) → Dec 9 hike ~fully priced** (~84% before CPI); no FOMC in November; next: PPI Nov 13, minutes Nov 18, Q3 GDP revision/Oct PCE Nov 25
- **9b** Treasury buyback — Nov 4 refunding kept auction sizes unchanged ($58B 3Y / $42B 10Y / $25B 30Y), raised buyback capacity to up to $70B liquidity + $25B cash management (vs $38B projected in Aug); 7Y moving to quarterly new issues; structural fiscal-vs-monetary tension
- **9c** Auction demand — Nov 10 10Y: 5.02%, B/C 2.46 (below ~2.54 avg), indirect 61.2% (lowest since Oct 2023; tail ~+1bp single-source); Oct 8 30Y B/C 2.54× (solid); next test Nov 12 30Y; RFI 0.44
- **9d** Buyer-base shift — official foreign holders down from ~40% to ~12% of outstanding Treasuries; gap filled by price-sensitive private capital; structural fragility
- **9e** Debt-service math — net interest $1.0T (3.3% GDP) FY2026, rising to $2.1T by 2036; CBO FY2026 deficit $2.0T (Nov 9); interest exceeds Medicare from FY2028; debt/GDP 101% → 120% by 2036
- **9f** Fiscal off-ramps all constrained — tax hikes growth-negative, DOGE reversed by reconciliation act (+$4.7T to CBO deficit), mandatory spending untouchable
- **9g** Reserve diversification — WGC Q3 2026: official-sector net buying **321t (+42% y/y; YTD 675t)**, only ~120t reported (China +63t, Poland +40t, Kazakhstan +14t, Uzbekistan +14t, Czech +5t; Russia −19t); Q2 2026 +289t; Q1 revised to +57t; PBoC +21t in September (23rd straight month); gold 2026 low $3,870 on Oct 30; G/S ratio ~77× (Nov 10, flat vs Oct 29)

**COT positioning watch:** Managed money net long ~8,000 contracts (carried forward; last CFTC-confirmed 7,614 Sep 29 capitulation low). CFTC non-commercial net long **21,251** for week ended Nov 3 (from 19,703 Oct 27); non-commercial longs 37,002, shorts 15,751; OI 115,583; net longs ~18.4% of OI. Net long rose while silver broke below $50 — no spec capitulation. Short-covering risk persists but both named catalysts (NFP, CPI) came in hot. Next CFTC report (week ended Nov 10) due Nov 13.

**Key price levels (as of Nov 10, 2026):** Silver COMEX ~$52.4 (Nov 10 est.; spot range $51.7–$53.0; traded below $50 around Oct 30–Nov 3; $61.2 Sep 29 → $55.01 Oct 22 → ~$52.0 Oct 29 → <$50 early Nov → ~$52 Nov 10); Gold ~$4,050 (est.; 2026 low $3,870 Oct 30); G/S ratio ~77×. Supports $51.27, $50; resistance $53.42, $54.64, $60–64; CPM sees $45–48 floor. Structural support ~$60 (monthly close below = thesis review) — **breached; Nov 10 spot ~13% below the line.** WTI ~$85, DXY ~102.3.

**India import mechanics:** Duty 15% since May 13, 2026 (up from 6%). IIBX ~90t/month (Aug confirmed; Sep–Nov CF); MCX Silver ~₹187,000/kg (Nov 10 est.); USD/INR ~93.9 (H.10 Nov 6). India FX reserves $721.0bn (week ended Oct 16; later WSS prints not confirmed) — duty reversal is a political choice; lower oil and a firmer rupee ease BOP pressure. A duty cut to 6% would trigger ~500–800t immediate import surge. Dhanteras Nov 6 / Diwali Nov 8 have passed; festival demand data not yet published.

**Forward milestones to watch:** ALMM List II net-metering/open-access exemption expires **Dec 31 2026** — if MNRE holds, all Indian solar project categories lock into domestic (silver-intensive) cells. **Nov 12** — 30Y auction. **Nov 13** — PPI; CFTC COT. **~Nov 15** — Q3 BDC 10-Qs (non-accruals). **Nov 18** — FOMC minutes. **Nov 25** — Q3 GDP revision / Oct PCE. **Nov 30** — month-end close vs $60 structural support. **Dec 9** — FOMC decision and projections (hike ~fully priced); BOJ December hike possible.

---

## Dashboard Architecture

The HTML file is a single-file app (~2,700 lines): all CSS, HTML, and JavaScript in one file. No external dependencies beyond system fonts.

### Tab structure

Three top-level tabs (`.page-tab-btn` / `.page-tab-panel`):

1. **Timeline** — month-by-month event timeline with filter pills
2. **India Policies** — tabbed policy cards covering import duties and ALMM (solar PV cell mandate)
3. **Central Bank Bullion Holdings** — collapsible tables of CB gold/silver data

A **Market Data Snapshot (MDS)** section sits above the timeline with collapsible tables tracking FX rates, precious metals prices, credit stress indicators, India-specific metrics, and private credit.

### Event system (Timeline tab)

Each event is a `<div class="event event--{category}">` block. Category classes drive the left-border colour and background:

| Class suffix | Badge label | Covers |
|---|---|---|
| `fed` | FOMC | Federal Reserve decisions |
| `boj` | BOJ / Carry | Bank of Japan / yen carry trade |
| `credit` | Credit | Credit market stress |
| `cb` | Central bank | Central bank gold purchases |
| `price` | Silver / gold | Price action and technicals |
| `india` | India / RBI | RBI and India macro events |
| `macro` | Macro | Global macro |
| `catalyst` | Catalyst | Bull/bear catalysts |
| `duty` | Import Duty | India customs duty changes |
| `almm` | ALMM | India solar PV cell mandate events |

Status pills inside each event title: `status-confirmed`, `status-projected`, `status-watch`.

Phase headers (`<div class="phase-header">`) divide the timeline into named phases (e.g., "Phase 1 — Accumulation window Aug 2026 – Feb 2027").

### JavaScript (inline, IIFE at bottom of `<body>`)

- `init()` — runs on DOMContentLoaded; calls `initCollapsers()`, `buildSparkbars()`, `buildCounts()`, then syncs filter pills
- `updateVisibility()` — hides/shows `.event` and `.month-block` elements based on `activeCategories` (Set) and `activeStatuses` (Set)
- `buildSparkbars()` — reads numeric cell text in MDS table rows and injects a proportional bar under each value
- Collapsible MDS sections and CB sections use `.collapsed` class toggled on the wrapper element
- FAB "jump to today" button scrolls to the `.month-label.current` element

### Adding new events

1. Find the correct `<div class="month-block">` for the target month (or add a new one in date order).
2. Copy an existing `<div class="event event--{category}">` block.
3. Set the badge class (`badge--{category}`), title text, status pill, detail text, and signal text.
4. Mark `completed` class on the event and dot when the event has occurred.

### Updating the MDS table

The MDS table is a standard HTML `<table>` inside `.mds-table`. Columns represent months; add a new `<th>` and the corresponding `<td>` in each data row. The `th-current` class highlights the current month column. Sparkbars are rebuilt automatically by `buildSparkbars()` on page load — no manual update needed.
