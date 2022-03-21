import pandas as pd
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
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

groups = newdf.groupby('name')[['name','square']]
for group, i in groups:
    print(group)
    print(i['square'].cumsum())
    plt.scatter(i.index, i['square'].cumsum())



for group, i in groups:
    plt.scatter(i['date'], i['square'])







