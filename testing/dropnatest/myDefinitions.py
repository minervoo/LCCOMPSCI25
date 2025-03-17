import pandas as pd

df = pd.read_csv('emissions_dirty.csv')

def pandasTest(df):
    df.fillna(method='bfill', inplace=True)
    return df.to_string()

# a = pandasTest(df)
# print(a)

