# Fund Fee Calculator
### Built by [Your Name] | Python · Financial Modelling · Fund Structures

---

## What This Project Is

This is an end-to-end, interactive fund fee calculator built from scratch in Python. It models the full economics of a private investment fund — management fees, performance/incentive fees, high-water mark mechanics, and clawback provisions — across multiple periods, with a clean period-by-period output table and a final performance summary including net IRR.

The project was built to demonstrate the intersection of **financial domain knowledge** and **practical programming** — not just knowing how fund fees work in theory, but being able to translate that knowledge into working, accurate, and user-friendly code.

---

## Why This Project Is Non-Trivial

Fund fee structures sound simple on the surface — "2 and 20" — but the actual mechanics are nuanced in ways that trip up even finance professionals. This tool correctly handles all of the following:

**Fee calculation edge cases:**
- Management fee on *beginning* vs *ending* AUM (different funds use different conventions, and the formula changes)
- Incentive fee calculated *independent of* vs *net of* management fees — a distinction that materially changes the GP's take

**Three distinct hurdle rate mechanics:**
- **Soft Hurdle** — once the threshold is crossed, the fee applies to *all* profits, not just the excess. This requires careful conditional logic.
- **Hard Hurdle** — the fee only applies to returns *above* the hurdle. Different formula, different LP/GP economics.
- **Catchup Clause** — the most complex of the three. The GP "catches up" to their full carry entitlement before profits split normally. This required building a separate `catchup()` function that computes the precise NAV band within which the catchup applies.

**High-Water Mark (HWM) with cashflow adjustments:**
- Most implementations of HWM simply track the highest fund value. This tool goes further — when investors add or withdraw capital mid-fund, the HWM is **scaled proportionally** to the new AUM, preventing artificial incentive fee distortions. This is how institutional funds actually handle it.

**Clawback Provision:**
- At fund close, the tool checks whether the GP has been overpaid in incentive fees relative to the fund's *overall* profit. If the fund had strong early years but weak later years, the cumulative carry paid may exceed the GP's fair entitlement — and the clawback amount is computed accordingly.

---

## Skills Demonstrated

| Skill Area | Demonstration |
|---|---|
| **Financial Knowledge** | Deep understanding of PE/HF fee structures, LP-GP economics, carry mechanics, and return attribution |
| **Python Programming** | Modular function design, conditional logic, loops, list management, dynamic data building |
| **Data Handling** | Using `pandas` to dynamically build and display a growing DataFrame period by period |
| **Financial Mathematics** | IRR computation via `numpy_financial`, HWM scaling, NAV waterfall logic |
| **Edge Case Reasoning** | Handling negative first cashflows, zero-return periods, HWM below gross AUM conditions, and fund structure variations |

> **Note on Presentation Layer:** The output formatting — `PrettyTable` for the summary tables and `pandas` tabulation — was implemented with AI assistance. This is intentional: the presentation layer is not the point of this project. The financial logic, fee mechanics, HWM methodology, and calculation architecture are entirely my own work and reflect where the real intellectual effort lies.

---

## Features at a Glance

- Management fee on Beginning or Ending AUM
- Three hurdle types: Soft, Hard, Catchup
- High-Water Mark tracking with proportional cashflow adjustment
- Incentive fee independent of or net of management fee
- Clawback provision with GP overpayment calculation
- Live period table with all key metrics after each year
- Final performance summary: total fees, closing AUM, and net IRR
- Confirmation loop to catch input errors before the calculation runs

---

## Requirements

- Python 3.8+

```bash
pip install pandas numpy_financial prettytable
```

---

## How to Run

```bash
python Fund_fee_calculator.py
```

The program is fully interactive — no config files or arguments needed. Follow the prompts. **CAPS LOCK should be on** as letter inputs (`B`, `E`, `S`, `H`, `C`, `Y`, `N`) are expected in uppercase.

---

## Input Reference

### Step 1 — Fund Parameters

| Parameter | What to Enter |
|---|---|
| Management Fee | Decimal (e.g. `0.02` for 2%) |
| Fee Basis | `B` = Beginning AUM, `E` = Ending AUM |
| Hurdle Rate | Decimal (e.g. `0.08` for 8%) |
| Hurdle Type | `S` = Soft, `H` = Hard, `C` = Catchup |
| Incentive Fee Rate | Decimal (e.g. `0.20` for 20%) |
| Incentive Fee Basis | `D` = Net of Mgmt Fee, `I` = Independent |
| Clawback | `Y` = Yes, `N` = No |

