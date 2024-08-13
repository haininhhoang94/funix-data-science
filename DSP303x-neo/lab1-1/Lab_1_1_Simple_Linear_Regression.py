# %%
# # Hồi Quy Tuyến Tính Đơn Giản
#
# Thời lượng ước tính: **45** phút
#
# ## Mục tiêu
#
# Sau khi hoàn thành bài lab này bạn sẽ có thể:
#
# -   Sử dụng scikit-learn để triển khai Hồi Quy Tuyến Tính Đơn Giản
# -   Tạo một mô hình, huấn luyện, kiểm tra và sử dụng mô hình
#

# ### Import các gói cần thiết
#

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import seaborn as sns
import math
from sklearn.linear_model import LinearRegression

# ## Hiểu dữ liệu
#
# ### `FuelConsumption.csv`:
#
# Chúng tôi đã download tập dữ liệu tiêu thụ nhiên liệu **`FuelConsumption.csv`**, chứa xếp hạng mức tiêu thụ nhiên liệu cụ thể cho từng mẫu xe và lượng khí thải CO2 ước tính cho các loại xe hạng nhẹ bán lẻ mới ở Canada. [Nguồn tập dữ liệu](http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork-20718538&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork-20718538&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork-20718538&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork-20718538&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)
#
# -   **MODELYEAR** ví dụ: 2014
# -   **MAKE** ví dụ: Acura
# -   **MODEL** ví dụ: ILX
# -   **VEHICLE CLASS** ví dụ: SUV
# -   **ENGINE SIZE** ví dụ: 4.7
# -   **CYLINDERS** ví dụ: 6
# -   **TRANSMISSION** ví dụ: A6
# -   **FUEL CONSUMPTION in CITY(L/100 km)** ví dụ: 9.9
# -   **FUEL CONSUMPTION in HWY (L/100 km)** ví dụ: 8.9
# -   **FUEL CONSUMPTION COMB (L/100 km)** ví dụ: 9.2
# -   **CO2 EMISSIONS (g/km)** ví dụ: 182   --> low --> 0
#

# ## Đọc dữ liệu vào
#

df = pd.read_csv("./FuelConsumption.csv")

# ### Data Explantory
# Let's check the columns type
df.info()
# Let's split X and y
X_ = df.drop(columns=["CO2EMISSIONS"])
y_ = df["CO2EMISSIONS"]
# Let's split the columns into cat_vars and num_vars, and target
cat_vars = X_.select_dtypes(include=["object"]).columns
num_vars = X_.select_dtypes(exclude=["object"]).columns

# --------------------------------- Check n/a -------------------------------- #
percentage_na = X_.isna().sum()
# => There is no n/a

# plot histogram for num_vars
X_[num_vars].hist()
plt.tight_layout()
plt.show()


# Check scatter plot for num_vars
def v_scatter(X_, y_, var, ax):
    X_ = X_.copy()
    y_ = y_.copy()
    sns.scatterplot(x=X_[var], y=y_, ax=ax)


fig, axs = plt.subplots(
    ncols=2, nrows=math.ceil(len(num_vars) / 2), figsize=(10, 15)
)
axs = axs.flatten()
plt.tight_layout()
for i, var in enumerate(num_vars):
    v_scatter(X_, y_, var, axs[i])
plt.show()


# Since the scope of this lab is only EMISSION (y) vs ENGINESIZE(x)
# Train test split
def train_test_split(X_, y_, test_size=0.2):
    msk = np.random.rand(len(X_)) < (1 - test_size)
    X_train = X_[msk]
    X_test = X_[~msk]
    y_train = y_[msk]
    y_test = y_[~msk]
    return (X_train, X_test, y_train, y_test)


X_train, X_test, y_train, y_test = train_test_split(X_[["ENGINESIZE"]], y_)
