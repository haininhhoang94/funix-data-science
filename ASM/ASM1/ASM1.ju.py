# %%
# find EUR/USD data
import pandas as pd
import numpy as np

import yfinance as yf
# %%
ticker = "EURUSD=X"
data = yf.download(tickers=ticker, period="730d", interval="1d")
data=pd.DataFrame(data)
data
# %%
data.describe()
# %%
data.isnull().any()
# %%
# Replace NaN data by either
# To drop row with NaN
# data.dropna(inplace=True)
# To fill data with NaN using mean, in order to preserve
# our stationary for ARIMA model
# data.fillna(data.mean(), inplace=True)
type(data)
# %%
# Draw histogram for Adj Close
import seaborn as sns
import matplotlib.pyplot as plt
# Create a sample dataset
# Draw histogram using Seaborn
sns.displot(data=pd.to_numeric(data['Close']), kde=False, bins=5)
# Show the plot
plt.show()
