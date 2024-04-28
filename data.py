import pandas as pd


def get_data(filename):
    df = pd.read_excel(filename, na_values=['?'])
    df.drop(df.tail(2).index, inplace=True)  # drop last 2 rows
    return df


def get_data1():
    return get_data('data/附件1.xlsx')


def get_data1c():
    return get_data('data/附件1_改.xlsx')
