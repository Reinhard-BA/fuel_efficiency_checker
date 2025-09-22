import pandas as pd
import glob
import os

# Folder where your files are
folder_path = "C:/Users/ThinkPad/Desktop/Python/VS Code/vehicle_mpg_cal/mpg_data"

# Collect all CSV and XLSX files
files = glob.glob(os.path.join(folder_path, "*.csv")) + glob.glob(os.path.join(folder_path, "*.xlsx"))

all_dataframes = []

for file in files:
    if file.endswith(".csv"):
        df = pd.read_csv(file)
    elif file.endswith(".xlsx"):
        df = pd.read_excel(file)
    else:
        continue  # skip unknown formats
    
    all_dataframes.append(df)

# Concatenate all data
merged_df = pd.concat(all_dataframes, ignore_index=True)

# Save as one CSV
merged_df.to_csv("merged_mpg_data.csv", index=False)
