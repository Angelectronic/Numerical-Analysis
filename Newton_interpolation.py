import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import math

def u_cal(u, n):
    res = u
    for i in range(1, n):
        res = res * (u - i)
    return res

# Dữ liệu
data = pd.read_csv('population.csv').values
x = data[:, 0]
y = data[:, 1]
input = float(input('Nhập năm: ')) 

n = len(x)
y_forward = np.array([[0 for i in range(n)] for j in range(n)])
y_forward[:, 0] = y

# Tính sai phân tiến
for i in range(1, n):
    for j in range(n - i):
        y_forward[j][i] = y_forward[j + 1][i - 1] - y_forward[j][i - 1]

# Tính nội suy Newton
u = (input - x[0]) / (x[1] - x[0])
Newton = y_forward[0][0]
for i in range(1, n):
    Newton = Newton + (u_cal(u, i) * y_forward[0, i]) / math.factorial(i)

print('Dân số', Newton)
