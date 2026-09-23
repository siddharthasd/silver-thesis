# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal investment research project tracking a **silver (precious metal) investment thesis** built around a "Nine Driver Framework" (documented in `references/Silver Nine Driver Framework August 2026.pdf`). The primary artefact is a single self-contained HTML dashboard file.

## Files

- `silver-thesis-key-milestones.html` — the full research dashboard; no build step, open directly in a browser
- `references/Silver Nine Driver Framework August 2026.pdf` — the underlying framework document this dashboard tracks

## The Nine Driver Framework

The thesis holds that silver is in a structural multi-year bull market driven by nine simultaneous demand/supply/monetary forces. The framework document is updated periodically; the timeline dashboard tracks events as they confirm, project, or stress-test each driver. **Exit discipline: hold to 2034 or $300/oz.**

| # | Driver | Status (as of Sep 22, 2026) | Dashboard categories |
|---|---|---|---|
| 1 | COMEX Registered & Eligible Drain | Active — ~97.9 moz registered (Sep 22, CME); below 100 moz warn threshold; Reg/Eligible ~0.42x; eligible ~232.9 moz | `price`, `macro` |
| 2 | SHFE Critically Low Deliverable Stocks | Active — 1,407t (45.3 moz, Sep 11 confirmed); recovered from near-alarm ~868t lows but well below pre-2026 norms; backwardation narrowed to −8¢ spot–3M post-FOMC hike (was −12¢; 12+ months of backwardation) | `price`, `macro` |
| 3 | RBI Silver Collateral Monetisation Policy | Operative since 1 Apr 2026; IIBX ~90t/month Aug; duty still 15%; India FX reserves record $785.7bn (Sep 12); USD/INR ~95.8 (Sep 22, rupee firmed slightly from Sep 17 post-hike low) | `india`, `duty` |
| 4 | ALMM-2 Solar Module Mandate | Operative since 1 Jun 2026; 9th revision Aug 21 adds TOPCon (Avaada); 28+ GW approved domestic cell capacity; TOPCon uses ~15% more silver/watt than PERC | `almm` |
| 5 | Chinese VAT Rebate Removal on PV Exports | Operative since 1 Apr 2026; front-loading complete; export cost headwind structural | `macro` |
| 6 | Mexican Supply Frictions | Ongoing cartel disruption; no new supply response | `macro` |
| 7 | SEBI ETF/MF Valuation Circulars | Operative since 1 Apr 2026; MCX Silver ~₹238,000/kg (Sep 22, recovered with COMEX); premium ~$1.6/oz over duty-adjusted parity | `india` |
| 8 | Geopolitical Risk Premium (Hormuz) | **Partially easing** — WTI ~$96 (Sep 22, down from $102 Sep 17 as Hormuz diplomatic contacts reported); oil still above $90, structurally inflationary; USD/INR ~95.8 (Sep 22) | `macro`, `catalyst` |
| 9 | Stagflation / Monetary-System Stress | **Most active — hike delivered** — Sep 17 FOMC +25bps unanimous; Fed Funds 4.00%; dot-plot signals one more to ~4.25%; see sub-threads | `fed`, `boj`, `credit`, `macro`, `cb` |

**Driver 9 sub-threads:**
- **9a** Fed policy — Sep 16–17 FOMC: +25bps unanimous hike to 4.00% (first hike since 2023); Warsh cited PCE 3.7%, CPI 3.4%, oil shock; dot-plot median = one more hike this year → ~4.25%; next FOMC Oct 27–28
- **9b** Treasury buyback — confirmed active Sep 9; $4B+ per operation 10–30yr sector through Nov 4; structural fiscal-vs-monetary tension; 30Y auction Oct 8 is the next real demand test
- **9c** Auction demand — Sep 9 10Y: B/C 2.71x (recovered from 2.39x prior); UST 10Y ~4.96%, 30Y ~5.30% (Sep 22, yields eased post-hike selloff); RFI 0.46; 30Y Oct 8 auction is the next test
- **9d** Buyer-base shift — official foreign holders down from ~40% to ~12% of outstanding Treasuries; gap filled by price-sensitive private capital; structural fragility
- **9e** Debt-service math — net interest $1.0T (3.3% GDP) FY2026, rising to $2.1T by 2036; interest exceeds Medicare from FY2028; debt/GDP 101% → 120% by 2036
- **9f** Fiscal off-ramps all constrained — tax hikes growth-negative, DOGE reversed by reconciliation act (+$4.7T to CBO deficit), mandatory spending untouchable
- **9g** Reserve diversification — CB gold buying ~1,200t in 2025, 244t Q1 2026, 289t Q2 2026 (record quarter); WGC: gold overtakes Treasuries as largest global reserve asset (27% vs 22%); G/S ratio ~67× (Sep 22, compressing as silver outperforms gold post-FOMC)

**COT positioning watch:** Managed money net long ~25k (est. Sep 22; Sep 9 confirmed 37.8k; post-FOMC hike liquidation reduced it) — well below the 40–50k+ caution threshold. Room for re-entry on dip-buying at $62.

**Key price levels (as of Sep 22, 2026):** Silver COMEX $65.3 (recovered from $62 post-FOMC low); Gold ~$4,380; G/S ratio ~67×. July low $55 → Aug 27 high ~$70 → post-hike support ~$60–62. Structural support ~$60 (monthly close below = thesis review).

**India import mechanics:** Duty 15% since May 13, 2026 (up from 6%). IIBX ~90t/month Aug; MCX Silver ~₹238,000/kg (Sep 22, recovered with COMEX); USD/INR ~95.8 (Sep 22, rupee firmed slightly from post-hike low). India FX reserves record $785.7bn (Sep 12) — removes BOP urgency for duty cut; reversal is a political choice. A duty cut to 6% would trigger ~500–800t immediate import surge.

**Forward milestone to watch:** ALMM List II net-metering/open-access exemption expires **Dec 31 2026** — if MNRE holds, all Indian solar project categories lock into domestic (silver-intensive) cells. **Oct 27–28 FOMC** — follow-on hike decision; dot-plot signals one more → ~4.25%.

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
