import pandas as pd

df = pd.read_csv('emissions_cleaned.csv')

def mean(df):
    df = df['Emissions.Type.CO2'].mean()
    return df

# Uncomment these lines only for manual testing and comment them before running testMean.py
# a = mean(df)
# print(a)