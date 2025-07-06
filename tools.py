from typing import Iterable

import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame, Series


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


def scatter(x, y, *, xlabel=None, ylabel=None,**kwargs):
    """画散点图"""
    plt.scatter(x, y, **kwargs)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def plot(model, x_range, label="model prediction line",**kwargs):
    """画回归线"""
    x = np.linspace(x_range.min(), x_range.max()).reshape(-1, 1)
    y = model.predict(x)
    plt.plot(x, y, label=label, **kwargs)


def show():
    plt.legend()  # 图例
    plt.show()  # 图像
