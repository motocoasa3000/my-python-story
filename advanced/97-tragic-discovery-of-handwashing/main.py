import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


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


# Alternative to using .info()
print(f'Any yearly NaN values? {df_monthly.isna().values.any()}')
print(f'Any monthly NaN values? {df_yearly.isna().values.any()}')

print(f'Any yearly duplicates? {df_yearly.duplicated().values.any()}')
print(f'Any monthly duplicates? {df_monthly.duplicated().values.any()}')

# Descriptive Statistics
df_yearly.describe()
df_monthly.describe()

# Percentage pf Women Dying in childbirth
prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')


# Visualise the Total Number of Births and Deaths over Time

# Plot the Monthly data on twin axes
plt.figure(figsize=(14,8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.grid(color='grey', linestyle='--')

ax1.plot(df_monthly.date,
         df_monthly.births,
         color='skyblue',
         linewidth=3)

ax2.plot(df_monthly.date,
         df_monthly.births,
         color='skyblue',
         linewidth=3)

ax2.plot(df_monthly.date,
         df_monthly.births,
         color='crimson',
         linewidth=2,
         linestyle='--')
plt.show()
