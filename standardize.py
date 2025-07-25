import pandas as pd
from sklearn.preprocessing import StandardScaler

from lib import utils

def z_score_normalize_excel(input_path, output_path, year_column='年份'):
    """
    对Excel文件进行Z-score标准化（排除年份列），删除空值行，确保年份信息不丢失
    
    参数:
    input_path: 输入Excel文件路径（.xlsx）
    output_path: 输出Excel文件路径（.xlsx）
    year_column: 年份列名（默认'年份'）
    """
    # 1. 读取数据
    df = pd.read_excel(input_path)
    
    # 2. 检查年份列是否存在
    if year_column not in df.columns:
        raise ValueError(f"列 '{year_column}' 不存在!")
    
    # 3. 删除空值行（使用自定义方法）
    utils.remove_na(df)
    df_cleaned = df.reset_index(drop=True)
    
    # 4. 分离年份列和其他数据列
    years = df_cleaned[year_column]
    data_to_scale = df_cleaned.drop(columns=[year_column])
    
    # 5. Z-score标准化
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_to_scale)
    
    # 6. 重建DataFrame（保持索引对齐）
    normalized_df = pd.DataFrame(
        scaled_data,
        columns=data_to_scale.columns,
        index=df_cleaned.index
    )
    normalized_df.insert(0, year_column, years)
    # normalized_df[year_column] = years
    
    # 7. 重置索引（可选）
    normalized_df.reset_index(drop=True, inplace=True)
    
    # 8. 保存结果
    normalized_df.to_excel(output_path, index=False)
    print(f"标准化完成，结果已保存至: {output_path}")

# 使用示例
z_score_normalize_excel(
    input_path="./data/data.xlsx",
    output_path="./data/standardized.xlsx",
    year_column="年份"  # 如果列名不是'年份'，需修改
)