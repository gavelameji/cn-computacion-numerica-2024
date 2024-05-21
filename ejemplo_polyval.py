# Computación Numérica - Práctica 3
# Ejemplo De Evaluación de Polinomios

import numpy as np
import matplotlib.pyplot as plt

x0 = 1
# Los coeficientes de menor a mayor grado.
p = np.array([1,-3,1])
# El valor del polinomio en...
np.polyval(p, x0)
# Linespace para la gráfica.
x = np.linspace(-5,5,100)
# Opción 1: Expresar como lambda-función.
f = lambda x: 1-3*x+x**2
plt.plot(x,f(x))
plt.show()
# Opción 2: Expresar con polyval directamente.
plt.plot(x,np.polyval(p,x))
plt.show()