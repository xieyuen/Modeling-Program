from typing import Iterable

import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame, Series
from scipy.stats import t


def remove(data: DataFrame, condition: Series | Iterable):
    """
    删除符合条件的行，会直接修改数据

    Args:
        data (DataFrame): 要修改的数据
        condition (SeriesLike): 条件
    
    Example:
        >>> remove(data, data["x"]==1)
    """
    data.drop(
        data[condition].index,
        inplace=True
    )


def remove_na(data: DataFrame):
    """
    删除所有有数据缺失的行，会直接修改数据
    """
    for subset in data:
        data.dropna(
            subset=subset,
            inplace=True
        )


def scatter(x, y, *, xlabel=None, ylabel=None, **kwargs):
    """画散点图"""
    plt.scatter(x, y, **kwargs)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def plot(model, x_range, label="model prediction line", **kwargs):
    """画回归线"""
    x = np.linspace(x_range.min(), x_range.max()).reshape(-1, 1)
    y = model.predict(x)
    plt.plot(x, y, label=label, **kwargs)


def show():
    plt.legend()  # 图例
    plt.show()  # 图像


def r_squared(model, X, y):
    return model.score(X, y)


def adjusted_r_squared(r2, X):
    # 计算调整R²
    n, p = X.shape  # 样本数和特征数
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

    return adjusted_r2


def p(model, X, y):
    coefficients = model.coef_
    y_pred = model.predict(X)

    residuals = y - y_pred
    dof = len(X) - len(coefficients) - 1  # 自由度
    mse = np.sum(residuals ** 2) / dof

    X_with_const = np.column_stack([np.ones(len(X)), X])  # 添加截距项
    cov_matrix = np.linalg.inv(X_with_const.T @ X_with_const) * mse
    std_errors = np.sqrt(np.diag(cov_matrix))[1:]  # 忽略截距的标准误差

    # 计算t统计量和P值
    t_stats = coefficients / std_errors
    p_value = 2 * (1 - t.cdf(np.abs(t_stats), df=dof))

    return p_value
