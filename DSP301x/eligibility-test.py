import numpy as np


# Q1
def calculate_slope(y2, y1, x2, x1):
    slope = (y2 - y1) / (x2 - x1)
    return slope


q1 = calculate_slope(7, 0, 0, 3.5)

# Q2 - simple

# Q3 - more std dev - more spreadout

# Q4 - median is C?

# Q5:
my_string = "I'm ready"
print(my_string[4:8])

# Q6: probability: 2 country in eu, 6 total => 2/6=1/3

# Q7
q7 = (2 + 4**2) / 2

# Q8
q8 = 15 + (4**2) * 3

# Q9
q9 = (3 + 3 + 4 + 5 + 10) / 5
q9_alter = np.array([3, 3, 4, 5, 10]).mean()

# Q10
capitals = {
    "India": "New Delhi",
    "Nigeria": "Abuja",
    "USA": "Washington, DC",
}

capitals["Pakistan"] = "Islamabad"

# Q11
slope_q11 = calculate_slope(1, 10, 0, 4.5)

# Q12
x = ((52 / 2) - 1) / 10

pass
