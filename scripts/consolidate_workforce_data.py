import pandas as pd
import os

# Folder containing raw files
raw_data_path = "data/raw"

# List to store datasets
all_dataframes = []

# Read all CSV files
for file in os.listdir(raw_data_path):

    if file.endswith(".csv"):

        file_path = os.path.join(raw_data_path, file)

        df = pd.read_csv(file_path)

        all_dataframes.append(df)

# Combine all datasets
consolidated_df = pd.concat(all_dataframes, ignore_index=True)

# Remove duplicates
consolidated_df = consolidated_df.drop_duplicates()

# Save processed dataset
output_path = "data/processed/consolidated_workforce_data.csv"

consolidated_df.to_csv(output_path, index=False)

print("Operational datasets consolidated successfully.")