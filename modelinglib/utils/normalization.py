import pandas as pd

class Normalizer:
    """Normalizer, abstract class, init for fiting"""
    def __init__(self, data: pd.DataFrame):
        self.original = data
        self.max = data.max()
        self.min = data.min()
        self.std = data.std()
        self.mean = data.mean()
        self.length = self.max - self.min

    def normalize(self, data: pd.DataFrame | None = None) -> pd.DataFrame:
        raise NotImplementedError

class ZScoreNormalizer(Normalizer):
    """Z-score normalizer"""
    def __normalize(self, data):
        return (data - self.mean) / self.std 

    def normalize(self, data=None):
        if data is None:
            if not hasattr(self, "normalized"):
                self.normalized = self.__normalize(self.original)
        
            return self.normalized
        return self.__normalize(data)


class MinMaxTargetRange:
    def __init__(self):
        self.length, self.max, self.min = None, None, None
        self.is_initialized = False

    def set(self, min, max):
        assert max > min

        self.min = min
        self.max = max
        self.length = max - min
        self.is_initialized = True


class MinMaxNormalizer(Normalizer):
    def __init__(self, data):
        super().__init__(data)
        self.range = MinMaxTargetRange()
    
    def __normalize(self,data):
        self.length[self.length == 0] = 1  # 防止全为某一常数
        # (b - a)(x - min)/(max - min) + a
        return (data - self.min) * self.range.length / self.length + self.range.min

    def normalize(self, data=None):
        if not self.has_set_range:
            raise RuntimeError("MinMax标准化需要指定映射范围")

        if data is None:
            if not hasattr(self, "normalized"):
                self.normalized = self.__normalize(self.original)
            return self.normalized
        return self.__normalize(data)

    @property
    def has_set_range(self):
        return self.range.is_initialized

    def set_range(self, min, max):
        self.range.set(min, max)
        return self


class RobustNormalizer(Normalizer):
    pass
