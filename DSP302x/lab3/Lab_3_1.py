# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] id="5fpJa_3bk3cb"
# # Lab 3.1. Tạo bảng, chèn và truy vấn dữ liệu

# %% [markdown] id="SyoiqjiWk3ch"
# Đầu tiên chúng ta phải mở cmd lên và chạy các lệnh sau
#
# - pip install pandas
# - pip install pymysql
# - pip install ipython-sql
# - pip install "mysqlclient==1.3.12"
#
# Lưu ý để không phát sinh lỗi trong quá trình cài đặt, bài Lab đang được cài đặt ở môi trường window và với phiên bản python là python 3.6.8 (các lab 3.1, 3.2, 3.3).
#
# Sau khi cài đặt xong, chúng ta sẽ tiến hành import thư viện pymysql.

# %% id="UtDPdfFSk3ci"
import pymysql
import pandas as pd

# %% id="LBM_jfNrdvm2"

# %% [markdown] id="uLs54hJ1k3ck"
# Lưu ý là đầu tiên để thực hiện Lab chúng ta phải tiến hành mở dịch vụ MySql và Apache trong XAMPP.
#
# Để có thể kết nối Database ta sẽ phải có tài khoản truy cập, ta sẽ lấy tài khoản truy cập bằng cách chọn vào tab "Các tài khoản người dùng" trong trong phpMyAdmin. Ở ví dụ dưới chúng ta đang sử dụng tài khoản với username là root và không có password.

# %% id="frR5Kkeak3ck" outputId="1d8e2531-c923-491a-9528-7f7e139eb8d9"
import pymysql
import pandas as pd

conn=pymysql.connect(host='localhost',port=int(3306),user='root',passwd='',db='hr')

df=pd.read_sql_query("SELECT * FROM EMPLOYEES ",conn)
df

# %% id="Erwdaokmk3cm"
