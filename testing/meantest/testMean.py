import myDefinitions as md
import pandas as pd

testR = pd.read_csv('cases/5_boundarycase.csv')

# Invalid Test
for i in testR['Emissions.Type.CO2']:
    if not isinstance(i, (int, float)):
        print("Test cannot be done: 'Emissions.Type.CO2' column has non-numeric values.")
        exit()

# The Expected Result {The ONE that MUST be correct}
expectedV = testR['Emissions.Type.CO2'].mean()
print('The expected value is: ', expectedV)

# The Actual Result
actualV = md.mean(testR)
print('The Actual value is: ', actualV)

if expectedV == actualV:
    print("Test Passed")
else:
    print("Test Failed")