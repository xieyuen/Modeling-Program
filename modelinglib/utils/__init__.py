import numpy as _np
from pandas import _DataFrame, _Series
from scipy.stats import t as _t


def remove(data: _DataFrame, condition: _Series):
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
        inplace=True,
    )


def remove_na(data: _DataFrame):
    """
    删除所有有数据缺失的行，会直接修改数据
    """
    for subset in data:
        data.dropna(
            subset=subset,
            inplace=True,
        )


def r_squared(model, X, y):
    return model.score(X, y)


def adjusted_r_squared(X, r2):
    # 计算调整R²
    n, p = X.shape  # 样本数和特征数
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

    return adjusted_r2


def p(model, X, y):
    coefficients = model.coef_
    y_pred = model.predict(X)

    residuals = y - y_pred
    dof = len(X) - len(coefficients) - 1  # 自由度
    mse = _np.sum(residuals ** 2) / dof

    X_with_const = _np.column_stack([_np.ones(len(X)), X])  # 添加截距项
    cov_matrix = _np.linalg.inv(X_with_const.T @ X_with_const) * mse
    std_errors = _np.sqrt(_np.diag(cov_matrix))[1:]  # 忽略截距的标准误差

    # 计算t统计量和P值
    t_stats = coefficients / std_errors
    p_value = 2 * (1 - _t.cdf(_np.abs(t_stats), df=dof))

    return p_value


def related_r(x, y):
    r"""
    样本相关系数

    计算公式(Latex代码)
    r = \frac{
        \sum_{i=1}^{n}
            x_i y_i - n\bar{x}\bar{y}
    }{
        \sqrt{\sum_{i=1}^{n}x_i^2-n\bar{x}^2}
        \sqrt{\sum_{i=1}^{n}y_i^2-n\bar{y}^2}
    }

    Args:
        x (SeriesLike): 自变量的数据
        y (SeriesLike): 因变量的数据
    """
    n = len(x)  # n
    x_mean = x.mean()  # \bar{x}
    y_mean = y.mean()  # \bar{y}

    sum_xiyi = _np.sum(xi*yi for xi, yi in zip(x, y))
    sum_xi2 = _np.sum(xi ** 2 for xi in x)
    sum_yi2 = _np.sum(yi ** 2 for yi in y)

    return (sum_xiyi - n * x_mean * y_mean) / (_np.sqrt(
        (sum_xi2 - n * x_mean ** 2) * (sum_yi2 - n * y_mean ** 2)
    ))


def print_result_for_lm(model, x, y):
    print("变量:", *x.columns.values)
    print("回归系数:", *model.coef_)
    print(f"截距: {model.intercept_}")
    print("P值:", *p(model, x, y))
    print(f"决定R方: {model.score(x, y)}")
    print(f"调整R方: {adjusted_r_squared(model.score(x, y), x)}")


__all__ = [i for i in globals() if not i.startswith("_")]
