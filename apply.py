import pickle
from typing import Literal

import pandas as pd

from lib.constants import CityName, Index
from lib.nn.normal import NeuralNetwork as NorNN
from lib.nn.regularized import NeuralNetwork as RegNN


def load_model(path, model_type: Literal["lm", "nnn", "rnn"]):
    match model_type:
        case "lm":
            with open(path, "rb") as f:
                return pickle.load(f)
        case "nnn":
            return NorNN.load(path)
        case "rnn":
            return RegNN(path)
        case _:
            assert False, "不存在的模型类型"


def main():
    model = load_model("./model/LinearRegression/2_nostandard.pkl", "lm")

    data = pd.read_excel("./data/data.xlsx", CityName.BEI_JING)

    X = data[Index.X]
    y = data[Index.WATER_RESOURSE]

    print(model.predict(X), y)


if __name__ == "__main__":
    main()
