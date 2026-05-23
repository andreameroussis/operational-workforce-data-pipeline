import pandas as pd

# Load validated dataset
df = pd.read_csv(
    "data/processed/validated_workforce_data.csv"
)

# Generate summary metrics
summary = {
    "total_projected_workers":
        df["projected_workers"].sum(),

    "total_actual_workers":
        df["actual_workers"].sum(),

    "average_attendance_rate":
        round(df["attendance_rate"].mean(), 2),

    "critical_gap_cases":
        df["critical_gap"].sum(),

    "attendance_alert_cases":
        df["attendance_alert"].sum()
}

# Convert summary into dataframe
summary_df = pd.DataFrame([summary])

# Save summary
summary_df.to_csv(
    "reports/operational_summary.csv",
    index=False
)

print("Operational summary generated successfully.")