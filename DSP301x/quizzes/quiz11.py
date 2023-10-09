# %%
print(int(12.3) * 10 + int(4 / 5))

# %%
print(int(False))

# %%
t = ("foo", "bar", "baz")
t[1] = "test"

# %%
t = "foo"
# %%
a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
# first we create a tuple from 1 to 9, then from value 1 (start from 0)
# we create a new array with [2,5,8], spacing 3

# %%
d1 = {"john": 40, "peter": 45}
d2 = {"john": 466, "peter": 45}
d1 > d2
# %%
age = 60
if age > 40:
    if age > 60:
        print("Turning old")
    else:
        print("Middle Age")
else:
    print("Young Age")
# answer: Middle age, since in first if, no Young Age. in second if, no Turning old


# %%
if True:
    print("Some shit")
else:
    print("102")
# %%
if not (1 and (not (0 or 1))):
    print("Hello")
else:
    print("Bye")
# %%
test = 0 or 1
test1 = not (0 or 1)
test2 = 1 and test1
test3 = not test2

# %%
t = ("foo",)
# %%
