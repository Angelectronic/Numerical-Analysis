import numpy as np
import copy

A = [[-1, 4, 1],
     [5/3, 2/3, 2/3],
     [2, 1, 4]]

b = [8, 1, 11] 

A = np.array(A, dtype=float)
b = np.array(b, dtype=float)
row, col = A.shape

# Gauss
for i in range(row):
    if A[i, i] == 0:
        for j in range(i + 1, row):
            if A[j, i] != 0:
                C = copy.deepcopy(A[i])
                A[i] = copy.deepcopy(A[j])
                A[j] = C
                C = copy.deepcopy(b[i])
                b[i] = copy.deepcopy(b[j])
                b[j] = C
                break

    b[i] = b[i] / A[i, i]
    A[i] = A[i] / A[i, i]
    for j in range(i + 1, row):
        b[j] = b[j] - b[i] * A[j, i]
        A[j] = A[j] - A[i] * A[j, i]
     

# Backward    
for i in range(row - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        b[j] = b[j] - b[i] * A[j, i]
        A[j] = A[j] - A[i] * A[j, i]
        
print(A, b)