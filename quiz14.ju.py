# %%
import re

# %%
x = "From : Using the : character"
y = re.findall("^F.+:", x)
print(y)
# %%
x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("\S+?@\S+", x)
print(y)
# %%

# %%
import numpy as np

# %%
a = np.array([1, 1])
# %%
a.transpose()
# %%

