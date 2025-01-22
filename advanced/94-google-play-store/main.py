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
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)

# highest grossing paid apps (ballpark estimate)
df_apps_clean['Revenue_estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
df_apps_clean.sort_values('Revenue_estimate', ascending=False)[:10]


# Plotly bar charts & scatter plots: analysing app categories
# number of different categories
df_apps_clean.Category.nunique()

# number of apps per category
top10_category = df_apps_clean.Category.value_counts()[:10]
top10_category


# Vertical Bar Chart - Highest Competition (Number of Apps)
bar = px.bar(
    x = top10_category.index, # index = category name
    y = top10_category.values)
bar.show()

# Horizontal Bar chart - most popular categories (highest downloads)
# group apps by category and then sum the number of installations
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

h_bar = px.bar(
    x = category_installs.Installs,
    y = category_installs.index,
    orientation='h',
    title='Category Popularity'
)

h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()


# Category Concentration - Downloads vs. Competition
# count the number of apps in each category
cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)

scatter = px.scatter(cat_merged_df,
                     x='App',
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))
scatter.show()


# Extracting Nested Data from a Column

# number of genres
len(df_apps_clean.Genres.unique())

# Problem: Have multiple categories seperated by ;
df_apps_clean.Genres.value_counts().sort_values(ascending=True)[:5]

# split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

bar = px.bar(
    x = num_genres.index[:15], # index = category name
    y = num_genres.values[:15], # count
    title='Top Genres',
    hover_name=num_genres.index[:15],
    color=num_genres.values[:15],
    color_continuous_scale='Agsunset'
)

bar.update_layout(xaxis_title='Genre',
                  yaxis_title='Number of Apps',
                  coloraxis_showscale=False)

bar.show()


# Grouped Bar Charts: Free vs Paid Apps per Category

df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"],
                                        as_index=False).agg({'App': pd.Series.count})
df_free_vs_paid.sort_values('App')

g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')

g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder':'total descending'},
                    yaxis=dict(type='log'),)

g_bar.show()