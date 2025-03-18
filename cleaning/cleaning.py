import pandas as pd

# Load the dirty dataset with duplicates
df = pd.read_csv("emissions_dirty.csv")

# Keep only rows where the year is a multiple of 5
df = df[df["Year"] % 5 == 0]

# Fill missing values with estimates
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']: 
        df[col].fillna(method='bfill', inplace=True)

# Remove unused columns
df = df.drop(columns=['Ratio.Per GDP', 'Ratio.Per Capita'])

# Remove duplicate rows
df = df.drop_duplicates()

# Save the cleaned dataset
df.to_csv("emissions_cleaned.csv", index=False, encoding="utf-8")

print("Cleaned dataset saved as emissions_cleaned.csv")
