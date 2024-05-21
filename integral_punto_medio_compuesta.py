#-------------------------------------------------------------------------------
# Name:        Aproximación Integrales IV: Punto Medio Compuesto
# Author:      Enol Monte Soto
# Created:     03/04/2024
# Copyright:   CC EMS 2024
#-------------------------------------------------------------------------------

import numpy as np

def punto_medio_comp(f,a,b,n):
    x = np.linspace(a,b,n)
    h = x[1]-x[0]
    aprox = 0
    for i in range(1,n):
        aprox += h * f((x[i-1]-x[i])/2)
    return aprox

f = lambda x: np.log(x)
res = punto_medio_comp(f,1,3,200)
print(res)