# 已经拟合过的模型

***使用方法***
```py
import pickle
def get_linear_model(path="linear/model/name.pkl"):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model

def get_nn_model(path):
    from modelinglib.nn.normal import NeuralNetwork
    return NeuralNetwork.load(path)

```

