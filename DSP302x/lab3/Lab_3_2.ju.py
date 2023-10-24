# %% [markdown]
"""
# Lab 3.2
"""

# %% [markdown]
"""
# Truy cập cơ sở dữ liệu với SQL Magic

Ước tính thời gian cần thiết: **15** phút

## Mục tiêu

Sau khi hoàn thành bài Lab này, bạn sẽ có thể:

-   Truy cập cơ sở dữ liệu bằng SQL "magic" theo cách đơn giản hơn.

"""

# %% [markdown]
"""
Để giao tiếp với Cơ sở dữ liệu SQL từ bên trong JupyterLab notebook, chúng ta có thể sử dụng SQL "magic" của extension (tiện ích mở rộng) [ipython-sql](https://github.com/catherinedevlin/ipython-sql). "Magic" là thuật ngữ của JupyterLab cho những lệnh đặc biệt bắt đầu với dấu "%". Ở bên dưới, chúng ta sẽ dùng _load___ext_ magic để tải extension ipython-sql. Thư viện mysqlclient và ipython-sql đã được cài đặt trước ở Lab 3.1

"""

# %% [markdown]
"""
Bây giờ, chúng ta sẽ dùng lệnh SQL magic đầu tiên để kết nối với cơ sở dữ liệu hr mà chúng ta đã tạo ở các Lab trước đó. Chúng ta sẽ sử dụng tài khoản truy cập Database như ở Lap 3.1. Cú pháp khi kết nối Database sử dụng sql magic sẽ là:

%sql mysql://[user]:[password]@localhost/[dataBase]
"""

# %% [markdown]
"""
Một số gói thư viện chúng ta cần cài đặt thêm như sau:

- pip install seaborn
- pip install matplotlib
"""

# %%
# !pip install ipython-sql
# %load_ext sql
# %sql mysql://root:@localhost:3306/hr

# %% [markdown]
"""
Dưới đây chúng ta sẽ tạo một bảng và điền một số dữ liệu kiểm thử vào bảng để thử nghiệm.
"""

