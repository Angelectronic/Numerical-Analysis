import numpy as np
import math

N = 5000
TOL = 0.01

n = 100
alpha = 1 / 3

# create A
A = np.zeros((n - 1, n - 1))
np.fill_diagonal(A, 1)
np.fill_diagonal(A[1:, :], -alpha)
np.fill_diagonal(A[:, 1:], -(1 - alpha))

# create B
b = np.zeros(n - 1)
b[0] = alpha

A = [
    [-1, 0, 0, math.sqrt(2)/ 2, 1, 0, 0, 0],
    [0, -1, 0, math.sqrt(2)/ 2, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 1/2, 0],
    [0, 0, 0, math.sqrt(2)/ 2, 0, -1, -1/2, 0],
    [0, 0, 0, 0, -1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, -math.sqrt(2)/ 2, 0, 0, math.sqrt(3) / 2, 0],
    [0, 0, 0, 0, 0, 0, -math.sqrt(3) / 2, -1]
]

b = [0, 0, 0, 0, 0, 10000, 0, 0]


## Gauss-Seidel Method ##
A = np.array(A, dtype=float)
b = np.array(b, dtype=float)

row, col = A.shape
for r in range(row):
    b[r] /= A[r, r]
    A[r, :] /= A[r, r]

I = np.identity(row)
L = np.tril(A, -1)
U = np.triu(A, 1)

D = np.linalg.inv(I + L)
# print(f'D = {D}')
C = -np.dot(D, U)
# print(f'C = {C}')

# initial guess
x = np.dot(D, b) 
# x = np.zeros(row)

for i in range(N):
    k = x
    x = np.dot(C, x) + np.dot(D, b)
    print(f'x{i+1} = {x}')
    if (all(abs(x - k) < TOL)):
        break