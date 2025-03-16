import pandas as pd
import numpy as np

# Load the dirty dataset
df = pd.read_csv("emissions_dirty.csv")

# Preserve original order by adding an index column
df["OriginalIndex"] = df.index

# Check column names and fix if necessary
print("Column names in dataset:", df.columns)
column_mapping = {
    "Emissions.Type.CO2": "CO2_Emissions",
    "Emissions.Type.NO2": "NO2_Emissions",
    "Emissions.Type.CH4": "CH4_Emissions"
}
df.rename(columns=column_mapping, inplace=True)

# Convert Year to numeric, removing bad values
df["Year"] = pd.to_numeric(df["Year"].astype(str).str.replace("'", ""), errors="coerce")

# Ensure even distribution of years when shortening dataset
latest_year = df["Year"].max()
early_year = df["Year"].min()
df = df.groupby("Year", group_keys=False).apply(lambda x: x.sample(n=min(len(x), 10), random_state=42))

# Convert emissions columns to numeric
for col in ["CO2_Emissions", "NO2_Emissions", "CH4_Emissions"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing values with median for emissions
for col in ["CO2_Emissions", "NO2_Emissions", "CH4_Emissions"]:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# Restore original order
df = df.sort_values(by="OriginalIndex").drop(columns=["OriginalIndex"])

# Drop unused columns
df = df.drop(columns=['Ratio.Per GDP', 'Ratio.Per Capita'])

# Save the cleaned dataset
df.to_csv("emissions_cleaned.csv", index=False)

print("Data cleaned and saved as 'emissions_cleaned.csv'")