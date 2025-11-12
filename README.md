# Restaurant Turnover Prediction (Hackathon) — Section 9

**Goal:** Predict a restaurant’s **Annual Turnover**.  
**Metric:** RMSE (lower is better).  
**Result:** Public leaderboard **Top-5**.

## TL;DR
- **Models:** CatBoost (raw target) + LightGBM (log target)
- **Categoricals:** one-hot (low-card), **target encoding** for City & Theme (CV-safe)
- **Ensemble:** **log-space convex blend** (CatBoost weight ≈ 0.75)
- **Repro:** See `03_final_submission.ipynb` and `outputs/submissions/final/`

## Repo structure

- Final notebook: [`notebooks/03_final_submission.ipynb`](notebooks/03_final_submission.ipynb)
- Winning CSV: [`outputs/submissions/final/FINAL_submission_blend_convex_logspace.csv`](outputs/submissions/final/FINAL_submission_blend_convex_logspace.csv)
- Run report: [`outputs/submissions/final/run_report.json`](outputs/submissions/final/run_report.json)
- Walkthrough PDF: [`docs/Section9_Hackathon_Final_Walkthrough.pdf`](docs/Section9_Hackathon_Final_Walkthrough.pdf)

.
├─ notebooks/
│ ├─ 02_baseline_model_step_by_step.ipynb
│ └─ 03_final_submission.ipynb
├─ outputs/
│ └─ submissions/
│ └─ final/
│ ├─ FINAL_submission_blend_convex_logspace.csv
│ ├─ run_report.json
│ ├─ requirements.txt
│ └─ README.md
├─ docs/
│ └─ Section9_Hackathon_Final_Walkthrough.pdf
├─ models/ # (optional placeholder)
├─ src/ # (optional helpers)
├─ .gitignore
└─ README.md

## Approach (short)
- Parsed date (day-first) → `Age_days`, `Open_month`, `Open_dow`
- Ratings: `__isna` flags + median impute
- City “-1” → “Unknown”
- **Target-encode** `City` and `Restaurant Theme` (K-Fold, smoothing)
- CatBoost + LightGBM (early stopping), blended in **log space**
- Chose weight via OOF sweep; optional calibrated variant tested

## Reproduce
1. Open `03_final_submission.ipynb`
2. Run all cells (expects data under your Drive in the same structure)
3. Final CSV appears in `outputs/submissions/final/`

## Notes
- Raw datasets omitted from repo.
- Final CSV fingerprinted (SHA256) in `run_report.json`.
