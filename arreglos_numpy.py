#
# Enol Monte Soto - Computación Numérica
# Práctica 1 - Versión 2
#

import numpy as np
import math
import matplotlib.pyplot as plt

# Ejercicio 1

def ejercicio_1a():
    a = np.array([1, 3, 7])
    return a

def ejercicio_1b():
    b = np.array([(2, 4, 3), (0, 1, 6)])
    return b

def ejercicio_1c():
    c = np.ones((1,3))
    return c

def ejercicio_1d():
    d = np.zeros((1,4))
    return d

def ejercicio_1e():
    e = np.zeros((3,2))
    return e

def ejercicio_1f():
    f = np.ones((4,4))
    return f

# Ejercicio 2

def ejercicio_2a():
    np.set_printoptions(precision=2,suppress=True)
    a = np.arange(7,16,2)
    return a

# Ejercicio 4

def ejercicio_4a():
    arr = np.arange(1,4)
    arr = np.append(arr, 0)
    arr = np.append(0,arr)
    return arr

def ejercicio_4b():
    arr = np.arange(1,4)
    c = np.array((0))
    print(c)
    arr = np.concatenate([arr])
    return arr

# Ejericio 5

a = np.array([(2,1,3,4),(9,8,5,7),(6,-1,-2,-8),(-5,-6,-9,-6)])

def ejercicio_5c():
    return a[2]

# Ejercicio 6

def ejercicio_6a():
    f = lambda x: x*math.exp(x)
    return f(2)

def ejercicio_6b():
    g = lambda z: z/(math.sin(z)*math.cos(z))
    return g(math.pi/4)

def ejercicio_6c():
    h = lambda x, y: (x*y)/((x**2)+(y**2))
    return(h(2,4))

# Ejercicio 7 (necesita librería matplotlib)

def ejercicio_7():
    x = np.linspace(-2 * math.pi, 2 * math.pi, 1000)      # malla
    f = lambda x : x * np.sin(3*x)     # función
    OX = 0*x                           # eje OX
    plt.figure()
    plt.plot(x,f(x))                   # dibujar la función
    plt.plot(x,OX,'k-')                # dibujar el eje X
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('xsen(3x)')
    plt.show()

print(ejercicio_7())



