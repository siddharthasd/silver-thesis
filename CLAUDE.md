# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal investment research project tracking a **silver (precious metal) investment thesis** built around a "Nine Driver Framework" (documented in `references/Silver Nine Driver Framework August 2026.pdf`). The primary artefact is a single self-contained HTML dashboard file.

## Files

- `silver-thesis-key-milestones.html` — the full research dashboard; no build step, open directly in a browser
- `references/Silver Nine Driver Framework August 2026.pdf` — the underlying framework document this dashboard tracks

## The Nine Driver Framework

The thesis holds that silver is in a structural multi-year bull market driven by nine simultaneous demand/supply/monetary forces. The framework document is updated periodically; the timeline dashboard tracks events as they confirm, project, or stress-test each driver. **Exit discipline: hold to 2034 or $300/oz.**

| # | Driver | Status (as of Oct 29, 2026) | Dashboard categories |
|---|--------|------------------------------|---------------------|
| 1 | COMEX Registered & Eligible Drain | Active — ~101.4 moz registered (Oct 2 CF; carried forward, no newer CME print); above 100 moz warn threshold; Reg/Eligible ~0.43x; Reg/OI ~0.18x (OI ~114k, CFTC Oct 20); eligible ~236.2 moz | `price`, `macro` |
| 2 | SHFE Critically Low Deliverable Stocks | Active — 1,407t (45.3 moz, Sep 11 confirmed; carried forward Oct 29); well below pre-2026 norms; backwardation −8¢ spot–3M (12+ months sustained) | `price`, `macro` |
| 3 | RBI Silver Collateral Monetisation Policy | Operative since 1 Apr 2026; IIBX ~90t/month (Aug confirmed; Sep/Oct CF); duty still 15%; DGFT eased licensing Oct 9/13 (fast-track route from Oct 15; ~6,500t permits over six months per Reuters Oct 22); India FX reserves $721.0bn (week ended Oct 16 — sixth straight fall, ~$65bn below the Sep 4 record of $785.7bn); USD/INR ~95 (CF) | `india`, `duty` |
| 4 | ALMM-2 Solar Module Mandate | Operative since 1 Jun 2026; 12th revision ~Oct 8 (Gopin Semicon +402 MW TOPCon); ~37.4–37.8 GW approved domestic cell capacity; net-metering exemption expires Dec 31 2026 | `almm` |
| 5 | Chinese VAT Rebate Removal on PV Exports | Operative since 1 Apr 2026; front-loading complete; export cost headwind structural | `macro` |
| 6 | Mexican Supply Frictions | Ongoing cartel disruption; no new supply response | `macro` |
| 7 | SEBI ETF/MF Valuation Circulars | Operative since 1 Apr 2026; MCX Silver ~₹188,000/kg (Oct 29 est., silver ~$52); USD/INR ~95 (CF) | `india` |
| 8 | Geopolitical Risk Premium (Hormuz) | **Re-escalated** — WTI ~$101 (Dec, Oct 29); Brent ~$114; Houthi attacks on Saudi infrastructure (Oct 22); silver reaction negative (oil lifts rate/dollar expectations, no safe-haven bid) | `macro`, `catalyst` |
| 9 | Stagflation / Monetary-System Stress | **Most active** — Oct 28 FOMC held at 3.75–4.00% (10–2; Cook and Hammack dissented for a hike), December hike ~80–85% priced; UST 10Y 5.00%, 30Y ~5.33% (Oct 29, H.15 pending), JGB 10Y ~2.84% (BOJ held 1.25% Oct 30); RFI 0.46 (alarm 0.55); Sep CPI +3.7% y/y, Sep core PCE 3.1% y/y, Q3 GDP +3.4% (Oct 29); next FOMC Dec 9 | `fed`, `boj`, `credit`, `macro`, `cb` |

