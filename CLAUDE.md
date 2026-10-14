# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal investment research project tracking a **silver (precious metal) investment thesis** built around a "Nine Driver Framework" (documented in `references/Silver Nine Driver Framework August 2026.pdf`). The primary artefact is a single self-contained HTML dashboard file.

## Files

- `silver-thesis-key-milestones.html` — the full research dashboard; no build step, open directly in a browser
- `references/Silver Nine Driver Framework August 2026.pdf` — the underlying framework document this dashboard tracks

## The Nine Driver Framework

The thesis holds that silver is in a structural multi-year bull market driven by nine simultaneous demand/supply/monetary forces. The framework document is updated periodically; the timeline dashboard tracks events as they confirm, project, or stress-test each driver. **Exit discipline: hold to 2034 or $300/oz.**

| # | Driver | Status (as of Oct 13, 2026) | Dashboard categories |
|---|---|---|---|
| 1 | COMEX Registered & Eligible Drain | Active — ~101.4 moz registered (Oct 2 CF; Oct 13 carry-forward); above 100 moz warn threshold; Reg/Eligible ~0.43x; Reg/OI ~0.19x; eligible ~236.2 moz | `price`, `macro` |
| 2 | SHFE Critically Low Deliverable Stocks | Active — 1,407t (45.3 moz, Sep 11 confirmed; carried forward Oct 13); well below pre-2026 norms; backwardation −8¢ spot–3M (12+ months sustained) | `price`, `macro` |
| 3 | RBI Silver Collateral Monetisation Policy | Operative since 1 Apr 2026; IIBX ~90t/month (Aug confirmed; Sep/Oct CF); duty still 15%; India FX reserves $734.6bn (week ended Oct 2; published Oct 9 RBI WSS; cumulative $51bn decline from Sep 12 record); USD/INR ~96.2 (Oct 13 est.) | `india`, `duty` |
| 4 | ALMM-2 Solar Module Mandate | Operative since 1 Jun 2026; 9th revision Aug 21 adds TOPCon (Avaada); 28+ GW approved domestic cell capacity; TOPCon uses ~15% more silver/watt than PERC | `almm` |
| 5 | Chinese VAT Rebate Removal on PV Exports | Operative since 1 Apr 2026; front-loading complete; export cost headwind structural | `macro` |
| 6 | Mexican Supply Frictions | Ongoing cartel disruption; no new supply response | `macro` |
| 7 | SEBI ETF/MF Valuation Circulars | Operative since 1 Apr 2026; MCX Silver ~₹221,000/kg (Oct 8 est.; Oct 13 CF); USD/INR ~96.2 (Oct 13 est.) | `india` |
| 8 | Geopolitical Risk Premium (Hormuz) | **Partially easing** — WTI ~$91 (Oct 13 CF); oil still above $90, structurally inflationary; US-Iran phased deal contacts ongoing; India FX reserves $734.6bn (down $12.95bn week ended Oct 2) — cumulative $51bn reserve burn from Sep 12 record | `macro`, `catalyst` |
| 9 | Stagflation / Monetary-System Stress | **Most active** — Sep 17 FOMC +25bps to 4.00%; UST 30Y ~5.60%, UST 10Y ~5.24% (H.15 Oct 9), JGB 10Y ~3.11% (CF, 30-year high); RFI 0.53 (approaching 0.55 alarm); Sep payrolls +29k miss; **Sep CPI +3.7% y/y, core +2.6% (Oct 14 BLS — above consensus)** — hike probability Oct 27–28 now ~45–50%; **Oct 8 30Y auction solid** (2.54× B/C, 6.8% dealer absorption — not the alarm scenario); next FOMC Oct 27–28 | `fed`, `boj`, `credit`, `macro`, `cb` |

