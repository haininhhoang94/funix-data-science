# Quiz 13
# %%
# with open("./dog_breeds.txt", "r") as dog_breed_read:
with open("./dog_breeds.txt") as dog_breed_read:
    for line in dog_breed_read:
        print(line)

# %%
with open("./dog_breeds.txt") as tmpFile:
    print(tmpFile.read())
    # print(tmpFile.readline())
# %%
f = None
for i in range(5):
    with open("./data.txt", "w") as f:
        if i > 2:
            break
print(f.closed)
# True since by using open function the file are always closed after code running
# %%
import pandas as pd

pd.read_csv()
# %%
with open("./dog_breeds.txt", "r") as File1:
    file_stuff = File1.readline()
    print(file_stuff)
# Only print the first line

# %%
with open("./dog_breeds.txt", "r") as File1:
    for n in range(0, 2):
        file_stuff = File1.readline()
        # If the readline called again it shall be increase line (next line)
        print(file_stuff)

# %%
with open("./dog_breeds.txt", "r") as File1:
    print(File1.mode)
# %%
