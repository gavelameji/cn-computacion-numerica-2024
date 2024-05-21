import numpy as np
import matplotlib.pyplot as plt

# Este fichero representa los ejercicios 1 y 2 de la práctica 7.

# Ojo: z es un linspace / array numpy.
def interpolante(nodos, indice, z):
    res = 1
    for i in range(len(nodos)):
        if (i != indice):
            res *= (z-nodos[i])/(nodos[indice]-nodos[i])
    return res

def polinomio_lagrange(nodos, imgs, z):
    pol = 0
    for i in range(len(nodos)):
        pol += imgs[i] * interpolante(nodos, i, z)
    return pol

x = np.array([-1, 0, 2, 3, 5])
y = np.array([1, 3, 4, 3, 1])
Z = np.linspace(-2, 6, 10000)
pol = polinomio_lagrange(x, y, Z)
plt.plot(Z, pol)
plt.plot(x,y, "*r")
plt.show()
