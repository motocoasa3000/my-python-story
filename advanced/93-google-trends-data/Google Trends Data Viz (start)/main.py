import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')


# Data Exploration

print(df_tesla.shape)
df_tesla.head()

print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')

df_tesla.describe()


# Unemployment Data

print(df_unemployment.shape)
df_unemployment.head()

print('Largest value for "Unemployment Benefits" '
      f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')


# Bitcoin

print(df_btc_price.shape)
df_btc_price.head()

print(df_btc_search.shape)
df_btc_search.head()

print(f'largest BTC News Search {df_btc_search.BTC_NEWS_SEARCH.max()}')


# Data Cleaning
# Check for Missing Values

print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')
print(f'Missing values? for BTC price?: {df_btc_price.isna().values.any()}')

print(f'Number of Missing Values: {df_btc_price.isna().values.sum()}')
df_btc_price[df_btc_price.CLOSE.isna()]

# removing any missing values
df_btc_price.dropna(inplace=True)

# Convert strings to DateTime Objects
type(df_tesla.MONTH[0])

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

df_tesla.MONTH.head()

# Converting from daily to monthly data
df_btc_monthly = df_btc_price.resample('ME', on='DATE').last()

print(df_btc_monthly.shape)
df_btc_monthly.head()


# Data Visualisation

# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# Register date converters to avoid warning messages
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Tesla Stock Price vs Search Volume

ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price', color=#E6232E)
ax2.set_ylabel('Search Trend', color=#87CEEB)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color=#E6232E)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH=color=#87CEEB)

