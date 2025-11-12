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
