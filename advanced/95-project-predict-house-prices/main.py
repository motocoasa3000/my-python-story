import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.sphinxext.mathmpl import fontset_choice
from pandas.errors import PerformanceWarning

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
            bins=50, aspect=2,
            kde=True,
            color='#2196f3')

plt.title(f'1970s Home Values in Boston. Average: ${(1000 * data.PRICE.mean()):.6}')
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
                  joint_kws={'alpha': 0.5})

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
                  joint_kws={'alpha': 0.5})
plt.show()

# Split Training & Test Dataset

target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size=0.2,
                                                    random_state=10)

# % of training set
train_pct = 100 * len(X_train) / len(features)
print(f'Training data os {train_pct:.3}% of the total data.')

# % of test data set
test_pct = 100 * X_test.shape[0] / features.shape[0]
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
premium = regr_coef.loc['RM'].values[0] * 1000  # i.e., ~3.11 * 1000
print(f'The price premium for having an extra room is ${premium:.5}')

# Analyse the estimated values & regression residuals
# Create 2 scatter plots
predicted_vals = regr.predict(X_train)
residuals = (y_train - predicted_vals)

# Original Regression of Actual vs. Predicted Prices
plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices: $y_i$ vs $\hat y_i$', fontsize=18)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Predicted prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.figure(dpi=100)
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=18)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=15)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residual Distribution Chart
resid_mean = round(residuals.mean(), 2)
resid_skew = round(residuals.skew(), 2)

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Residuals Skew ({resid_skew} Mean ({resid_mean})')
plt.show()

# Data transformations for a better fit
tgt_skew = data['PRICE'].skew()
sns.displot(data['PRICE'], kde='kde', color='green')
plt.title(f'Normal Prices. Skew is {tgt_skew:.3}')
plt.show()

y_log = np.log(data['PRICE'])
sns.displot(y_log, kde=True)
plt.title(f'Log Prices. Skew is {y_log.skew():.3}')
plt.show()

# Log transformation
plt.figure(dpi=150)
plt.scatter(data.PRICE, np.log(data.PRICE))

plt.title('Mapping the Original Price to a Log Price')
plt.ylabel('Log Price')
plt.xlabel('Actual $ Price in 000s')
plt.show()

# Regression using Log Prices

new_target = np.log(data['PRICE'])  # use log prices
features = data.drop("PRICE", axis=1)

X_train, X_test, log_y_train, log_y_test = train_test_split(features,
                                                            new_target,
                                                            test_size=0.2,
                                                            random_state=10)
log_regr = LinearRegression()
log_regr.fit(X_train, log_y_train)
log_rsquared = log_regr.score(X_train, log_y_train)
log_predictions = log_regr.predict(X_train)
log_residuals = (log_y_train - log_predictions)

print(f'Training data r-squared: {log_rsquared:.2}')

# Evaluating Coefficients with Log Prices

df_coef = pd.DataFrame(data=log_regr.coef_, index=X_train.columns, columns=['coef'])
df_coef

# Regression with Log Prices & Residual Plots

# Graph of Actual vs Predicted Log Prices
plt.scatter(x=log_y_train, y=log_predictions, c='navy', alpha=0.6)
plt.plot(log_y_train, log_y_train, color='cyan')
plt.title(f'Actual vs Predicted Log Prices: $y _i$ vs $\hat y_i$ (R-Squared {log_rsquared:.2})', fontsize=17)
plt.xlabel('Actual Log Prices $y _i$', fontsize=14)
plt.ylabel('Predicted Log Prices $\hat y_i$', fontsize=14)
plt.show()

# Original Regression of Actual vs Predicted Prices
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Original Actual vs Predicted Prices: $y _i$ vs $\hat y_i$ (R-Squared {rsquared:.3})', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Predicted prices 000s $\hat _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values (Log prices)
plt.scatter(x=log_predictions, y=log_residuals, c='navy', alpha=0.6)
plt.title('Residuals vs Fitted Values for Log Prices', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Original Residuals vs Fitted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Distribution of Residuals (log prices) - checking for normality
log_resid_mean = round(log_residuals.mean(), 2)
log_resid_skew = round(log_residuals.skew(), 2)

sns.displot(log_residuals, kde=True, color='navy')
plt.title(f'Log price model: Residuals Skew ({log_resid_skew}) Mean ({log_resid_mean}')
plt.show()

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Original model: Residuals Skew ({resid_skew}) Mean ({resid_mean}')
plt.show()


# Compare Out of Sample PerformanceWarning
print(f'Original Model Test Data r-sqared: {regr.score(X_test, y_test):.2}')
print(f'Log Model Test Data r-squared: {log_regr.score(X_test, log_y_test):.2}')


# Predict a Property's Value using the Regression Coefficients

# Starting Point: average values in the dataset
features = data.drop(['PRICE'], axis=1)
average_vals = features.mean().values
property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)),
                              columns=features.columns)
property_stats

# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Concert log prices to actual dollar values
dollar_est = np.e**log_estimate * 1000
# or use
dollar_est = np.exp(log_estimate) * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')

# Define Property Characteristics
next_to_river = True
nr_rooms = 8
students_per_classroom = 20
distance_to_town = 5
pollution = data.NOX.quantile(q=0.75) # high
amount_of_poverty = data.LSTAT.quantile(q=0.25) # low

# Solution
# Set Property Characteristics
property_stats['RM'] = nr_rooms
property_stats['PTRATIO'] = students_per_classroom
property_stats['DIS'] = distance_to_town

if next_to_river:
    property_stats['CHAS'] = 1
else:
    property_stats['CHAS'] = 0

property_stats['NOX'] = pollution
property_stats['LSTAT'] = amount_of_poverty

# Make Prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Actual dollar values
dollar_est = np.e**log_estimate * 1000
print(f'The property is estimate to be worth ${dollar_est:.6}')