# %%
# # NOTE: comment this when not running
# # %%sql
#
# CREATE TABLE INTERNATIONAL_STUDENT_TEST_SCORES (
#     country VARCHAR(50),
#     first_name VARCHAR(50),
#     last_name VARCHAR(50),
#     test_score INT
# );
# INSERT INTO INTERNATIONAL_STUDENT_TEST_SCORES (country, first_name, last_name, test_score)
# VALUES
# ('United States', 'Marshall', 'Bernadot', 54),
# ('Ghana', 'Celinda', 'Malkin', 51),
# ('Ukraine', 'Guillermo', 'Furze', 53),
# ('Greece', 'Aharon', 'Tunnow', 48),
# ('Russia', 'Bail', 'Goodwin', 46),
# ('Poland', 'Cole', 'Winteringham', 49),
# ('Sweden', 'Emlyn', 'Erricker', 55),
# ('Russia', 'Cathee', 'Sivewright', 49),
# ('China', 'Barny', 'Ingerson', 57),
# ('Uganda', 'Sharla', 'Papaccio', 55),
# ('China', 'Stella', 'Youens', 51),
# ('Poland', 'Julio', 'Buesden', 48),
# ('United States', 'Tiffie', 'Cosely', 58),
# ('Poland', 'Auroora', 'Stiffell', 45),
# ('China', 'Clarita', 'Huet', 52),
# ('Poland', 'Shannon', 'Goulden', 45),
# ('Philippines', 'Emylee', 'Privost', 50),
# ('France', 'Madelina', 'Burk', 49),
# ('China', 'Saunderson', 'Root', 58),
# ('Indonesia', 'Bo', 'Waring', 55),
# ('China', 'Hollis', 'Domotor', 45),
# ('Russia', 'Robbie', 'Collip', 46),
# ('Philippines', 'Davon', 'Donisi', 46),
# ('China', 'Cristabel', 'Radeliffe', 48),
# ('China', 'Wallis', 'Bartleet', 58),
# ('Moldova', 'Arleen', 'Stailey', 38),
# ('Ireland', 'Mendel', 'Grumble', 58),
# ('China', 'Sallyann', 'Exley', 51),
# ('Mexico', 'Kain', 'Swaite', 46),
# ('Indonesia', 'Alonso', 'Bulteel', 45),
# ('Armenia', 'Anatol', 'Tankus', 51),
# ('Indonesia', 'Coralyn', 'Dawkins', 48),
# ('China', 'Deanne', 'Edwinson', 45),
# ('China', 'Georgiana', 'Epple', 51),
# ('Portugal', 'Bartlet', 'Breese', 56),
# ('Azerbaijan', 'Idalina', 'Lukash', 50),
# ('France', 'Livvie', 'Flory', 54),
# ('Malaysia', 'Nonie', 'Borit', 48),
# ('Indonesia', 'Clio', 'Mugg', 47),
# ('Brazil', 'Westley', 'Measor', 48),
# ('Philippines', 'Katrinka', 'Sibbert', 51),
# ('Poland', 'Valentia', 'Mounch', 50),
# ('Norway', 'Sheilah', 'Hedditch', 53),
# ('Papua New Guinea', 'Itch', 'Jubb', 50),
# ('Latvia', 'Stesha', 'Garnson', 53),
# ('Canada', 'Cristionna', 'Wadmore', 46),
# ('China', 'Lianna', 'Gatward', 43),
# ('Guatemala', 'Tanney', 'Vials', 48),
# ('France', 'Alma', 'Zavittieri', 44),
# ('China', 'Alvira', 'Tamas', 50),
# ('United States', 'Shanon', 'Peres', 45),
# ('Sweden', 'Maisey', 'Lynas', 53),
# ('Indonesia', 'Kip', 'Hothersall', 46),
# ('China', 'Cash', 'Landis', 48),
# ('Panama', 'Kennith', 'Digance', 45),
# ('China', 'Ulberto', 'Riggeard', 48),
# ('Switzerland', 'Judy', 'Gilligan', 49),
# ('Philippines', 'Tod', 'Trevaskus', 52),
# ('Brazil', 'Herold', 'Heggs', 44),
# ('Latvia', 'Verney', 'Note', 50),
# ('Poland', 'Temp', 'Ribey', 50),
# ('China', 'Conroy', 'Egdal', 48),
# ('Japan', 'Gabie', 'Alessandone', 47),
# ('Ukraine', 'Devlen', 'Chaperlin', 54),
# ('France', 'Babbette', 'Turner', 51),
# ('Czech Republic', 'Virgil', 'Scotney', 52),
# ('Tajikistan', 'Zorina', 'Bedow', 49),
# ('China', 'Aidan', 'Rudeyeard', 50),
# ('Ireland', 'Saunder', 'MacLice', 48),
# ('France', 'Waly', 'Brunstan', 53),
# ('China', 'Gisele', 'Enns', 52),
# ('Peru', 'Mina', 'Winchester', 48),
# ('Japan', 'Torie', 'MacShirrie', 50),
# ('Russia', 'Benjamen', 'Kenford', 51),
# ('China', 'Etan', 'Burn', 53),
# ('Russia', 'Merralee', 'Chaperlin', 38),
# ('Indonesia', 'Lanny', 'Malam', 49),
# ('Canada', 'Wilhelm', 'Deeprose', 54),
# ('Czech Republic', 'Lari', 'Hillhouse', 48),
# ('China', 'Ossie', 'Woodley', 52),
# ('Macedonia', 'April', 'Tyer', 50),
# ('Vietnam', 'Madelon', 'Dansey', 53),
# ('Ukraine', 'Korella', 'McNamee', 52),
# ('Jamaica', 'Linnea', 'Cannam', 43),
# ('China', 'Mart', 'Coling', 52),
# ('Indonesia', 'Marna', 'Causbey', 47),
# ('China', 'Berni', 'Daintier', 55),
# ('Poland', 'Cynthia', 'Hassell', 49),
# ('Canada', 'Carma', 'Schule', 49),
# ('Indonesia', 'Malia', 'Blight', 48),
# ('China', 'Paulo', 'Seivertsen', 47),
# ('Niger', 'Kaylee', 'Hearley', 54),
# ('Japan', 'Maure', 'Jandak', 46),
# ('Argentina', 'Foss', 'Feavers', 45),
# ('Venezuela', 'Ron', 'Leggitt', 60),
# ('Russia', 'Flint', 'Gokes', 40),
# ('China', 'Linet', 'Conelly', 52),
# ('Philippines', 'Nikolas', 'Birtwell', 57),
# ('Australia', 'Eduard', 'Leipelt', 53)
#
#
#
# %% [markdown]
"""
#### Sử dụng các biến Python trong các câu lệnh SQL 

Bạn có thể sử dụng biến python trong câu lệnh SQL bằng cách thêm tiền tố ":" vào tên biến python.

Ví dụ: nếu chúng ta có biến python `country` với giá trị là` "Canada" `, chúng ta có thể sử dụng biến này trong truy vấn SQL để tìm tất cả các hàng sinh viên đến từ Canada.

"""

# %%
# Using Python variable in Jupyter with magic command
country = "Canada"
# %sql select * from INTERNATIONAL_STUDENT_TEST_SCORES where country = :country

# %% [markdown]
"""
#### Gán kết quả của các truy vấn cho các biến Python
"""

# %% [markdown]
"""
Bạn có thể sử dụng cú pháp gán python thông thường để gán kết quả truy vấn cho các biến python.

Ví dụ: tôi có một truy vấn SQL để truy xuất phân phối điểm kiểm tra (tức là số lượng sinh viên đạt được mỗi điểm nhất định). Tôi có thể gán kết quả của truy vấn này cho biến `test_score_distribution` bằng cách dùng toán tử` = `.
"""

# %%
# NOTE: comment this when not running
# test_score_distribution = %sql SELECT test_score as 'Test Score', count(*) as 'Frequency' from INTERNATIONAL_STUDENT_TEST_SCORES GROUP BY test_score;
# test_score_distribution

# %% [markdown]
"""
#### Chuyển đổi kết quả truy vấn thành Khung dữ liệu
"""

# %% [markdown]
"""
Bạn có thể dễ dàng chuyển đổi kết quả truy vấn SQL thành khung dữ liệu pandas bằng phương thức `DataFrame()`. Các đối tượng khung dữ liệu linh hoạt hơn nhiều so với các đối tượng kết quả truy vấn SQL. Ví dụ: chúng ta có thể dễ dàng vẽ biểu đồ phân phối điểm kiểm tra của mình sau khi chuyển đổi sang khung dữ liệu.
"""

# %%
dataframe = test_score_distribution.DataFrame()

# %matplotlib inline
# uncomment the following line if you get an module error saying seaborn not found
# !pip install seaborn
import seaborn

plot = seaborn.barplot(x='Test Score',y='Frequency', data=dataframe)

# %% [markdown]
"""
Bây giờ các bạn đã biết cách làm việc với sql trong Jupyter notebook bằng cách sử dụng SQL "magic"!
"""

