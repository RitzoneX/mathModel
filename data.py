import pandas as pd


def get_data1():
    df = pd.read_excel('附件1.xlsx', na_values=['?'])
    df.drop(df.tail(2).index, inplace=True)  # drop last 2 rows
    return df
