import pandas as pd
from flask import jsonify

df = pd.read_csv("emissions_cleaned.csv")

def mean():
    mean_CO2 = df['Emissions.Type.CO2'].mean()
    return mean_CO2

a = mean()
print(a)