import seaborn as sns
import matplotlib.pyplot as plt

import data

# ! 解决不显示的问题：中文设置为宋体格式
plt.rcParams['font.family'] = ["Times New Roman", 'SimHei']

df = data.get_data1()

sns.boxplot(data=df, y='特征8')

plt.show()
