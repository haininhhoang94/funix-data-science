# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# %%
# Q20:
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df1 = df.iloc[:, 0:2]
df2 = df.iloc[:, 2:4]
pd.concat([df1, df2], axis=1)
pd.concat([df1, df2], axis="columns")

# %%
# Q19
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["Date"] = pd.date_range(start="1/1/2024", periods=len(df), freq="D")
df["Date_text"] = df["Date"].dt.strftime("%m/%d/%Y")
# df["Date_converted"] = pd.to_datetime(df["Date_text"])
# df["Date_converted"] = df["Date"].apply(pd.to_datetime)
df["Date_converted"] = df["Date"].astype("datetime64[ns]")
# %%
# Q18
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df.iloc[:, 1].isnull()

# %%
# Q16
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# df.columns = df.columns.astype(str)
df.columns = df.columns.map(str)
df
# %%
# Q14
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df.iloc[:, 0].astype(int) + 2
# %%
# Q13
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["Date"] = pd.date_range(start="1/1/2024", periods=len(df), freq="D")
df["Day"] = df["Date"].dt.day
df
# %%
# Q10
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df.corr()

# %%
# Q9
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df.drop_duplicates()


# %%
# Q8
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
len(df["sepal length (cm)"].unique()) == df["sepal length (cm)"].nunique()
# %%
pd.read_csv(index_col=)