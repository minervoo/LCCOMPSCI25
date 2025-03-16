import pandas as pd
import numpy as np

# Load the original dataset
df = pd.read_csv("emissions.csv")

# 1. Keep only relevant years (2000 and later)
df = df[df["Year"] >= 2000]

# 2. Clean missing values
df.fillna(df.median(numeric_only=True), inplace=True)  # Fill numeric NaNs with median

# 3. Ensure numeric columns are in the right format
for col in df.columns:
    if df[col].dtype == 'O':  # If column is object (string)
        df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numbers

# 4. Calculate target sample size to get around 8000 rows
target_size = 8000
current_size = len(df)
sample_ratio = target_size / current_size

# 5. Sample the data while preserving time series structure
df = df.sample(frac=sample_ratio, random_state=42)

# 6. Sort by date to maintain chronological order
df = df.sort_values('Date')

# 7. Save the cleaned & sampled dataset
df.to_csv("emissions_cleaned.csv", index=False)

print(f"Original dataset size: {current_size}")
print(f"Cleaned dataset size: {len(df)}")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print("Cleaned dataset saved as emissions_cleaned.csv")