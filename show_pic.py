#!/usr/bin/python
# -*- coding: UTF-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt

import data

# ! 解决不显示的问题：中文设置为宋体格式
# plt.rcParams['font.family'] = ["Times New Roman", 'SimHei']

df = data.get_data2()

df = df.drop(columns=['样本编号', '类别'])
print(df.isnull().sum())
print("共有%s个空值" % df.isnull().sum().sum())

fig = sns.boxplot(data=df)

fig.get_figure().savefig('imgs/boxplot2.png', dpi=400)
plt.show()
