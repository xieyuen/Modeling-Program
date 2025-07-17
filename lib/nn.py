import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.exceptions import NotFittedError


class NeuralNetwork:
    def __init__(self, hidden_layers=(100, 50), max_iter=1000, random_state=42):
        """
        初始化神经网络回归模型
        
        Args:
            hidden_layers (tuple): 隐藏层神经元数量，例如(100,50)表示两层
            max_iter (int): 最大训练迭代次数
            random_state (int): 随机种子
        """
        self.model = MLPRegressor(
            hidden_layer_sizes=hidden_layers,
            activation='relu',
            solver='adam',
            max_iter=max_iter,
            random_state=random_state
        )
        self.scaler = StandardScaler()
        self.is_trained = False
        self.n_features_ = None  # 用于调整R²计算

    def train(self, X, y):
        """
        训练模型
        
        Args:
            X (array-like): 特征数据，形状 (n_samples, n_features)
            y (array-like): 目标值，形状 (n_samples,)
        """
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        self.n_features_ = X.shape[1]  # 存储特征数量

    def predict(self, X):
        """
        使用训练好的模型进行预测
        
        Args:
            X (array-like): 要预测的特征数据
            
        Returns:
            array: 预测结果
        """
        if not self.is_trained:
            raise NotFittedError("模型尚未训练，请先调用train()方法")
        return self.model.predict(self.scaler.transform(X))

    def evaluate(self, X, y):
        """
        评估模型性能
        
        Args:
            X (array-like): 测试特征数据
            y (array-like): 测试真实值
            
        Returns:
            dict: 包含R²、调整R²和RMSE的字典
        """
        if not self.is_trained:
            raise NotFittedError("模型尚未训练")

        y_pred = self.predict(X)
        n_samples = X.shape[0]

        # 计算基础指标
        r2 = r2_score(y, y_pred)
        rmse = np.sqrt(mean_squared_error(y, y_pred))

        # 计算调整R²
        adjusted_r2 = 1 - (1 - r2) * (n_samples - 1) / (n_samples - self.n_features_ - 1)

        return {
            'r2': r2,
            'adjusted_r2': adjusted_r2,
            'rmse': rmse,
            'n_samples': n_samples,
            'n_features': self.n_features_
        }

    def save(self, filename):
        """保存模型到文件"""
        import pickle
        with open(filename, 'wb') as f:
            pickle.dump({
                'model': self.model,
                'scaler': self.scaler,
                'is_trained': self.is_trained,
                'n_features': self.n_features_
            }, f)

    @classmethod
    def load(cls, filename):
        """从文件加载模型"""
        import pickle
        with open(filename, 'rb') as f:
            data = pickle.load(f)

        nn = cls()
        nn.model = data['model']
        nn.scaler = data['scaler']
        nn.is_trained = data['is_trained']
        nn.n_features_ = data['n_features']
        return nn
