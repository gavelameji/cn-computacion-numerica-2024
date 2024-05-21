import numpy as np

def diagonalizar_por_debajo(A,b):
    # Número de filas.
    size = A.shape[0]
    # Verificamos que A sea cuadrada.
    if A.shape[0] != A.shape[1]:
        print("ERROR! La matriz debe ser cuadrada")
        return
    for i in range(size):
        for j in range(i+1, size):
            coef = A[j,i] / A[i,i]
            A[j,:] = A[j,:] - coef * A[i,:]
            # Para los términos independientes.
            b[j] = b[j] - coef * b[i]
    return A, b

def sustitucion_regresiva(A, b):
    size = A.shape[0]
    # En x guardamos las soluciones.
    x = np.zeros(size)
    x[size-1] = b[size-1]/A[size-1, size-1]
    for i in range(size-2, -1, -1):
        x[i] = (b[i] - A[i, i+1] * x[i+1])/A[i,i]
    return x
        
    
np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

n = 7
A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T
b = np.arange(n, 2*n)*1
AD, bD = diagonalizar_por_debajo(A, b)
x = sustitucion_regresiva(AD, bD)
# Imprimimos las soluciones.
print(x)