**Driver 9 sub-threads:**
- **9a** Fed policy — Sep 16–17 FOMC: +25bps unanimous hike to 4.00% (first hike since 2023). **Oct 28 FOMC: hold at 3.75–4.00%, 10–2** (Cook and Hammack dissented for a hike); statement upgraded activity to "strong"; December hike priced ~80–85%; next FOMC Dec 9 (no FOMC in November); next NFP Nov 6, Oct CPI Nov 10
- **9b** Treasury buyback — confirmed active Sep 9; $4B+ per operation 10–30yr sector through Nov 4; structural fiscal-vs-monetary tension; Oct 8 30Y auction COMPLETED (solid — 5.618% yield, 2.54× B/C, 6.8% dealer absorption)
- **9c** Auction demand — Sep 9 10Y: B/C 2.71x; Oct 8 30Y: B/C 2.54× (solid); UST 10Y 5.00%, 30Y ~5.33% (Oct 29); RFI 0.46; next test Nov quarterly refunding (announcement ~Nov 4)
- **9d** Buyer-base shift — official foreign holders down from ~40% to ~12% of outstanding Treasuries; gap filled by price-sensitive private capital; structural fragility
- **9e** Debt-service math — net interest $1.0T (3.3% GDP) FY2026, rising to $2.1T by 2036; interest exceeds Medicare from FY2028; debt/GDP 101% → 120% by 2036
- **9f** Fiscal off-ramps all constrained — tax hikes growth-negative, DOGE reversed by reconciliation act (+$4.7T to CBO deficit), mandatory spending untouchable
- **9g** Reserve diversification — CB gold buying ~1,200t in 2025; WGC (Q2 2026 report) **revised Q1 2026 to +57t from 244t**; Q2 2026 +289t (record Q2); PBoC +21t in September (23rd straight month, 2,196t); WGC: gold overtakes Treasuries as largest global reserve asset (27% vs 22%); G/S ratio ~78× (Oct 29 est., widening as silver underperforms)

**COT positioning watch:** Managed money net long ~8,000 contracts (carried forward; last CFTC-confirmed 7,614 Sep 29 capitulation low). CFTC non-commercial net long **19,795** for week ended Oct 20 (from 22,631 Oct 13); non-commercial shorts +26% to 14,780; OI 113,992; net longs ~17.4% of OI (7th percentile of 60 weeks). Short-side building into the price break = violent short-covering risk on a positive catalyst. Next CFTC report (week ended Oct 27) due Oct 30.

**Key price levels (as of Oct 29, 2026):** Silver COMEX ~$52.0 (Dec, Oct 29 intraday/est. — new 2026 low; $61.2 Sep 29 → $60.7 Oct 2 → ~$60.5 Oct 13 → $55.01 Oct 22 → ~$52.0 Oct 29); Gold ~$4,033 (Dec, est.); G/S ratio ~78×. Supports $51.39 then $50; resistance $53.24, $54.5–55.8, $60–64. July low $55 broken; structural support ~$60 (monthly close below = thesis review) — **breached; Oct month-end close will land ~13% below the line.** WTI ~$101, DXY ~102.0.

**India import mechanics:** Duty 15% since May 13, 2026 (up from 6%). IIBX ~90t/month (Aug confirmed; Sep/Oct CF); MCX Silver ~₹188,000/kg (Oct 29 est.); USD/INR ~95 (CF; H.10 Oct 16: 94.96). India FX reserves $721.0bn (week ended Oct 16, published ~Oct 23; sixth straight weekly fall, −$65bn from the Sep record of $785.7bn) — duty reversal is a political choice. A duty cut to 6% would trigger ~500–800t immediate import surge. DGFT licensing easing (Oct 9/13) ahead of Dhanteras Nov 6 / Diwali Nov 8.

**Forward milestones to watch:** ALMM List II net-metering/open-access exemption expires **Dec 31 2026** — if MNRE holds, all Indian solar project categories lock into domestic (silver-intensive) cells. **Oct 30** — CFTC COT (week ended Oct 27); silver month-end close vs $60 structural support (breached). **Nov 3** — US midterms. **~Nov 4** — Treasury refunding announcement. **Nov 6** — Oct NFP; Dhanteras (Diwali Nov 8). **Nov 10** — Oct CPI. **Nov 18** — FOMC minutes. **Dec 9** — FOMC decision and projections (hike ~80–85% priced); BOJ December hike possible.

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
