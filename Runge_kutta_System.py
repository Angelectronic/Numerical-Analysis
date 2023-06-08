import numpy as np

# Input
a = 0
b = 0.2
h = 0.1
N = (b-a)/h
m = 2

arr = [-1, 1] # Initial values

if N != int(N):
    print("Error: N must be an integer")
    exit()
N = int(N)

# Function
def f(t, y):
    return np.array([y[1], 1 - y[0]])

# Step 1
t = a

# Step 2
w = np.array([arr], dtype=float)

# Step 3
print ("t =", t, " w =", w[0])

# Step 4
for i in range(1, N+1):
    k1 = h * f(t, w[i-1])
    k2 = h * f(t + h/2, w[i-1] + k1/2)
    k3 = h * f(t + h/2, w[i-1] + k2/2)
    k4 = h * f(t + h, w[i-1] + k3)
    w = np.append(w, [w[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6], axis=0)
    t = a + i*h
    print ("t =", t, " w =", w[i])
