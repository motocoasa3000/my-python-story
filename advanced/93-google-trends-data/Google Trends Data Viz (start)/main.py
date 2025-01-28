import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

print(df_tesla.shape)
df_tesla.head()

print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')

df_tesla.describe()

print(df_unemployment.shape)
df_unemployment.head()

print('Largest value for "Unemployment Benefits" '
      f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')

print(df_btc_price.shape)
df_btc_price.head()

print(df_btc_search.shape)
df_btc_search.head()
