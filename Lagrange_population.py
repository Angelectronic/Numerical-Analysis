import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy

NUM_OF_DATA = 4

def Lagrange_interpolate(x, y, input):
    """Hàm Lagrange"""
    Lagrange = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if j != i:
                p *= (input - x[j]) / (x[i] - x[j])
        Lagrange += y[i] * p
    return Lagrange

def data_for_interpolate(x, y, input):
    res_x = []
    res_y = []
    
    x_copy = copy.deepcopy(x)
    y_copy = copy.deepcopy(y)
    x_copy = np.append(x_copy, input)
    x_copy = np.sort(x_copy)

    input_idx = np.where(x_copy == input)[0][0]
    
    if input_idx < NUM_OF_DATA // 2:
        res_x = x[:NUM_OF_DATA]
        res_y = y[:NUM_OF_DATA]
    elif input_idx > len(x) - NUM_OF_DATA // 2:
        res_x = x[-NUM_OF_DATA:]
        res_y = y[-NUM_OF_DATA:]
    else:
        res_x = x[input_idx - NUM_OF_DATA // 2: input_idx + NUM_OF_DATA // 2]
        res_y = y[input_idx - NUM_OF_DATA // 2: input_idx + NUM_OF_DATA // 2]

    return res_x, res_y


# Dữ liệu
data = pd.read_csv('population.csv').values
x = data[:, 0]
y = data[:, 1]
input = float(input('Nhập năm: '))    

used_x, used_y = data_for_interpolate(x, y, input)
res = Lagrange_interpolate(used_x, used_y, input)

print('Dân số: ', res)

# visualize
x_predict = np.arange(1955, 2021, 1)
y_predict = np.array([])
for i in x_predict:
    used_x, used_y = data_for_interpolate(x, y, i)
    res = Lagrange_interpolate(used_x, used_y, i)
    y_predict = np.append(y_predict, res)

plt.scatter(x, y)
plt.xlabel('Năm')
plt.ylabel('Dân số (triệu người)')
plt.plot(x_predict, y_predict, color='red')
plt.show()