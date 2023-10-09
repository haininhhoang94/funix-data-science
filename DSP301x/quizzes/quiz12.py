# Quiz 12
# %%

import numpy as np

a = np.array([1, 2, 3, 5, 8])
b = np.array([0, 3, 4, 2, 1])

c = a + b
c = c * a

print(c[2])
# %%
a = np.array([[1, 2, 3], [0, 1, 4]])
print(a.size)

# %%
a = np.array([[1, 2, 3], [0, 1, 4]])
b = np.zeros((2, 3), dtype=np.int16)
c = np.ones((2, 3), dtype=np.int16)

d = a + b + c
d
d[1, 2]

# %%
a = np.array([[0, 1, 0], [1, 0, 1]])
a += 3
b = a + 3

print(a[1, 2] + b[1, 2])

# %%
a = np.array([[3, 6, 7], [5, -3, 0]])
b = np.array([[1, 1], [2, 1], [3, -3]])
c = np.dot(a, b)

print(c)
# %%
a = np.array([[1, 4, 5, 12, 14], [-5, 8, 9, 0, 17], [-6, 7, 11, 19, 21]])
a[:, 2:4]
# %%
a = np.array([1, 1, 1, 1, 1])
b = np.array([2, 2, 2, 2, 2])
a * b
# %%
a = np.array([0, 1])
b = np.array([1, 0])
print(np.dot(a, b))

# %%
a = np.array([1, 1, 1, 1, 1])
a + 10
# %%
