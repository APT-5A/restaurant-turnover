
import sys, pandas as pd

def check(path):
    df = pd.read_csv(path)
    expected_cols = ["Registration Number", "Annual Turnover"]
    problems = []

    if df.columns.tolist() != expected_cols:
        problems.append(f"Columns must be exactly {expected_cols} (got {df.columns.tolist()})")
    if len(df) != 500:
        problems.append(f"Row count must be 500 (got {len(df)})")
    if "Registration Number" in df.columns and not df["Registration Number"].is_unique:
        problems.append("Registration Number must be unique")

    if problems:
        raise SystemExit("Submission check failed:\n- " + "\n- ".join(problems))
    print("✅ Submission file passes format checks.")

if __name__ == "__main__":
    check(sys.argv[1])
