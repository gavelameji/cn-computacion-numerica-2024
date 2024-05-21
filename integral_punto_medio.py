#-------------------------------------------------------------------------------
# Name:        Aproximación Integrales I: Punto Medio
# Author:      Enol Monte Soto
# Created:     03/04/2024
# Copyright:   CC EMS 2024
#-------------------------------------------------------------------------------

import numpy as np

def punto_medio_simple(f,a,b):
    aprox = (b-a) * f((a+b)/2)
    return aprox

f = lambda x: np.log(x)
res = punto_medio_simple(f,1,3)
print(res)