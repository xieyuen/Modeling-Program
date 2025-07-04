import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import t
from sklearn.linear_model import LinearRegression

from data.constants import Title, Labels
from tools import adjusted_r_squared, p_values


def main():
    # 读取数据
    original_data = pd.read_excel(
        "./data/data.xlsx"
    )

    Xi = original_data[Title.X]
    y = original_data[Title.PM_CONCENTRATION]


    # print(original_data.head())

    model = LinearRegression()
    model.fit(Xi, y)

    print(
        f"回归系数: {model.coef_}\n"
        f"截距: {model.intercept_}\n"
        f"R方: {model.score(Xi, y)}"
    )

    p_value = p_values(model, Xi, y)

    print("特征:", Xi.columns.tolist())
    print("P值:", p_value)
    print("调整R方", adjusted_r_squared(model, Xi, y))




    """
    # 第一幅图
    plt.subplot(1,3,1)
    plt.scatter(
        original_data[Title.TRAFFIC_FLOW],
        original_data[Title.PM_CONCENTRATION],
    )
    plt.xlabel(Labels.TRAFFIC_FLOW)
    plt.ylabel(Labels.PM_CONCENTRATION)

    # 第二幅图
    plt.subplot(1,3,2)
    plt.scatter(
        original_data[Title.AVERAGE_TEMPERTURE],
        original_data[Title.PM_CONCENTRATION],
    )
    plt.xlabel(Labels.AVERAGE_TEMPERTURE)
    plt.ylabel(Labels.PM_CONCENTRATION)

    # 第三幅图
    plt.subplot(1,3,3)
    plt.scatter(
        original_data[Title.HUMIDITY],
        original_data[Title.PM_CONCENTRATION],
    )
    plt.xlabel(Labels.HUMIDITY)
    plt.ylabel(Labels.PM_CONCENTRATION)
    """

    """
    # 删除异常值
    original_data.drop(
        original_data[original_data[Title.WIND_SPEED] == 240].index,
        inplace=True
    )

    plt.scatter(
        original_data[Title.WIND_SPEED],
        original_data[Title.PM_CONCENTRATION],
    )
    plt.xlabel(Labels.WIND_SPEED)
    plt.ylabel(Labels.PM_CONCENTRATION)
    """

    """
    plt.scatter(
        original_data[Title.TRAFFIC_FLOW],
        original_data[Title.PM_CONCENTRATION],
        label="original data",
    )
    plt.xlabel(Labels.TRAFFIC_FLOW)
    plt.ylabel(Labels.PM_CONCENTRATION)

    # 线性模型构建
    model = LinearRegression()
    x = original_data[Title.TRAFFIC_FLOW].values.reshape(-1,1)
    y = original_data[Title.PM_CONCENTRATION].values
    model.fit(x, y)

    # 模型结果
    print(
        f"model: y = {model.coef_[0]} x + {model.intercept_}\n"
        f"R^2: {model.score(x, y)}"
    )

    # 画在散点图上
    plt.plot(
        (xrange:=np.linspace(x.min(),x.max()).reshape(-1,1)),
        model.predict(xrange),
        label="model prediction line",
        color="red",
    )

    plt.legend()
    plt.show()
    """


if __name__ == "__main__":
    main()
