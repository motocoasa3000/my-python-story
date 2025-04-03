import pandas as pd
import matplotlib.dates as mdates

# Notebook Presentation
pd.options.display.float_format = '{:,.2f'.format

# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# Register date converters to avoid warning messages
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read the Data
df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
df_monthly = pd.read_csv('monthly_deaths.csv',
                         parse_dates=['date'])

# Preliminary Data Exploration
print(df_yearly.shape)
df_yearly

print(df_monthly.shape)
df_monthly

# Check for Nan and Duplicates
df_yearly.info()
df_monthly.info()
