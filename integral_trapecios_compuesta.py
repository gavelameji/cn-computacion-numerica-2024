#-------------------------------------------------------------------------------
# Name:        Aproximación Integrales V: Trapecios Compuesto
# Author:      Enol Monte Soto
# Created:     03/04/2024
# Copyright:   CC EMS 2024
#-------------------------------------------------------------------------------

import numpy as np

def trapecios_comp(f,a,b,n):
    x = np.linspace(a,b,n)
    h = x[1]-x[0]
    aprox = h/2 * (f(a) + f(b))
    for i in range(1,n-1):
        aprox += h * f(x[i])
    return aprox

f = lambda x: np.log(x)
res = trapecios_comp(f,1,3,200)
print(res)

