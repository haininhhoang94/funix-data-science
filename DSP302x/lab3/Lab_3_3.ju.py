# %% [markdown]
"""
# Phân tích tập dữ liệu thực tế với SQL và Python

Ước tính thời gian cần thiết: **15** phút

## Mục tiêu

Sau khi hoàn thành bài Lab này, bạn sẽ có thể:

-   Hiểu tập dữ liệu về các chỉ số kinh tế xã hội được chọn ở Chicago
-   Tìm hiểu cách lưu dữ liệu từ internet vào trong cơ sở dữ liệu
-   Giải quyết các bài toán ví dụ để thực hành kỹ năng SQL của bạn

"""

# %% [markdown]
"""
## Các chỉ số kinh tế xã hội được chọn ở Chicago

Thành phố Chicago đã phát hành tập dữ liệu kinh tế xã hội cho Cổng thông tin thành phố Chicago.
Bộ dữ liệu này chọn 6 chỉ số kinh tế xã hội có ý nghĩa đối với sức khỏe cộng đồng và “chỉ số khó khăn” cho từng khu vực cộng đồng ở Chicago trong những năm 2008 - 2012.

Scores on the hardship index can range from 1 to 100, with a higher index number representing a greater level of hardship.Điểm của chỉ số khó khăn là từ 1 đến 100, số càng cao thì thể hiện mức độ khó khăn càng lớn.

Bạn có thể xem mô tả chi tiết về tập dữ liệu trên [trang web của thành phố Chicago](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ), nhưng tóm lại, tập dữ liệu có các biến sau:

-   **Số khu vực cộng đồng** (`ca`): Dùng để xác định duy nhất từng hàng của tập dữ liệu

-   **Tên khu vực cộng đồng** (`community_area_name`): Tên vùng ở thành phố Chicago 

-   **Phần trăm nhà ở có đông người** (`percent_of_housing_crowded`): Phần trăm các đơn vị nhà ở có nhiều hơn một người trên một phòng

-   **Phần trăm hộ gia đình ở dưới mức nghèo** (`percent_households_below_poverty`): Phần trăm hộ gia đình sống ở dưới mức nghèo của liên bang

-   **Phần trăm thất nghiệp của những người từ 16 tuổi trở lên** (`percent_aged_16_unemployed`): Phần trăm số người trên 16 tuổi thất nghiệp

-   **Phần trăm số người từ 25 trở lên không có Bằng tốt nghiệp Cấp 3** (`percent_aged_25_without_high_school_diploma`): Phần trăm số người trên 25 tuổi không có tốt nghiệp cấp 3

-   **Phần trăm dân số** dưới 18 hoặc hơn 64 tuổi:Phần trăm dân số dưới 18 tuổi hoặc trên 64 tuổi (`percent_aged_under_18_or_over_64`): (tức là những người phụ thuộc)

-   **Thu nhập bình quân đầu người** (`per_capita_income_`): Thu nhập bình quân đầu người của Khu vực cộng đồng được ước tính bằng tổng thu nhập tổng hợp ở cấp khu vực chia cho tổng dân số

-   **Chỉ số khó khăn** (`hardship_index`): Điểm này kết hợp 6 chỉ số kinh tế xã hội đã chọn

Trong bài Lab này, chúng ta sẽ xem xét các biến trong tập dữ liệu chỉ số kinh tế xã hội và thực hiện một số phân tích cơ bản với Python.

"""

# %% [markdown]
"""
### Tạo cơ sở dữ liệu chicago trong trang quản lý phpMyadmin
"""

# %% [markdown]
"""
Ở Lap 2 chúng ta đã được thực hành tạo cơ sở dữ liệu, bây giờ chúng ta làm tương tự với Lap 2 để tạo cơ sở dữ liệu chicago
"""

# %% [markdown]
"""
### Kết nối với cơ sở dữ liệu

Đầu tiên, hãy tải extension SQL và thiết lập kết nối với cơ sở dữ liệu

"""

# %%
# %load_ext sql

# %%
# %sql mysql://root:@localhost/chicago

# %% [markdown]
"""
### Lưu tập dữ liệu trong Bảng

Trong nhiều trường hợp, tập dữ liệu cần phân tích sẽ ở dạng file .CSV (các giá trị được phân tách bằng dấu phẩy) trên internet. Để phân tích dữ liệu bằng SQL, trước tiên, dữ liệu cần được lưu trữ trong cơ sở dữ liệu.

Đầu tiên, chúng ta sẽ đọc nguồn tập dữ liệu .CSV từ internet vào khung dữ liệu pandas

Sau đó, chúng ta cần tạo một bảng trong cơ sở dữ liệu để lưu tập dữ liệu. Lệnh PERSIST trong SQL "magic" sẽ khiến quá trình tạo bảng và ghi dữ liệu từ khung dữ liệu `pandas` vào bảng đơn giản hơn

"""

# %%
import pandas

chicago_socioeconomic_data = pandas.read_csv(
    "https://data.cityofchicago.org/resource/jcxq-k9xf.csv"
)
# %sql --persist chicago_socioeconomic_data

# %% [markdown]
"""
#### Để xác minh rằng việc tạo bảng đã thành công, bạn có thể thực hiện một truy vấn cơ bản như:
"""

# %%
# %sql SELECT * FROM chicago_socioeconomic_data limit 5;

# %% [markdown]
"""
## Các bài toán

### Bài toán 1

#### Có bao nhiêu hàng trong tập dữ liệu?

"""

