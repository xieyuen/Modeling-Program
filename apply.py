import warnings

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels import api as sm

from get_all_data import get
from modelinglib.constants import Index
from modelinglib import utils

warnings.filterwarnings("ignore")

VAR = [*Index.X_, Index.Y, Index.AREA, Index.USAGE, Index.STORAGE]

data = get("./data/data2.xlsx")[VAR]
utils.remove_na(data)

data[VAR] = (data[VAR] - data[VAR].mean()) / data[VAR].std()  # Z-Score Normalize

y = data[Index.Y]
x = data.drop(Index.Y, axis=1)

m2 = LinearRegression()
m2.fit(x, y)

utils.print_result_for_lm(m2, x ,y)

model = sm.OLS(y, sm.add_constant(x)).fit()
print(model.summary())
