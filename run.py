import pandas as pd
from sklearn.linear_model import LinearRegression
from lib import tools
from lib.constants import Index
from lib.nn import NeuralNetwork


def linear_2():
    data = pd.read_excel("./data/data.xlsx")

    tools.remove_na(data)

    y = data[Index.WATER_RESOURSE]
    x = data[Index.X_]

    model = LinearRegression()

    model.fit(x, y)

    print("变量:", *x.columns.values)
    print("回归系数:", *model.coef_)
    print(f"截距: {model.intercept_}")
    print(f"决定R方: {model.score(x, y)}")
    print(f"调整R方: {tools.adjusted_r_squared(model.score(x, y), x)}")
    print("P值:", *tools.p(model, x, y))


def linear_all():
    data = pd.read_excel("./data/data.xlsx")

    tools.remove_na(data)

    y = data[Index.WATER_RESOURSE]
    x = data[Index.X]

    model = LinearRegression()

    model.fit(x, y)

    print("变量:", *x.columns.values)
    print("回归系数:", *model.coef_)
    print(f"截距: {model.intercept_}")
    print(f"决定R方: {model.score(x, y)}")
    print(f"调整R方: {tools.adjusted_r_squared(model.score(x, y), x)}")
    print("P值:", *tools.p(model, x, y))


def nn_2():
    data = pd.read_excel("./data/data.xlsx")

    tools.remove_na(data)

    y = data[Index.WATER_RESOURSE]
    x = data[Index.X_]

    nn = NeuralNetwork()
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

    # 保存模型
    nn.save('./model/NeuralNetwork/all.pkl')


def nn_all():
    data = pd.read_excel("./data/data.xlsx")

    tools.remove_na(data)

    y = data[Index.WATER_RESOURSE]
    x = data[Index.X]

    nn = NeuralNetwork()
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

    # 保存模型
    nn.save('./model/NeuralNetwork/all.pkl')
