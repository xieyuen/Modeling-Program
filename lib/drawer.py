import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from constants import Index, Label


class Drawer:
    def __init__(self, data, threeD=False):
        self.data = data
        if threeD:
            self.fig = plt.figure()
            self.ax = self.fig.add_axes(Axes3D(self.fig))

    def rain(self):
        plt.scatter(
            self.data[Index.RAIN],
            self.data[Index.Y],
        )
        plt.title(f"{Label.RAIN} vs {Label.WATER_RESOURSE}")
        plt.xlabel(Label.RAIN)
        return self

    def temp(self):
        plt.scatter(
            self.data[Index.TEMP],
            self.data[Index.Y],
        )
        plt.title(f"{Label.TEMP} vs {Label.WATER_RESOURSE}")
        plt.xlabel(Label.TEMP)
        return self

    def hum(self):
        plt.scatter(
            self.data[Index.HUM],
            self.data[Index.Y],
        )
        plt.title(f"{Label.HUM} vs {Label.WATER_RESOURSE}")
        plt.xlabel(Label.HUM)
        return self

    def time(self):
        plt.scatter(
            self.data[Index.TIME],
            self.data[Index.Y],
        )
        plt.title(f"{Label.TIME} vs {Label.WATER_RESOURSE}")
        plt.xlabel(Label.TIME)
        return self

    def rain_and_time(self):
        self.ax.scatter(
            self.data[Index.RAIN],
            self.data[Index.TIME],
            self.data[Index.WATER_RESOURSE],
            label="original data",
        )
        return self

    def experience_rain_time(self, exp, color="red"):
        x1 = np.linspace(
            self.data[Index.RAIN].min(),
            self.data[Index.RAIN].max(),
        )
        x2 = np.linspace(
            self.data[Index.TIME].min(),
            self.data[Index.TIME].max(),
        )
        X1, X2 = np.meshgrid(x1, x2)
        Y = exp(X1, X2)
        self.ax.plot_surface(
            X1, X2, Y,
            color=color,
            label="experience",
        )
        return self

    def show(self):
        plt.ylabel(Label.WATER_RESOURSE)
        plt.show()

    def show_3d(self):
        self.ax.set_zlabel(Label.WATER_RESOURSE, {"size": 15, "color": "red"})
        self.ax.set_ylabel(Label.RAIN, {"size": 15, "color": "red"})
        self.ax.set_xlabel(Label.TIME, {"size": 15, "color": "red"})
        self.ax.legend()
        plt.show()
