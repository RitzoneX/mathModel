#!/usr/bin/python
# -*- coding: UTF-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt

import data

# ! 解决不显示的问题：中文设置为宋体格式
# plt.rcParams['font.family'] = ["Times New Roman", 'SimHei']

df = data.get_data1()

print(df.isnull().sum())
print("共有%s个空值" % df.isnull().sum().sum())

fig = sns.boxplot(data=df.isnull().sum())

fig.get_figure().savefig('imgs/boxplot.png', dpi=400)
plt.show()