A summary table is shown after entry — confirm with `Y` to proceed or `N` to re-enter.

### Step 2 — Cashflows and Returns (per period)

- Enter the **initial investment as the first cashflow** (positive value)
- Each subsequent period: enter the period's cashflow (+ for inflows, − for outflows) and gross return
- A full period table is printed after each entry
- Enter `Y` to add another period or `N` to finalise and generate the summary

---

## Understanding the Fee Logic

### Management Fee

| Basis | Formula |
|---|---|
| Beginning AUM | `mgmt_fee × Beginning AUM` |
| Ending AUM | `mgmt_fee × (1 + gross_return) × Beginning AUM` |

### Hurdle Types

**Soft Hurdle** — If gross return exceeds the hurdle, the incentive fee applies to all profits above the HWM. Think of the hurdle as a gate: once you're through, the fee is on everything.

**Hard Hurdle** — The incentive fee *only* applies to returns in excess of the hurdle. The GP earns nothing on the portion of returns up to the hurdle rate.

**Catchup** — Once the hurdle is cleared, 100% of incremental profits go to the GP until they've received their full carry entitlement. After that, profits split at the stated incentive rate. This is the standard structure in most PE fund waterfall agreements.

### High-Water Mark

The HWM prevents the GP from charging incentive fees on recovered losses. If the fund drops in value, no carry is charged until it surpasses its prior high. When new capital is added or withdrawn, the HWM is adjusted proportionally — `new HWM = prior HWM × (new Beginning AUM / prior Ending AUM)` — so the LP's fee threshold scales correctly with their economic exposure.

### Clawback

At the end of the fund:
- **GP's fair entitlement** = `incentive_rate × max(0, total profit)`
- **Clawback** = `max(0, total incentive fees paid − GP entitlement)`

If the GP collected more carry than they were ultimately entitled to based on full-fund performance, the clawback amount is the excess to be returned.

---

## Output Reference

### Period Table

| Column | What It Shows |
|---|---|
| Period | Period number |
| Beginning AUM | Opening AUM before cashflows |
| Cashflow for the Period | Net capital in/out |
| BGN AUM + Cashflow | Adjusted opening AUM |
| Gross Return | Period gross return |
| Gross AUM | Pre-fee AUM after return |
| High Water Mark | HWM threshold for this period |
| Management Fee | Fee charged this period |
| Incentive Fee | Carry charged this period |
| End AUM | Net AUM after all fees |

### Final Summary

| Metric | What It Shows |
|---|---|
| Total Invested Amount | Sum of all capital contributions |
| Total Management Fees Paid | Cumulative management fees |
| Total Incentive Fees Paid | Cumulative carry |
| Closing Value of Investment | Final net AUM |
| IRR Earned on the Investment | Net IRR across all cashflows |
| Clawback Amount | GP overpayment, if applicable |

---

## Example

**Setup:** 2% management fee on beginning AUM · 8% soft hurdle · 20% incentive fee (net of mgmt fee) · No clawback

**Period 1:** $1,000,000 initial investment · 15% gross return

```
Gross AUM            = $1,000,000 × 1.15              = $1,150,000
Management Fee       = 2% × $1,000,000                = $20,000
Incentive Fee Base   = $1,150,000 − $20,000           = $1,130,000
Above HWM by         = $1,130,000 − $1,000,000        = $130,000
Incentive Fee        = 20% × $130,000                 = $26,000
Ending AUM           = $1,150,000 − $20,000 − $26,000 = $1,104,000
HWM updated to       $1,104,000
```

---

## Functions Reference

| Function | Purpose |
|---|---|
| `mgmt_fee_calculation()` | Computes management fee on beginning or ending AUM |
| `catchup()` | Computes incentive fee under a catchup clause, with NAV band logic |
| `incentive_fee_calculation()` | Master function routing to the correct hurdle logic (S/H/C) |
| `clawback_provision()` | Computes GP overpayment at fund close |
| `calculation_of_End_of_fund_value()` | Computes net ending AUM after all fees |

---

## Notes & Scope

- The clawback formula is a standard simplified model. Real-world fund agreements can involve tax distributions, tiered carry, and GP commitment offsets not covered here.
- The catchup assumes a standard 100% GP catchup. Some fund agreements use partial catchups (e.g. 50/50 in the catchup band) — a straightforward extension of the existing `catchup()` function.
- There is no file import — all inputs are entered interactively. A natural next step would be CSV import or a simple front-end interface.
- Restart the script to model a new fund.