# %%
# # %%sql
# SELECT
#     COUNT(*)
# FROM
#     chicago.chicago_socioeconomic_data

# %% [markdown]
"""
<details><summary>Click vào đây để xem lời giải</summary>

```python
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;

Correct answer: 78
```

</details>

"""


# %% [markdown]
"""
### Bài toán 2

#### Có bao nhiêu khu vực cộng đồng ở Chicago có chỉ số khó khăn lớn hơn 50.0?

"""

# %%
# # %%sql
# SELECT
#     *
# FROM
#     chicago_socioeconomic_data
# WHERE
#     hardship_index > 50
# %% [markdown]
"""
<details><summary>Click vào đây để xem lời giải</summary>

```python
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;

Correct answer: 38
```

</details>

"""

# %% [markdown]
"""
### Bài toán 3

#### Giá trị tối đa của chỉ số khó khăn trong tập dữ liệu này là bao nhiêu?

"""
# %%
# # %%sql
# SELECT
#     MAX(hardship_index)
# FROM
#     chicago_socioeconomic_data;

# %% [markdown]
"""
<details><summary>Click vào đây để xem lời giải</summary>

```python
%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;

Correct answer: 98.0
```

</details>

"""

# %% [markdown]
"""
### Bài toán 4

#### Khu vực cộng đồng nào có chỉ số khó khăn cao nhất?

"""

# %%
# # %%sql
# SELECT
#     community_area_name,
#     hardship_index
# FROM
#     chicago_socioeconomic_data
# ORDER BY
#     hardship_index DESC
# LIMIT
#     5;
# %% [markdown]
"""
<details><summary>Click vào đây để xem lời giải</summary>

```python
#We can use the result of the last query to as an input to this query:
%sql SELECT community_area_name FROM chicago_socioeconomic_data where hardship_index=98.0

#or another option:
%sql SELECT community_area_name FROM chicago_socioeconomic_data ORDER BY hardship_index DESC NULLS LAST FETCH FIRST ROW ONLY;

#or you can use a sub-query to determine the max hardship index:
%sql select community_area_name from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data ) 

Correct answer: 'Riverdale'
    
```

</details>

"""

# %% [markdown]
"""
### Bài toán 5

#### Những khu vực cộng đồng nào ở Chicago có thu nhập bình quân đầu người lớn hơn 60.000 đô la?

"""

# %%
# # %%sql
# SELECT
#     community_area_name,
#     per_capita_income_
# FROM
#     chicago_socioeconomic_data
# WHERE
#     per_capita_income_ > 60000;

# %% [markdown]
"""
<details><summary>Click vào đây để xem lời giải</summary>

```python
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;

Correct answer:Lake View,Lincoln Park, Near North Side, Loop
    
```

</details>

"""

# %% [markdown]
"""
### Bài toán 6

#### Tạo biểu đồ phân tán bằng cách sử dụng các biến `per_capita_income_` và` hard_index`. Giải thích mối tương quan giữa hai biến số.

"""

# %%
import numpy as np  # convert to dataframe for better viewing result
import seaborn as sns

#
# per_capita_income_ = %sql SELECT per_capita_income_ FROM chicago_socioeconomic_data
# per_capita_income_ = np.array(per_capita_income_).flatten()
per_capita_income_ = np.array([1, 2, 3])
# hardship_index = %sql SELECT hardship_index FROM chicago_socioeconomic_data
# hardship_index = np.array(hardship_index).flatten()
hardship_index = np.array([1, 2, 3])
# %%
# using seaborn for scatter plot
sns.scatterplot(
    x=per_capita_income_,
    y=hardship_index,
)
# %%
# For fun, i would like to explore this relationship a little bit
# it certainly look like a semi-log relationship to me (or log-log)
# Let's test it 
log_hardship_index = np.log(hardship_index.astype('float64'))
log_per_capita_income_ = np.log(per_capita_income_.astype('float64'))
sns.scatterplot(
    x=per_capita_income_,
    y=log_hardship_index,
)
# After some experiment, it is quite a semi-log relationship, with log hardship_index as y and per_capita_income_ as x. We can apply Linear Regression in this. Oh btw, it is a negative relationship
# %% [markdown]
"""
<details><summary>Click vào đây để xem lời giải</summary>

```python
# if the import command gives ModuleNotFoundError: No module named 'seaborn'
# then uncomment the following line i.e. delete the # to install the seaborn package 
# !pip install seaborn

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())

Correct answer:You can see that as Per Capita Income rises as the Hardship Index decreases. We see that the points on the scatter plot are somewhat closer to a straight line in the negative direction, so we have a negative correlation between the two variables. 
    
```

</details>

"""

# %% [markdown]
# TODO:


"""
### Kết luận
#### Giờ bạn đã biết cách phân tích dữ liệu khám phá cơ bản bằng các công cụ visualization (trực quan hóa) SQL và python, bạn có thể khám phá thêm tập dữ liệu này để xem biến `per_capita_income_` có liên quan như thế nào đến`percent_households_below_poverty` và `percent_aged_16_unemployed`. Hãy tạo ra những visualization thú vị nhé!

"""

# %% [markdown]
"""
## Tóm tắt

#### Trong bài Lab này, bạn đã học cách lưu tập dữ liệu thực tế từ internet trong cơ sở dữ liệu, hiểu sâu hơn về dữ liệu bằng cách sử dụng truy vấn SQL. Bạn cũng tạo visualization một phần dữ liệu trong cơ sở dữ liệu để xem chúng kể câu chuyện gì.

"""
