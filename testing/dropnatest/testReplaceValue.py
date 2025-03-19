import myDefinitions as md
import pandas as pd

testR = pd.read_csv('cases/5_boundaryCase.csv')

# Invalid Case
for i in testR.columns:
    if testR[i].dtype not in ['float64', 'int64'] and testR[i].isnull().any():
        print("Test cannot be done: Non-numeric column contains missing values.")
        exit()

# Fix For Boundary Case
if testR.isnull().all().all():  
    print("Test cannot be done: Empty DataFrame found.")
    exit()  

# The Expected Result (The ONE that HAS TO be correct)
testR.fillna(method='bfill', inplace=True)
expectedV = testR.to_string()
print('The expected value is: ', expectedV)

# The Actual Result
actualV = md.pandasTest(testR) 
print('The Actual value is: ', actualV)

if expectedV == actualV:
    print("Test Passed")
else:
    print("Test Failed")