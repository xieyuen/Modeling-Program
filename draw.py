import pandas as pd
from lib.drawer import Drawer

data = pd.read_excel("./data/data.xlsx")

def scatter_2d():
    # 散点图
    drawer = Drawer(data)
    drawer.rain()  # 降雨量
    # drawer.hum()  # 湿度
    # drawer.temp()  # 温度
    # drawer.time()  # 日照时间
    drawer.show()

def scatter_3d():  # 三维散点图
    drawer = Drawer(data, True)
    drawer.rain_and_time()
    drawer.show_3d()

def exper_and_pred(exp):
    drawer = Drawer(data, True)
    drawer.experience_rain_time(exp).rain_and_time()
    drawer.show_3d()


if __name__ == "__main__":
    scatter_2d()
    # scatter_3d()
    # import pickle
    # with open("./model/LinearRegression/2_nostandard.pkl", "rb") as f:
    #     model = pickle.load(f)

    # def exp(x, y):
    #     return x * model.coef_[0] + y * model.coef_[1] + model.intercept_
    # exper_and_pred(exp)
