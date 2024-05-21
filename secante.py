import numpy as np
import matplotlib.pyplot as plt

def secante(f, x0, x1, tol = 1.e-6, max_iter = 100):
    i = 0
    error = np.inf
    x = [x0,x1]
    for i in range(max_iter):
        if np.abs(x[-1]-x[-2]) < tol:
            return x[-1], x, i
        x_k = x[-1] - f(x[-1]) * (x[-1]-x[-2])/(f(x[-1])-f(x[-2]))
        x.append(x_k)
    return x[-1], x, maxiter

f = lambda x: x**5-3*x**2+1.6
res = secante(f,-1,-0.5)
r_aprox = res[0]
r_int = res[1]
r_iter = res[2]
x_graf = np.linspace(-1, 1.5)
plt.plot(x_graf, f(x_graf))
plt.plot(r_int[-1], f(r_int[-1]), 'r*')
plt.show()
