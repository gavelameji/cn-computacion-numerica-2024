import numpy as np

np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

def triangulariza(A, b):
    # Verificamos que "A" sea cuadrada.
    filas = A.shape[0]
    cols = A.shape[1]
    if filas != cols:
        print("ERROR! La matriz debe ser cuadrada")
    # Copiamos la matriy y el vector a dos variables auxiliares.
    At = A
    bt = b
    # Recorremos de fila 0 a antepenúltima fila.
    for k in range(filas-1):
        # Coef: Dividimos el de al lado de la diagonal entre el de la diagonal.
        coef = At[k+1, k] / At[k,k]
        # Ponemos el siguiente de la diagonal a cero.
        At[k+1, k] = 0
        # Restamos a la siguiente de la diagonal el coeficiente por el de debajo
        At[k+1,k+1] -= coef*At[k,k+1]
        # Para los términos independientes, al siguiente le restamos coef + b[k]
        bt[k+1] -= coef*bt[k]
    return At,bt

# Pruebina

n = 7

A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T

b = np.arange(n,2*n)*1.

print('-------------  DATOS  -------------')
print('A')
print(A)
print('b')
print(b)
print('\n\n')

At, bt = triangulariza(A,b)

print('----  SISTEMA TRIANGULARIZADO ----')
print('At')
print(At)
print('bt')
print(bt)
print('\n\n')
#------------------------------------
n = 8

np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T

b = np.random.rand(n)

print('-------------  DATOS  -------------')
print('A')
print(A)
print('b')
print(b)
print('\n\n')

At, bt = triangulariza(A,b)

print('----  SISTEMA TRIANGULARIZADO ----')
print('At')
print(At)
print('bt')
print(bt)
print('\n\n')