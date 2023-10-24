# %% [markdown]
"""
# Lab 3.1. Tạo bảng, chèn và truy vấn dữ liệu
"""

# %% [markdown]
"""
Đầu tiên chúng ta phải mở cmd lên và chạy các lệnh sau

- pip install pandas
- pip install pymysql
- pip install ipython-sql
- pip install "mysqlclient==1.3.12"

Lưu ý để không phát sinh lỗi trong quá trình cài đặt, bài Lab đang được cài đặt ở môi trường window và với phiên bản python là python 3.6.8 (các lab 3.1, 3.2, 3.3).

Sau khi cài đặt xong, chúng ta sẽ tiến hành import thư viện pymysql.
"""
# %%
# import pymysql
from sqlalchemy import create_engine
import pandas as pd

# %% [markdown]
"""
Lưu ý là đầu tiên để thực hiện Lab chúng ta phải tiến hành mở dịch vụ MySql và Apache trong XAMPP.

Để có thể kết nối Database ta sẽ phải có tài khoản truy cập, ta sẽ lấy tài khoản truy cập bằng cách chọn vào tab "Các tài khoản người dùng" trong trong phpMyAdmin. Ở ví dụ dưới chúng ta đang sử dụng tài khoản với username là root và không có password.
"""

# %%
# NOTE: there is a warning that we shouldn't use pymysql. Let's use sqlalchemy
# conn = pymysql.connect(
#     host="localhost", port=int(3306), user="root", passwd="", db="hr"
# )
# df = pd.read_sql_query("SELECT * FROM EMPLOYEES ", conn)
engine = create_engine("mysql+mysqldb://root@localhost:3306/hr")
df = pd.read_sql_query("SELECT * FROM EMPLOYEES ", engine)
df

# %%
