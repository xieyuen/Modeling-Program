"""
简单工具
画完图记得show()(pyplot.show和这里的show都一样)
"""

from typing import Iterable

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


def plot(x, y, xlabel=None, ylabel=None):
    """画散点图"""
    plt.scatter(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def show():
    plt.show()
