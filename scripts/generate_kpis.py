import pandas as pd

# Load validated dataset
df = pd.read_csv(
    "data/processed/validated_workforce_data.csv"
)

# KPI calculations
total_projected = df["projected_workers"].sum()

total_actual = df["actual_workers"].sum()

overall_attendance = round(
    df["attendance_rate"].mean(),
    2
)

total_gap = df["worker_gap"].sum()

total_harvest = df["kg_harvested"].sum()

# Create KPI dataframe
kpi_df = pd.DataFrame([{

    "total_projected_workers": total_projected,

    "total_actual_workers": total_actual,

    "overall_attendance_rate": overall_attendance,

    "total_worker_gap": total_gap,

    "total_kg_harvested": total_harvest

}])

# Save KPI report
kpi_df.to_csv(
    "reports/operational_kpis.csv",
    index=False
)

print("Operational KPIs generated successfully.")