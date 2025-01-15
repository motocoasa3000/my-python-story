import pandas as pd
import plotly.express as px


# Show numeric output in decimal format
pd.options.display.float_format = '{:,.2f}'.format

df_apps = pd.read_csv('apps.csv')
df_apps.shape
df_apps.head()
df_apps.sample(5)
df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)
df_apps.head()

# find and remove nan values in ratings
nan_rows = df_apps[df_apps.Rating.isna()]
print(nan_rows.shape)
nan_rows.head()
df_apps_clean = df_apps.dropna()
df_apps_clean.shape

# find and remove duplicates
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
duplicated_rows.head()
df_apps_clean = df_apps_clean.drop_duplicates()

# specify the subset for identifying duplicates
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
df_apps_clean[df_apps_clean.App == 'Instagram']
df_apps_clean.shape

# find the highest rated apps
df_apps_clean.sort_values('Rating', ascending=False).head()

# find 5 largest apps in terms of size (MBs)
df_apps_clean.sort_values('Size_MBs', ascending=False).head()

# find the 5 app with most reviews
df_apps_clean.sort_values('Reviews', ascending=False).head()

# plotly pie and donut charts - content ratings
ratings = df_apps_clean.Content_Rating.value_counts()


fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()
fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label')

fig.show()


# numeric type conversation: examine the number of installs
df_apps_clean.Installs.describe()
df_apps_clean.info()
# Installs of data type obj cause of the (,) character
df_apps_clean[['App', 'Installs']].groupby('Installs').count()

df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()


# Find the Most Expensive Apps, Filter out the Junk and Calculate a (ballpark) Sales Revenue estimate
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
# convert price to numeric data and investigate top 20 most expensive apps
df_apps_clean.sort_values('Price', ascending=False).head(20)

# the most expensive apps sub $250
df_apps_clean = df_apps_clean[df_app_clean['Price'] < 250]
df_apps_clean.sort_value('Price', ascending=False).head(5)

# highest grossing paid apps (ballpark estimate)
df_apps_clean['Revenue_estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]
