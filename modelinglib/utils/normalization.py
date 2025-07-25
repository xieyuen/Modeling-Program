import pandas as pd

class Normalize:
    def __init__(self, data: pd.DataFrame):
        self.data: pd.DataFrame = data

    def z_score(self):
        return (self.data - self.data.mean()) / self.std()

    def max_min(self, feature_range=(0, 1)):
        min_vals = self.data.min()
        max_vals = self.data.max()
        ranges = max_vals - min_vals
        ranges[ranges == 0] = 1  # 防止全部相同的数据导致报错
        
        # 标准化到 [0, 1]
        normalized = (self.data - min_vals) / ranges

        a, b = feature_range
        return normalized * (b - a) + a  # 放缩到 [a, b]
