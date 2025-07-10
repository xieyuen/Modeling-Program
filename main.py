import warnings

import pandas as pd
from sklearn.linear_model import LinearRegression

import tools
from constants import Title


def main():
    data = pd.read_excel("./data/data.xlsx")

    tools.remove_na(data)

    y = data[Title.WATER_RESOURSE]
    x = data[Title.X_]

    model = LinearRegression()

    model.fit(x, y)

    print("变量:",*x.columns.values)
    print("回归系数:", *model.coef_)
    print(f"截距: {model.intercept_}")
    print(f"决定R方: {model.score(x, y)}")
    print(f"调整R方: {tools.adjusted_r_squared(model, x, y)}")
    print("P值:", *tools.p(model, x, y))



if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()
