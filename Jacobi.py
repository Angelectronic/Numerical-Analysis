import numpy as np
import math 

N = 100
TOL = 0.01
A = [
    [3, -1, 1],
    [3, 6, 2],
    [3, 3, 7]
]

b = [1, 0, 4]

A = np.array(A, dtype=float)
b = np.array(b, dtype=float)

row, col = A.shape
for r in range(row):
    b[r] /= A[r, r]
    A[r, :] /= A[r, r]

I = np.identity(row)

D = I - A

x = np.zeros(row)

for i in range(N):
    k = x
    x = b + np.dot(D, x)
    print(f'x{i+1} = {x}')
    if (all(abs(x - k) < TOL)):
        break

