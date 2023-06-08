import numpy as np
from numpy.polynomial import polynomial as poly
import math

x = np.array([7, 9.4, 12.3])
y = np.array([2, 4, 6])

# Fit a 2nd order polynomial to the data
coefs = poly.polyfit(x, y, 1)

# Evaluate the polynomial at x
yfit = poly.polyval(x, coefs)

# Compute the error
error = np.sum((y - yfit)**2)

# Print the results
print("Coefficients: {}".format(coefs))
print("Error: {}".format(error))