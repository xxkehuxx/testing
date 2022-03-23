import pandas as pd
import numpy as np

df = pd.read_excel('data/123.xls')

df.columns = ['date', 'dateop', 'cardnum', 'status','sumop','currency', 'sumpaid', 'currency', 'cashback', 'category', 'mss', 'descr', 'bonus', 'investkop', 'totalop']

df['date'] = pd.to_datetime(df['date'])
df['dateop'] = pd.to_datetime(df['dateop'])

df = df[df['status'] == 'OK']
df['group'] = np.where(df['sumop'] > 0, 'earned', 'spent')

df.drop('currency', axis = 1, inplace=True)
df.drop('dateop', axis = 1, inplace = True)
expenses = df.groupby('descr').agg(['sum','count'])['sumop'].sort_values('sum',ascending=False)
categories = df[df['group'] == 'spent'].groupby('category').aggregate(['sum','count'])['sumop']
categories.sort_values('sum', inplace = True)

daily_exp = ['Супермаркеты', 'Сервис. услуги' , 'Одежда, обувь' , 'Разные товары', 'Фастфуд', 'Развлечения']
df_daily = df[df['category'].isin(daily_exp)]
df_daily.index = df_daily['date']
for index, i in df_daily.groupby(by=df_daily.index.month):
    print(index)
    print(i.sum()['sumop'])