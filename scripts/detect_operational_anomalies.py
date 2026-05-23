import pandas as pd

# Load validated dataset
df = pd.read_csv(
    "data/processed/validated_workforce_data.csv"
)

# Detect low attendance
low_attendance = df[
    df["attendance_rate"] < 94
]

# Detect large workforce gaps
large_gap = df[
    df["worker_gap"] >= 10
]

# Detect low harvest productivity
low_productivity = df[
    (df["kg_harvested"] > 0) &
    (df["kg_harvested"] < 5000)
]

# Combine anomalies
anomalies = pd.concat([
    low_attendance,
    large_gap,
    low_productivity
]).drop_duplicates()

# Save anomalies report
anomalies.to_csv(
    "reports/operational_anomalies_report.csv",
    index=False
)

print("Operational anomalies detected successfully.")