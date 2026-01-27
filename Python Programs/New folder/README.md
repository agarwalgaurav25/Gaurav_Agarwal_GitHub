# 📊 Fund Performance & Fee Calculation Notebook

## Overview
A Python-based notebook that models **multi-period investment fund performance** with **realistic management and incentive fee mechanics**.

The project focuses on correctly implementing **High-Water Marks (HWM)** and **Hurdle Rates**, which are often simplified or incorrectly handled in basic fund models.

---

## Why This Project
- Demonstrates **practical understanding of fund fee structures**
- Implements **HWM logic across multiple periods**
- Handles **Soft vs Hard hurdle** incentive fees
- Emphasizes **transparent, auditable calculations**

This is a **fund mechanics model**, not an investment or valuation tool.

---

## Key Features
- 📈 Multi-period NAV simulation  
- 💼 Management fee on **Beginning or Ending AUM**  
- 💧 High-Water Mark enforcement  
- 🚧 Soft and Hard hurdle support  
- 🧮 Clean, tabular output using pandas  

---

## What’s Modeled
For each period:
- Beginning AUM
- Gross Return
- Management Fee
- Incentive Fee
- Ending AUM
- Updated High-Water Mark

---

## Tech Stack
- **Python**
- **Pandas**
- **Jupyter / Google Colab**

---

## Scope & Limitations
- Fund-level mechanics only (no security-level portfolios)
- Deterministic annual returns
- Simplified clawback logic

---

## Disclaimer
For educational and analytical purposes only.
