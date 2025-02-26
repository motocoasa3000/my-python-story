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

# House Prices
sns.displot(data['PRICE'],
            bins=50,aspect=2,
            kde=True,
            color='#2196f3')

plt.title(f'1970s Home Values in Boston. Average: ${(1000*data.PRICE.mean()):.6}')
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')

plt.show()

# Length of Commute
sns.displot(data.DIS,
            bins=50,
            aspect=2,
            kde=True,
            color='darkblue')
plt.title(f'Distance to Employment Centres. Average: {(data.DIS.mean()):.2}')
plt.xlabel('Weighted Distance to 5 Boston Employment Centres')
plt.ylabel('Nr. of Homes')

plt.show()

# Number of Rooms
sns.displot(data.RM,
            aspect=2,
            kde=True,
            color='#00796b')

plt.title(f'Distribution of Rooms in Boston. Average: {data.RM.mean():.2}')
plt.xlabel('Average Number of Rooms')
plt.ylabel('Nr. of Homes')

plt.show()

# Access to Highways
plt.figure(figsize=(10, 5), dpi=200)
plt.hist(
    data['RAD'],
    bins=24,
    ec='black',
    color='#7b1fa2',
    rwidth=0.5)

plt.xlabel('Accessibility to Highways')
plt.ylabel('Nr. of Houses')
plt.show()


# Bar chart with plotly for CHAS to show many more homes are away from the river versus next to it

river_access = data['CHAS'].value_counts()

bar = px.bar(x=['No', 'Yes'],
             y=river_access.values,
             color_continuous_scale=px.colors.sequential.haline,
             title='Next to Charles River?')

bar.update_layout(xaxis_title='Property Located Next to the River?',
                  yaxis_title='Number of Homes',
                  coloraxis_showscale=False)
bar.show()


# Understanding the relationship in data

sns.pairplot(data)
plt.show()


# Compare DIS (Distance from employment) with NOX (Nitric Oxide Pollution) using Seaborn's `.jointplot()`.

with sns.axes_style('darkgrid'):
    sns.jointplot(x=data['DIS'],
                  y=data['NOX'],
                  height=8,
                  kind='scatter',
                  color='darkred',
                  joint_kws={'alpha':0.5})

plt.show()


# Proportion of Non-Retail Industry vs Pollution
# Compare INDUS (the proportion of non-retail industry i.e., factories)
# with NOX (Nitric Oxide Pollution) using Seaborn's `.jointplot()`.

with sns.axes_style('darkgrid'):
    sns.jointplot(x=data.NOX,
                  y=data.INDUS,
                  # kind='hex',
                  height=7,
                  color='darkgreen',
                  joint_kws={'alpha':0.5})
plt.show()


# Split Training & Test Dataset

target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size=0.2,
                                                    random_state=10)

# % of training set
train_pct = 100*len(X_train)/len(features)
print(f'Training data os {train_pct:.3}% of the total data.')

# % of test data set
test_pct = 100*X_test.shape[0]/features.shape[0]
print(f'Test data makes up the remaining {test_pct:0.3}%.')


# Multivariable Regression
# Run First Regression

regr = LinearRegression()
regr.fit(X_train, y_train)
rsquared = regr.score(X_train, y_train)

print(f'Training data r-squared: {rsquared:.2}')

# Evaluate the Coefficients of the Model

regr_coef = pd.DataFrame(data=regr.coef_, index=X_train.columns, columns=['Coefficient'])
regr_coef

# Premium for having an extra room
premium = regr_coef.loc['RM'].values[0] * 1000 # i.e., ~3.11 * 1000
print(f'The price premium for having an extra room is ${premium:.5}')


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
