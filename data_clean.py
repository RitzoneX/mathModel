#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd

import data


def data_clean(df):
    # x = '特征8'
    # sns.countplot(x=x, data=df, palette='Set2')
    # plt.show()
    # print(df[x].value_counts())

    # 预览数据
    df['类别'].replace({2: 0, 4: 1}, inplace=True)
    # print('数据个数 {}.'.format(df.shape[0]))

    # 处理数据
    print(df.isnull().sum())
    print('缺失值共有%s个' % df.isnull().sum().sum())
    for i in range(1, 10):
        col = '特征%s' % i
        m = df[col].mode()[0]
        df[col].fillna(m, inplace=True)

        # 替换异常值
        df[col] = df[col].apply(lambda x: m if x > 20 else x)


if __name__ == '__main__':
    df = data.get_data2()
    # print(df.info())
    df.describe().to_excel('data/describe2.xlsx')

    # data_clean(df)
    # df.to_excel('附件1_改.xlsx')
