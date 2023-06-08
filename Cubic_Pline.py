import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import math

# input data
x = np.array([0, 1, 2, 3])
y = np.array([1, math.e, pow(math.e, 2), pow(math.e, 3)])
n = len(x) - 1
res = np.empty((n + 1, 4))
res[:, 0] = y

# Step 1
h = np.empty(n)
for i in range(n):
    h[i] = x[i+1] - x[i]

# Step 2
a = np.empty(n)
for i in range(1, n):
    a[i] = (3 / h[i]) * (res[i + 1, 0] - res[i, 0]) - (3 / h[i - 1]) * (res[i, 0] - res[i - 1, 0])

# Step 3
l = np.empty(n + 1)
l[0] = 1
u = np.empty(n + 1)
u[0] = 0
z = np.empty(n + 1)
z[0] = 0

# Step 4
for i in range(1, n):
    l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1]
    u[i] = h[i] / l[i]
    z[i] = (a[i] - h[i - 1] * z[i - 1]) / l[i]

# Step 5
l[n] = 1
z[n] = 0
res[n, 2] = 0

# Step 6
for j in range(n - 1, -1, -1):
    res[j, 2] = z[j] - u[j] * res[j + 1, 2]
    res[j, 1] = (res[j + 1, 0] - res[j, 0]) / h[j] - h[j] * (res[j + 1, 2] + 2 * res[j, 2]) / 3
    res[j, 3] = (res[j + 1, 2] - res[j, 2]) / (3 * h[j])
    
# Step 7
print(res[:-1, :])