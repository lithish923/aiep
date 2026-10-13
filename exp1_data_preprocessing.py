"""
EXPERIMENT 1 — DATA PRE-PROCESSING
Source: 22IT702 LAB MANUAL (Page 2)
"""

import pandas as pd

# Load dataset
data = pd.read_csv("sample_data.csv")

# Remove missing values
data = data.dropna()

# Remove duplicates
data = data.drop_duplicates()

# Save cleaned dataset
data.to_csv("cleaned_dataset.csv", index=False)

print("Data preprocessing completed successfully.")
