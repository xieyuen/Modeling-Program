import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.exceptions import NotFittedError

class NeuralNetwork:
    def __init__(self, hidden_layers=(100, 50), max_iter=1000, random_state=42, 
                 alpha=0.0001, early_stopping=True):
        """
        初始化带正则化和早停的神经网络
        
        Args:
            hidden_layers (tuple): 隐藏层结构，如(100,50)表示两层
            max_iter (int): 最大迭代次数
            random_state (int): 随机种子
            alpha (float): L2正则化系数（默认0.0001）
            early_stopping (bool): 强制开启早停（默认True）
        """
        self.model = MLPRegressor(
            hidden_layer_sizes=hidden_layers,
            activation='relu',
            solver='adam',
            alpha=alpha,
            max_iter=max_iter,
            random_state=random_state,
            early_stopping=early_stopping,
            validation_fraction=0.1,  # 10%验证集
            n_iter_no_change=20  # 20轮无改进则停止
        )
        self.scaler = StandardScaler()
        self.is_trained = False

    def train(self, X, y):
        """训练模型并自动记录早停信息"""
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        self.best_iter_ = self.model.n_iter_  # 记录实际迭代次数
        self.loss_curve_ = self.model.loss_curve_  # 训练损失曲线

    def predict(self, X):
        """预测新数据"""
        if not self.is_trained:
            raise NotFittedError("请先调用train()方法训练模型")
        return self.model.predict(self.scaler.transform(X))

    def evaluate(self, X, y):
        """
        评估模型性能
        
        Returns:
            dict: {
                'r2': R平方,
                'rmse': 均方根误差,
                'n_iter': 实际迭代次数,
                'regularization': 当前L2系数
            }
        """
        if not self.is_trained:
            raise NotFittedError("模型未训练")
            
        y_pred = self.predict(X)
        return {
            'r2': r2_score(y, y_pred),
            'rmse': np.sqrt(mean_squared_error(y, y_pred)),
            'n_iter': self.best_iter_,
            'regularization': self.model.alpha
        }

    def set_regularization(self, alpha):
        """动态调整L2正则化强度"""
        self.model.set_params(alpha=alpha)
        if self.is_trained:
            print("警告：参数变更需重新训练模型")

    def save(self, filename):
        """保存模型到文件"""
        import pickle
        with open(filename, 'wb') as f:
            pickle.dump({
                'model': self.model,
                'scaler': self.scaler,
                'is_trained': self.is_trained,
                'best_iter': self.best_iter_
            }, f)

    @classmethod
    def load(cls, filename):
        """从文件加载模型"""
        import pickle
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        
        # 从加载的模型获取原始参数
        nn = cls(
            hidden_layers=data['model'].hidden_layer_sizes,
            alpha=data['model'].alpha
        )
        nn.model = data['model']
        nn.scaler = data['scaler']
        nn.is_trained = data['is_trained']
        nn.best_iter_ = data['best_iter']
        return nn
