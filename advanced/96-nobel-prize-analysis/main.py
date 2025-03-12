import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('nobel_prize_data.csv')
df_data.shape
df_data.head()
df_data.tail()
print(f'Any duplicates? {df_data.duplicated().values.any()}')
print(f'Any NaN values among the data? {df_data.isna().values.any()}')
df_data.isna().sum()

# NaN values for birthdate are all organisations
col_subset = ['year', 'category', 'laureate_type',
              'birth_date', 'full_name', 'organization_name']
df_data.loc[df_data.birth_date.isna()][col_subset]

# NaN values for organisation_name
col_subset = ['year', 'category', 'laureate_type', 'full_name', 'organization_name']
df_data.loc[df_data.organization_name.isna()][col_subset]

df_data.birth_date = pd.to_datetime(df_data.birth_date)

separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denomenator

df_data.info()


biology = df_data.sex.value_counts()
fig = px.pie(labels=biology.index,
             values=biology.values,
             title="Percentage of Male vs. Female Winners",
             names=biology.index,
             hole=0.4)

fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
fig.show()

df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]

is_winner = df_data.duplicated(subset=['full_name'], keep=False)
multiple_winners = df_data[is_winner]
print(f'There are {multiple_winners.full_name.nunique()}' \
      ' winners who were awarded the prize more than once.')


# Alternative:
multiple_winners = df_data.groupby(by = 'full_name').filter(lambda x : x['year'].count() >= 2)

col_subset = ['year', 'category', 'laureate_type', 'fullname']
# multiple_winners[col_subset]

# Number of different categories
df_data.category.nunique()

prizes_per_category = df_data.category.value_counts()
v_bar = px.bar(
    x = prizes_per_category.index,
    y = prizes_per_category.values,
    color = prizes_per_category.values,
    color_continuous_scale='pubugn',
    title='Number of Prizes Awarded per Category'
)

v_bar.update_layout(xaxis_title="Nobel Prize Category",
                    coloraxis_showscale=False,
                    yaxis_title='Number of Prizes')
v_bar.show()

df_data[df_data.category == 'Economics'].sort_values('year')[:3]

cat_men_women = df_data.groupby(['category', 'sex'],
                                as_index=False).agg({'prize': pd.Series.count})
cat_men_women.sort_values('prize', ascending=False, inplace=True)
cat_men_women

v_bar_split = px.bar(x = cat_men_women.category,
                     y = cat_men_women.prize,
                     color = cat_men_women.sex,
                     title='Number of Prizes Awarded per Category split by Men and Women')

v_bar_split.update_layout(xaxis_title='Nobel Prize Category',
                          yaxis_title='Number of Prizes')

v_bar_split.show()
