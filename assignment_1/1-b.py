import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import math

# Creating a sample space of 150 points from 0 - 4
sample = np.linspace(-4, 4, 150)
# number of order terms (0, 1, 2, 3, 4)
num_order = 5
# Creating an output array that stores all the values
output = [0] * 5
# Taylor series expansion of e^x
# T(x) = 1 + x + (x^2/2!) + (x^3 / 3!) + ...... + (x^n / n!)
# 0 order term: 1
# 1st order term: 1 + x
# 2nd order term: 1 + x + (x^2/2!)
# 3rd order term: 1 + x + (x^2/2!) + (x^3/3!)
# 4th order term: 1 + x + (x^2/2!) + (x^3/3!) + (x^4/4!)
for i in range(5):
    # For the 0th term, all the values would be 1
    if i == 0:
        # Make the entire 0th row of the output array as 1
        output[i] = np.ones(len(sample))
    else:
        taylor_expansion = sample ** i / math.factorial(i)
        # Add the previous row's value + current value
        output[i] = output[i - 1] + taylor_expansion
# Add labels
output_var = ['Zeroth', 'First', 'Second', 'Third', 'Forth']     
for i in range(5):
    plt.plot(sample,output[i], label=output_var[i] + ' term')
# Plot the actual taylor series values for the function
plt.plot(sample, np.exp(sample), label="e^x")
# Plot the values for the zeroth to fourth order term
for i in range(5):
    plt.plot(sample, output[i])
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
