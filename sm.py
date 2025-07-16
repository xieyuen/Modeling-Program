from statsmodels import api as sm
import pandas as pd
from lib.constants import Index
from lib.tools import remove_na


data = pd.read_excel("./data/data.xlsx")
remove_na(data)


model = sm.OLS(
    data[Index.WATER_RESOURSE],
    sm.add_constant(data[Index.X_]),
).fit()

print(model.summary())
