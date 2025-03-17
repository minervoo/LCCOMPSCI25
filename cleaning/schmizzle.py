import pandas as pd

# Load your dataset
df = pd.read_csv("emissions_dirty.csv")  # Change to your actual file

# Standard Case: Some missing values that can be filled using bfill
standard_case = df.copy()
standard_case.iloc[2:4, 1] = None  # Introduce some missing values

# Edge Case: Missing values at the end of the column
edge_case = df.copy()
edge_case.iloc[-3:, 1] = None  # Last few values are missing

# Stress Case: Entire numeric column missing values
stress_case = df.copy()
stress_case.iloc[:, 1] = None  # Whole column missing

# Invalid Case: Missing values in a non-numeric column
invalid_case = df.copy()
invalid_case.iloc[2:4, 0] = None  # Assuming first column is non-numeric

# Boundary Case: Completely empty dataset
boundary_case = pd.DataFrame(columns=df.columns)

# Save test cases as CSV files
standard_case.to_csv("standard_case.csv", index=False)
edge_case.to_csv("edge_case.csv", index=False)
stress_case.to_csv("stress_case.csv", index=False)
invalid_case.to_csv("invalid_case.csv", index=False)
boundary_case.to_csv("boundary_case.csv", index=False)

print("Test case CSV files generated successfully.")
