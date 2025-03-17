import pandas as pd

df = pd.read_csv("emissions_dirty.csv")

def fillna_test(df):
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']: 
            df[col].fillna(method='bfill', inplace=True)
    return df.to_string()


# a = fillna_test(df)
# print(a)

