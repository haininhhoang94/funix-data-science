# %%
# Testing for subtraction in index
import pandas as pd

# Example Series
series1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
series2 = pd.Series([1, 2, 3, 4], index=["b", "c", "d", "e"])

# Subtracting Series
result = series1 - series2

print(result)

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    "Category": ["A", "B", "C", "D"],
    "Value1": [10, 15, 7, 12],
    "Value2": [5, 8, 6, 9],
}

# Create a DataFrame from the data
import pandas as pd

df = pd.DataFrame(data)

# Create a stacked column chart
plt.figure(figsize=(8, 6))

# Plot the first set of values (Value1)
sns.barplot(x="Category", y="Value1", data=df, color="b", label="Value1")

# Plot the second set of values (Value2) on top of the first
sns.barplot(
    x="Category", y="Value2", data=df, color="r", bottom=df["Value1"], label="Value2"
)

plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Stacked Column Chart Example")
plt.legend()

plt.show()

# %%
