import numpy as np
import matplotlib.pyplot as plt
import math

# Initialise a range between -50, 50
x = np.linspace(-50.0, 50.0, 100)
y = np.linspace(-50.0, 50.0, 100)

# Creating a meshgrid to  convert x and y from 
# ( 1 X 100 ) vector to ( 100 X 100 ) matrix.
[X, Y] = np.meshgrid(x, y) 

# Initialising the cost function given 
cost_fn = ((1/2)*((np.array(Y - X) ** 2) + (1 - X) ** 2))

figs, axes = plt.subplots(1, 1)
axes.set_title('Contour Plot of J(w)') 
axes.set_xlabel('weight vector 1 (w1)') 
axes.set_ylabel('weight vector 2 (w2)') 
axes.contourf(X, Y, cost_fn, 10, cmap = 'jet') 
axes.grid(True)
plt.arrow(2, 5, -2, 3, width = 2, ec ='white') 
plt.arrow(10, 5, 14, -5, width = 2, ec ='white')
plt.arrow(0, 5, -6, 5, width = 2, ec ='white')
plt.show()

# Reference: http://www.adeveloperdiary.com/data-science/how-to-visualize-gradient-descent-using-contour-plot-in-python/