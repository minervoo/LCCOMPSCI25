import myDefinitions as md
import pandas as pd

# Unit test
test_df = pd.read_csv("edge_case.csv")

# Check for non-numeric values in 'Emissions.Type.CO2' column
if not pd.api.types.is_numeric_dtype(test_df['Emissions.Type.CO2']):
    raise ValueError("Test cannot be done: 'Emissions.Type.CO2' column has non-numeric values.")

# The Expected Result {The ONE that MUST be correct}
expected_mean = test_df['Emissions.Type.CO2'].mean()
print('The expected value is:', expected_mean)

# The Actual Result
actual_mean = md.mean()
print('The actual value is:', actual_mean)

# Debugging: Print the data used for calculation
print('Data used for expected mean calculation:')
print(test_df['Emissions.Type.CO2'])

# Use assertion for testing with a tolerance level
tolerance = 1e-5
assert abs(expected_mean - actual_mean) < tolerance, f"Test Failed: expected {expected_mean}, got {actual_mean}"
print("Test Passed")