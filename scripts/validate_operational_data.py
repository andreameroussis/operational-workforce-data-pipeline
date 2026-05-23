import pandas as pd

# Load consolidated dataset
df = pd.read_csv(
    "data/processed/consolidated_workforce_data.csv"
)

# Calculate workforce gap
df["worker_gap"] = (
    df["projected_workers"] - df["actual_workers"]
)

# Flag attendance issues
df["attendance_alert"] = df["attendance_rate"] < 95

# Flag critical workforce gaps
df["critical_gap"] = df["worker_gap"] >= 10

# Save validated dataset
df.to_csv(
    "data/processed/validated_workforce_data.csv",
    index=False
)

print("Operational validation completed successfully.")