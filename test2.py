import sklearn.experimental.enable_iterative_imputer# .enable_iterative_imputer
from sklearn.impute import IterativeImputer

from modelinglib.constants import Index
from src.get_all_data import get

from sklearn.preprocessing import QuantileTransformer, StandardScaler

def standardize_water_data(data):
    """
    标准化处理流程（适用于不含USAGE的数据）
    :param data: 包含Index.X_和Index.Y的DataFrame
    :return: 标准化后的DataFrame
    """
    # 确保列存在
    required_cols = Index.X_ + [Index.Y]  # ['年降雨量','年日照时间','水资源总量']
    assert all(col in data.columns for col in required_cols), "缺少必要列"
    
    # 拷贝避免污染原数据
    data_std = data.copy()
    
    # 1. 对年降雨量和水资源总量用分位数标准化（解决潜在偏态）
    qt_cols = [Index.RAIN, Index.Y]
    qt = QuantileTransformer(output_distribution='normal')
    data_std[qt_cols] = qt.fit_transform(data_std[qt_cols])
    
    # 2. 对年日照时间用全局标准化（量级稳定时更保真）
    scaler = StandardScaler()
    data_std[Index.TIME] = scaler.fit_transform(data_std[[Index.TIME]])
    
    return data_std


def handle_missing_values(data):
    """基于变量关系的缺失值填充"""
    # 1. 标记缺失状态（可选）
    for col in Index.X_:
        data[f'{col}_missing'] = data[col].isna().astype(int)
    
    # 2. 多变量迭代填充（利用RAIN和TIME的相互关系）
    imputer = IterativeImputer(max_iter=10, random_state=42)
    data[Index.X_] = imputer.fit_transform(data[Index.X_])
    
    return data


data = get("./data/data2.xlsx")

# 组合应用
final_data = handle_missing_values(standardize_water_data(data))

import matplotlib.pyplot as plt

# 绘制标准化前后对比
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(x=Index.CITY, y=Index.RAIN, data=data)
plt.title('原始降雨量')

plt.subplot(1, 2, 2)
sns.boxplot(x=Index.CITY, y=Index.RAIN, data=final_data)
plt.title('标准化后降雨量')
plt.show()