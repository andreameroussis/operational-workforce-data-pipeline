import pandas as pd

# Load validated dataset
df = pd.read_csv(
    "data/processed/validated_workforce_data.csv"
)

# Create productivity metric
df["kg_per_worker"] = (
    df["kg_harvested"] / df["actual_workers"]
).round(2)

# Replace division errors
df["kg_per_worker"] = (
    df["kg_per_worker"]
    .fillna(0)
)

# Create operational status
df["operational_status"] = "Normal"

df.loc[
    df["attendance_alert"] == True,
    "operational_status"
] = "Attendance Risk"

df.loc[
    df["critical_gap"] == True,
    "operational_status"
] = "Critical Gap"

# Save final dataset
df.to_csv(
    "data/final/final_operational_dataset.csv",
    index=False
)

print("Final operational dataset created successfully.")