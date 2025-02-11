import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


pd.options.display.float_format = '{:,.2f'.format

# Load Data
data = pd.read_csv('boston.csv', index_col=0)


# Preliminary data exploration
data.shape
data.columns

data.head()
data.tail()
data.count()

# Check Missing Values and Duplicates
data.info()
print(f'Any NaN values? {data.isna().values.any()}')
print(f'Any duplicates? {data.duplicated().values.any()}')


# Descriptive Statistics
data.describe()


# Visualise the Features
sns.displot(data['PRICE'],
            bins=50,aspect=2,
            kde=True,
            color='#2196f3')

plt.title(f'1970s Home Values in Boston. Average: ${(1000*data.PRICE.mean()):.6}')
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')

plt.show()


# predicted_values = regr.predict(X_train)
# residuals =(y_train = predicted_values)
#
# plt.figure(dpi=150)
# plt.scatter(data.PRICE, np.log(data.PRICE))
#
# plt.title('Mapping the Original Price to a Log Price')
# plt.ylabel('Log Price')
# plt.xlabel('Actual $ Price in 000s')
# plt.show()
#
# # Starting Point: Average Values in the Dataset
# features = data.drop(['PRICE'], axis=1)
# average_vals = features.mean().values
# property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)),
#                               columns=features.columns)
# property_stats
