import seaborn as sns
import matplotlib.pyplot as plt

#! 解决不显示的问题：中文设置为宋体格式
plt.rcParams['font.family'] = ["Times New Roman", 'SimHei']

df = sns.load_dataset("titanic")
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(14,11))

sns.boxplot(ax=axs[0,0], data=df, x ="age", y="class")
axs[0,0].set_title("图1：舱位等级的年龄分布", fontsize=14)
axs[0,0].xaxis.grid(True)

# sns.boxplot(ax=axs[0,1], data=df, x="age", y="class", hue="alive")
sns.boxplot(ax=axs[0,1], data=df, x="class", y="age", hue="alive")  # 对掉x、y参数可以切换水平、垂直绘图
axs[0,1].set_ylabel('')
axs[0,1].set_title("图2：基于存活与否分组的舱位等级年龄分布", fontsize=14)
axs[0,1].yaxis.grid(True)

sns.boxplot(ax=axs[0,2], data=df[["age", "fare"]], orient="h")
axs[0,2].set_title("图3：绘制多列数值型数组的箱线图", fontsize=14)
axs[0,2].xaxis.grid(True)

sns.boxplot(ax=axs[1,0], data=df, x="fare", y="deck", hue="deck", dodge=False)
axs[1,0].set_title("图4：hue参数与dodge参数的作用", fontsize=14)
axs[1,0].xaxis.grid(True)

sns.boxplot(ax=axs[1,1], data=df, x="fare", y="deck", order=["G", "F", "E", "D", "C", "B", "A"], hue="deck", dodge=False)
axs[1,1].set_title("图5：改变图4中y轴的排列次序", fontsize=14)
axs[1,1].xaxis.grid(True)

sns.boxplot(
    ax=axs[1,2], data=df, x="age", y="class",
    notch=True, showcaps=False,
    flierprops={"marker": "^"},
    # boxprops={"facecolor": (.4, .6, .8, .5)},
    medianprops={"color": "r"}
)
axs[1,2].set_title("图6：使用matplotlib.boxplot参数进行配置", fontsize=14)
axs[1,2].xaxis.grid(True)
plt.show()