**Driver 9 sub-threads:**
- **9a** Fed policy — Sep 16–17 FOMC: +25bps unanimous hike to 4.00% (first hike since 2023); Warsh cited PCE 3.7%, CPI 3.4%, oil shock; dot-plot median = one more hike this year → ~4.25%; Sep payrolls +29k miss (Oct 2) reduced Oct hike probability from ~60% to ~35%; Sep CPI +3.7% y/y (Oct 14 BLS) has pushed hike probability back toward ~45–50%; next FOMC Oct 27–28
- **9b** Treasury buyback — confirmed active Sep 9; $4B+ per operation 10–30yr sector through Nov 4; structural fiscal-vs-monetary tension; Oct 8 30Y auction COMPLETED (solid — 5.618% yield, 2.54× B/C, 6.8% dealer absorption)
- **9c** Auction demand — Sep 9 10Y: B/C 2.71x; Oct 8 30Y: B/C 2.54× (solid; indirect 72.3% vs 69.1% avg; dealer absorption 6.8%); UST 30Y ~5.60%, 10Y ~5.24% (H.15 Oct 9); RFI 0.53; next test Nov quarterly refunding
- **9d** Buyer-base shift — official foreign holders down from ~40% to ~12% of outstanding Treasuries; gap filled by price-sensitive private capital; structural fragility
- **9e** Debt-service math — net interest $1.0T (3.3% GDP) FY2026, rising to $2.1T by 2036; interest exceeds Medicare from FY2028; debt/GDP 101% → 120% by 2036
- **9f** Fiscal off-ramps all constrained — tax hikes growth-negative, DOGE reversed by reconciliation act (+$4.7T to CBO deficit), mandatory spending untouchable
- **9g** Reserve diversification — CB gold buying ~1,200t in 2025, 244t Q1 2026, 289t Q2 2026 (record quarter); WGC: gold overtakes Treasuries as largest global reserve asset (27% vs 22%); G/S ratio ~69× (Oct 13 est., slight expansion as gold outperforms on hot CPI)

**COT positioning watch:** Managed money net long ~8,000 contracts (est. Oct 6 week CFTC, published Oct 11; partial recovery from 7,614 Sep 29 capitulation low; non-commercial net confirmed +1,070 to 23,153 for week ended Oct 6). Down ~80% from Sep 9 peak of 37.8k. Still approaching <5k full-capitulation threshold. Short-side crowded = violent short-covering risk on positive catalyst. Next CFTC report (week ended Oct 10) due Oct 16.

**Key price levels (as of Oct 13, 2026):** Silver COMEX ~$60.5 (est. Oct 13; $60.7 Oct 2 → $61.2 Sep 29 → $60.7 Oct 2 → ~$60.5 Oct 13); Gold ~$4,175 (est.); G/S ratio ~69×. July low $55 → Aug 27 high ~$70 → post-FOMC support ~$60. Structural support ~$60 (monthly close below = thesis review). Sep CPI +3.7% y/y (Oct 14) may test $60 support intraday as FOMC hike expectations rise.

**India import mechanics:** Duty 15% since May 13, 2026 (up from 6%). IIBX ~90t/month (Aug confirmed; Sep/Oct CF); MCX Silver ~₹221,000/kg (Oct 8 est.); USD/INR ~96.2 (Oct 13 est.). India FX reserves $734.6bn (week ended Oct 2, published Oct 9 RBI WSS; cumulative $51bn decline from Sep 12 record of $785.7bn) — duty reversal is a political choice. A duty cut to 6% would trigger ~500–800t immediate import surge.

**Forward milestones to watch:** ALMM List II net-metering/open-access exemption expires **Dec 31 2026** — if MNRE holds, all Indian solar project categories lock into domestic (silver-intensive) cells. **Oct 27–28 FOMC** — follow-on hike decision; Sep CPI +3.7% (Oct 14) has pushed hike probability to ~45–50%; next NFP ~Nov 6. **Oct 16** — CFTC COT for week ended Oct 10 (first post-CPI positioning read). **Oct 31** — Core PCE (critical for FOMC hike final decision).

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
