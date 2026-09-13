# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal investment research project tracking a **silver (precious metal) investment thesis** built around a "Nine Driver Framework" (documented in `references/Silver Nine Driver Framework August 2026.pdf`). The primary artefact is a single self-contained HTML dashboard file.

## Files

- `silver-thesis-key-milestones.html` — the full research dashboard; no build step, open directly in a browser
- `references/Silver Nine Driver Framework August 2026.pdf` — the underlying framework document this dashboard tracks

## The Nine Driver Framework

The thesis holds that silver is in a structural multi-year bull market driven by nine simultaneous demand/supply/monetary forces. The framework document is updated periodically; the timeline dashboard tracks events as they confirm, project, or stress-test each driver. **Exit discipline: hold to 2034 or $300/oz.**

| # | Driver | Status (as of Sep 2026) | Dashboard categories |
|---|---|---|---|
| 1 | COMEX Registered & Eligible Drain | Active — ~86 Moz registered, historically tight | `price`, `macro` |
| 2 | SHFE Critically Low Deliverable Stocks | Active — ~868t, sustained backwardation | `price`, `macro` |
| 3 | RBI Silver Collateral Monetisation Policy | Operative since 1 Apr 2026; India import licensing bottleneck easing | `india`, `duty` |
| 4 | ALMM-2 Solar Module Mandate | Operative since 1 Jun 2026; locks in silver-intensive domestic cells | `almm` |
| 5 | Chinese VAT Rebate Removal on PV Exports | Operative since 1 Apr 2026; front-loading complete | `macro` |
| 6 | Mexican Supply Frictions | Ongoing cartel disruption; no new supply response | `macro` |
| 7 | SEBI ETF/MF Valuation Circulars | Operative since 1 Apr 2026; supports MCX domestic premium | `india` |
| 8 | Geopolitical Risk Premium (Hormuz) | Active but markets showing adaptation fatigue | `macro`, `catalyst` |
| 9 | Stagflation / Monetary-System Stress | Most active — see sub-threads 9a–9g below | `fed`, `boj`, `credit`, `macro`, `cb` |

**Driver 9 sub-threads:**
- **9a** Fed policy — Warsh hawkish (Jackson Hole, Aug 28): PCE 3.7%, financial conditions loose; no forward guidance; Sep hike ~60% probability post-speech
- **9b** Treasury buyback — doubled to $4B+ per operation for 10–30yr sector (Sep 9 – Nov 4); quasi-QE framing but no Fed balance sheet involvement; 30Y yield reversal showed it didn't resolve underlying demand weakness
- **9c** Auction demand deteriorating — bid-to-cover 2.39, primary dealers absorbing 11.5% (above 12-month avg), awarded yield above when-issued
- **9d** Buyer-base shift — official foreign holders down from ~40% to ~12% of outstanding Treasuries; gap filled by price-sensitive private capital; structural fragility
- **9e** Debt-service math — net interest $1.0T (3.3% GDP) FY2026, rising to $2.1T by 2036; interest exceeds Medicare from FY2028; debt/GDP 101% → 120% by 2036
- **9f** Fiscal off-ramps all constrained — tax hikes growth-negative, DOGE reversed by reconciliation act (+$4.7T to CBO deficit), mandatory spending untouchable
- **9g** Reserve diversification ≠ trade-settlement dominance — CB gold buying accelerating (~1,200t in 2025, 244t Q1 2026); trade invoicing still ~88% USD; mBridge only $55.5B cumulative; dollar erosion is gradual, not cliff-risk

**COT positioning watch:** Managed money net long ~14,073 (week of Aug 25) — well below the 40–50k+ caution threshold that would signal a crowded trade.

**Key price levels (as of early Sep 2026):** July low $55 → Aug 27 high ~$70 → post-Warsh support $65.50–66. Structural support ~$60 (close below would threaten recovery structure).

**India import mechanics:** Duty 15% since May 13, 2026 (up from 6%). Licensing via IIBX releasing slowly — ~90t August, domestic premium ~$4/oz (peak $6.30). A duty reversal to 6% would trigger an immediate ~500–800t import surge.

**Forward milestone to watch:** ALMM List II net-metering/open-access exemption expires **Dec 31 2026** — if MNRE holds, all Indian solar project categories lock into domestic (silver-intensive) cells.

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
