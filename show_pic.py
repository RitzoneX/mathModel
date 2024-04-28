import seaborn as sns
import matplotlib.pyplot as plt

import data

# ! 解决不显示的问题：中文设置为宋体格式
# plt.rcParams['font.family'] = ["Times New Roman", 'SimHei']

df = data.get_data1()

fig = sns.boxplot(data=df)

fig.get_figure().savefig('imgs/boxplot.png', dpi = 400)
plt.show()
