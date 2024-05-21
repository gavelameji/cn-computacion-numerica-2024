import numpy as np
import matplotlib.pyplot as plt

# Este fichero respresenta el ejercicio 4 de la práctica 7.

def dif_div(nodos, imgs):
    if (len(imgs) == 1):
        return imgs[0]
    difdiv1 = (dif_div(nodos[:len(imgs)-1]), imgs[:len(imagen)-1])
    difdiv2 = dif_div(imgs[:len(imgs)-1])
    result = (difdiv1 - difdiv2) / (nodo[0] - nodo[-1])
    return result

def polinomio_newton(nodos, imgs, z):
    pol = 0
    mul = 1
    for i in range(len(nodos)):
        pol += dif_div(nodos[:i], imgs[:i]) * mul
        mul *= (z-nodos[i])
    return pol

x = np.array([-1, 0, 2, 3, 5])
y = np.array([1, 3, 4, 3, 1])
Z = np.linspace(-2, 6, 10000)
pol = polinomio_newton(x, y, Z)
plt.plot(Z, pol)
plt.plot(x,y, "*r")
plt.show()
