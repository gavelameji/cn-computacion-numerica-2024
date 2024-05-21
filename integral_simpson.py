#-------------------------------------------------------------------------------
# Name:        Aproximación Integrales III: Simpson
# Author:      Enol Monte Soto
# Created:     03/04/2024
# Copyright:   CC EMS 2024
#-------------------------------------------------------------------------------

import numpy as np

def simpson_simple(f,a,b):
    aprox = (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))
    return aprox

f = lambda x: np.log(x)
res = simpson_simple(f,1,3)
print(res)