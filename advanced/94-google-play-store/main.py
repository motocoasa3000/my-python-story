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
