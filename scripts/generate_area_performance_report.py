import pandas as pd

# Load validated dataset
df = pd.read_csv(
    "data/processed/validated_workforce_data.csv"
)

# Group by operational area
area_summary = df.groupby("area").agg({

    "projected_workers": "sum",
    "actual_workers": "sum",
    "attendance_rate": "mean",
    "worker_gap": "sum"

}).reset_index()

# Round attendance
area_summary["attendance_rate"] = (
    area_summary["attendance_rate"].round(2)
)

# Sort by worker gap descending
area_summary = area_summary.sort_values(
    by="worker_gap",
    ascending=False
)

# Save report
area_summary.to_csv(
    "reports/area_performance_report.csv",
    index=False
)

print("Area performance report generated successfully.")