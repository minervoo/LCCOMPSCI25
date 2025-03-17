import myDefinitions as md
import pandas as pd

# Load the test data
test_df = pd.read_csv("stress_case.csv")

# Fix for invalid case
numeric_df = test_df.select_dtypes(include=['float64', 'int64'])
if numeric_df.empty:
    print("Test cannot be done: No numeric columns found.")
    exit()

# Fix for boundary case
if numeric_df.isnull().all().all():
    print("Test cannot be done: Empty DataFrame found.")
    exit()

# The expected result (the one that must be correct)
expected_df = numeric_df.copy()
for col in expected_df.columns:
    expected_df[col].fillna(method='bfill', inplace=True)
expected_result = expected_df.to_string()

# The actual result
actual_result = md.fillna_test(numeric_df)

# Compare the expected result with the actual result
if expected_result == actual_result:
    print("Test Passed")
else:
    print("Test Failed")
    print("Expected:")
    print(expected_result)
    print("Actual:")
    print(actual_result)