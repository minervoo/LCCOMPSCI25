import pandas as pd

# Load your dataset
df = pd.read_csv("emissions_dirty.csv")  # Change to your actual file

# Identify numeric and non-numeric columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
non_numeric_cols = df.select_dtypes(exclude=['float64', 'int64']).columns

# Convert numeric columns to float to allow missing value assignment
df[numeric_cols] = df[numeric_cols].astype(float)

# Standard Case: Some missing values in numeric columns that can be filled using bfill
standard_case = df.copy()
standard_case.loc[2:4, numeric_cols] = pd.NA  # Introduce some missing values

# Edge Case: Missing values at the end of numeric columns
edge_case = df.copy()
edge_case.loc[edge_case.index[-3:], numeric_cols] = pd.NA  # Last few values are missing

# Stress Case: Entire numeric column missing values
stress_case = df.copy()
stress_case[numeric_cols] = pd.NA  # Whole numeric column missing

# Invalid Case: Non-numeric column contains missing values
invalid_case = df.copy()
invalid_case[non_numeric_cols] = invalid_case[non_numeric_cols].astype("string")  # Ensure dtype compatibility
invalid_case.loc[2:4, non_numeric_cols] = pd.NA  # Non-numeric columns affected

# Boundary Case: Completely empty dataset
boundary_case = pd.DataFrame(columns=df.columns)

# Save test cases as CSV files
standard_case.to_csv("standard_case.csv", index=False)
edge_case.to_csv("edge_case.csv", index=False)
stress_case.to_csv("stress_case.csv", index=False)
invalid_case.to_csv("invalid_case.csv", index=False)
boundary_case.to_csv("boundary_case.csv", index=False)

print("Test case CSV files generated successfully.")
