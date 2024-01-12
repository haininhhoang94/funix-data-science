inputs = [1, 2, 3, 2.5]

# NOTE: Output Layer
# Now, we have 4 inputs, which need 3 nodes (this just the definition of this problem). Let's define our nodes (1->3)
#
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

#
bias1 = 2
bias2 = 3
bias3 = 0.5

# output = [ inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias ]
output = []
# just for shortcut
weights = [weights1, weights2, weights3]
bias = [bias1, bias2, bias3]

# for i,
#
# print(output)
# pass
