import pandas as pd

df = pd.read_csv('C:/Users/user/Downloads/Telegram Desktop/moscow.csv/moscow-73519000437-79110366666.csv')
maxim = df[df['amount_charged'] == df['amount_charged'].max()]
print(maxim.