import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import seaborn as sns

import data
from data_clean import data_clean

sns.set(style="white")  # 设置seaborn画图的背景为白色
sns.set(style="whitegrid", color_codes=True)

log_regression = None


def generate_mode(df=None):
    global log_regression
    # 定义预测变量和响应变量
    x = df[['特征%s' % x for x in range(1, 10)]]
    y = df['类别']

    # split the dataset into training (80%) and testing (20%) sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # 实例化模型对象
    log_regression = LogisticRegression()

    # 使用训练数据拟合模型
    log_regression.fit(x_train, y_train)

    # 使用测试数据进行预测
    y_pred = log_regression.predict(x_test)

    # 输出模型参数
    print(log_regression.intercept_, log_regression.coef_, log_regression.score(x_train, y_train))
    # [-2.86843745] [[-3.79999456e+00  4.03495132e-03 -1.36823955e-04]] 0.9691428571428572

    # 模型诊断
    # 测试完成后，我们需要分析模型表现. 首先创建混淆矩阵：
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(cnf_matrix)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    # # 计算 Pearson 相关系数
    # correlation_matrix = df.corr()
    # # 使用热图可视化 Pearson 相关系数
    # sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    # plt.show()

    logit_roc_auc = roc_auc_score(y_test, log_regression.predict(x_test))
    fpr, tpr, thresholds = roc_curve(y_test, log_regression.predict_proba(x_test)[:, 1])
    plt.figure()
    plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.savefig('Log_ROC')
    plt.show()


def import_data():
    # 将数据读入 DataFrame
    df = data.get_data1()

    data_clean(df)

    # # 相关系数
    # correlation_matrix = df.corr()
    # # 使用热图可视化 Pearson 相关系数
    # sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    # plt.show()

    generate_mode(df)


def predict():
    global log_regression

    df = pd.read_excel('附件2.xlsx', na_values=['?'])
    df.drop(df.tail(3).index, inplace=True)  # 删除最后3行

    # print(df)
    # df.plot()
    # plt.show()
    print('附件2包含的数据个数 {}.'.format(df.shape[0]))

    # print(df.isnull().sum())

    data_clean(df)

    df = df.drop(columns=['样本编号', '类别'])
    # 使用测试数据进行预测
    y_pred = log_regression.predict(df)
    print(y_pred)


if __name__ == '__main__':
    import_data()
    # predict()
