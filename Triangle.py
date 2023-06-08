import numpy as np

A = [[3, 1, -1],
     [1, -5, 1],
     [-1, 1, 4]]

b = [5, -17, 11] 

A = np.array(A)
b = np.array(b)
row, col = A.shape

L = np.zeros((row, col))
U = np.zeros((row, col))
np.fill_diagonal(U, 1)

for k in range(row):
    L[k, 0] = A[k, 0]
    for j in range(1, k+1):
        L[k, j] = A[k, j] - np.dot(L[k, :j], U[:j, j])
    for i in range(k, row):
        U[k, i] = (A[k, i] - np.dot(L[k, :k], U[:k, i])) / L[k, k]

y = np.zeros(row)
for i in range(row):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

print(y)