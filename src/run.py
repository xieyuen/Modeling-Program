import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from statsmodels import api as sm

from lib import utils
from lib.constants import Index
from lib.nn.normal import NeuralNetwork as NorNN
from lib.nn.regularized import NeuralNetwork as RNN


def linear_2():
    data = pd.read_excel("./data/data.xlsx")

    utils.remove_na(data)

    y = data[Index.WATER_RESOURCE]
    x = data[Index.X_]

    model = LinearRegression()

    model.fit(x, y)

    utils.print_result_for_lm(model, x, y)


def linear_all():
    data = pd.read_excel("./data/data.xlsx")

    utils.remove_na(data)

    y = data[Index.WATER_RESOURCE]
    x = data[Index.X]

    model = LinearRegression()

    model.fit(x, y)

    m2 = sm.OLS(y, sm.add_constant(x)).fit()

    print(m2.summary())

    utils.print_result_for_lm(model, x, y)


def linear_2_standardized():
    # 读取数据
    data = pd.read_excel("./data/standardized.xlsx")
    # 定义因变量
    y = data[Index.WATER_RESOURCE]
    # 定义自变量
    x = data[Index.X_]

    # 创建线性回归模型
    model = LinearRegression()

    # 拟合模型
    model.fit(x, y)

    # 使用OLS方法拟合模型
    m2 = sm.OLS(y, sm.add_constant(x)).fit()
    # 打印模型摘要
    print(m2.summary())

    # 打印线性回归模型结果
    utils.print_result_for_lm(model, x, y)


def nn_2():
    data = pd.read_excel("./data/data.xlsx")

    utils.remove_na(data)

    y = data[Index.WATER_RESOURCE]
    x = data[Index.X_]

    nn = NorNN()
    nn.train(x, y)

    # 评估
    metrics = nn.evaluate(x, y)
    print(f"""
    评估结果:
    R²: {metrics['r2']:.3f}
    调整R²: {metrics['adjusted_r2']:.3f} 
    RMSE: {metrics['rmse']:.2f}
    (基于{metrics['n_samples']}个样本和{metrics['n_features']}个特征)
    """)


def nn_all():
    data = pd.read_excel("./data/data.xlsx")

    utils.remove_na(data)

    y = data[Index.WATER_RESOURCE]
    x = data[Index.X]

    nn = NorNN()
    nn.train(x, y)

    # 评估
    metrics = nn.evaluate(x, y)
    print(f"""
    评估结果:
    R²: {metrics['r2']:.3f}
    调整R²: {metrics['adjusted_r2']:.3f} 
    RMSE: {metrics['rmse']:.2f}
    (基于{metrics['n_samples']}个样本和{metrics['n_features']}个特征)
    """)


def r_nn_all():
    data = pd.read_excel("./data/data.xlsx")

    utils.remove_na(data)

    y = data[Index.WATER_RESOURCE]
    x = data[Index.X]

    nn = RNN()
    nn.train(x, y)

    # 评估
    metrics = nn.evaluate(x, y)
    print(f"""
    评估结果:
    R²: {metrics['r2']:.3f}
    RMSE: {metrics['rmse']:.2f}
    """)
    nn.save("./model/NeuralNetwork/regular_all.pkl")


def r_nn_2():
    data = pd.read_excel("./data/data.xlsx")

    utils.remove_na(data)

    y = data[Index.WATER_RESOURCE]
    x = data[Index.X_]

    nn = RNN()
    nn.train(x, y)

    # 评估
    metrics = nn.evaluate(x, y)
    print(f"""
    评估结果:
    R²: {metrics['r2']:.3f}
    RMSE: {metrics['rmse']:.2f}
    """)
    nn.save("./model/NeuralNetwork/regular_2.pkl")


def related_r():
    data = pd.read_excel("./data/data.xlsx")

    utils.remove_na(data)

    y = data[Index.WATER_RESOURCE]

    for i in Index.X:
        x = data[i]
        r = utils.related_r(x, y)
        print(f"{i} 的样本相关系数:", r)
