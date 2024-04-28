#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd


def get_data(filename):
    df = pd.read_excel(filename, na_values=['?'])
    return df


def get_data1():
    df = get_data('data/附件1.xlsx')
    df.drop(df.tail(2).index, inplace=True)
    return df


def get_data2():
    df = get_data('data/附件2.xlsx')
    df.drop(df.tail(3).index, inplace=True)
    return df


def get_data1c():
    return get_data('data/附件1_改.xlsx')
