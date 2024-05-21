#-------------------------------------------------------------------------------
# Name:        Aproximación Integrales VI: Simpson Compuesto
# Author:      Enol Monte Soto
# Created:     03/04/2024
# Copyright:   CC EMS 2024
#-------------------------------------------------------------------------------

import numpy as np

def simpson_comp(f,a,b,n):
    x = np.linspace(a,b,n)
    h = x[1]-x[0]
    aprox = 0
    for i in range(1,n):
        aprox += h/6 * (f(x[i-1]) + 4*f((x[i-1]+x[i])/2) + f(x[i]))
    return aprox

f = lambda x: np.log(x)
res = simpson_comp(f,1,3,200)
print(res)