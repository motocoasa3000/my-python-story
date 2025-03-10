import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


pd.options.display.flat_format = '{:,.2f'.format(
    df_data = pd_read_csv('nobel_prize_data.csv')
)
df.data.shape
df_data.head()
df_data.tail()
print(f'Any duplicates? {df_data.duplicated().values.any()}')
print(f'Any NaN values among the data? {df_data.isna().values.any()}')
df_data.isna().sum()
