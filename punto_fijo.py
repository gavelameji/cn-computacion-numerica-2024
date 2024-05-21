import numpy as np
import matplotlib.pyplot as plt

def punto_fijo(g, x0, tol = 1E-6, max_iter = 100):
    x = [x0]
    for i in range(max_iter):
        x_k = g(x[-1])
        x.append(x_k)
        if np.abs(x[-1] - x[-2]) < tol:
            return x[-1], x, i
    return x[-1], x, max_iter

g = lambda x: np.exp(-x)
res = punto_fijo(g, 0.5, max_iter = 200)
print(res[0])