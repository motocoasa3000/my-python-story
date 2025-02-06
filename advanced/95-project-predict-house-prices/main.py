import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


pd.options.display.float_format = '{:,.2f'.format

# Load Data
data = pd.read_csv('boston.csv', index_col=0)

predicted_values = regr.predict(X_train)

