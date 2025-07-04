import numpy as np
from scipy.stats import t


def r_squared(model, X, y):
    return model.score(X, y)


def adjusted_r_squared(model, X, y):
    r2 = model.score(X, y)

    # 计算调整R²
    n, p = X.shape  # 样本数和特征数
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

    return adjusted_r2


def p_values(model, X, y):
    coefficients = model.coef_
    y_pred = model.predict(X)
    
    residuals = y - y_pred
    dof = len(X) - len(coefficients) - 1  # 自由度
    mse = np.sum(residuals**2) / dof
    
    X_with_const = np.column_stack([np.ones(len(X)), X])  # 添加截距项
    cov_matrix = np.linalg.inv(X_with_const.T @ X_with_const) * mse
    std_errors = np.sqrt(np.diag(cov_matrix))[1:]  # 忽略截距的标准误差

    # 计算t统计量和P值
    t_stats = coefficients / std_errors
    p_value = 2 * (1 - t.cdf(np.abs(t_stats), df=dof))

    return p_value
