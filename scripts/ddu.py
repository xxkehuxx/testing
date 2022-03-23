import pandas as pd
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

desired_width = 200
pd.set_option('display.width', desired_width)


df = pd.read_excel('data/123.xlsx')
df.columns
df.drop_duplicates(inplace = True)

newdf = df.dropna(axis=0, how='all')
pd.to_datetime(newdf.date)
newdf[['square', 'price']].astype('float')
newdf['date'] = newdf['date'].map(dt.datetime.toordinal)
newdf = newdf.set_index(newdf['date'])
newdf = newdf[newdf['type'] == 'Квартира']
# newdf.groupby(newdf.index)['name', 'square'].cumsum()

grouped = df.groupby(['date', 'name'])[['date','name','square']]
grouped = grouped.sum().reset_index()
zhk_first = grouped[grouped.name == 'Нагорная 7']
y = zhk_first.square.values
X = zhk_first.date.values
X = X.reshape(-1,1)
reg = LinearRegression()
reg = reg.fit(X,y)

# The coefficients
print("Coefficients: \n", reg.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y, ))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y, ))











