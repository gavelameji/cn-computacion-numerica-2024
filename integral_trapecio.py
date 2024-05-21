#-------------------------------------------------------------------------------
# Name:        Aproximación Integrales II: Trapecio
# Author:      Enol Monte Soto
# Created:     03/04/2024
# Copyright:   CC EMS 2024
#-------------------------------------------------------------------------------

import numpy as np

def trapecio_simple(f,a,b):
    aprox = (b-a)/2 * (f(a) + f(b))
    return aprox

f = lambda x: np.log(x)
res = trapecio_simple(f,1,3)
print(res)