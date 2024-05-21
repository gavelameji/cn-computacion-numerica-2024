import numpy as np

"""
Va recorrendo subintervalos de tamaño 1, de uno en uno,
si cumple Bolzano es que hay una raíz así que la añade.

RECIBE:
    f: Función lambda.
    a, b: Extremos del intervalo.
    n: Numero de intervalos en los que se dividirá \ valores que toma f.

DEVUELVE:
    Lista de intervalos que contienen raíces.
"""
def busqueda_incremental(f, a, b, n):
    # Creamos un linspace de a hasta b con n valores.
    x = np.linspace(a, b, n+1)
    # Guardamos en "y" las imágenes de los valores del linespace para f.
    y = f(x)
    # Un array de tuplas que guarde los intervalos.
    intervalos = np.zeros((n,2))
    # Contador de intervalos con raíces.
    contador = 0
    # Para cada uno de los valores...
    for i in range(n):
        # ... si imagen de ese por la del siguiente < 0...
        if y[i] * y[i+1] < 0:
            # Se añade a la ultima fila.
            intervalos[contador,:] = x[i : i+2]
            # Se incrementa el contador de intervalos.
            contador += 1
    return intervalos[:contador,:]

#%% Ejemplo 1
f1 = lambda x: x**5 - 3 * x**2 + 1.6
a = -1.; b = 1.5; n = 25

intervalos = busqueda_incremental(f1,a,b,n)
print('Intervalos que contienen raíces de f1\n')
print(intervalos)

#%% Ejemplo 2
f2 = lambda x: (x+2) * np.cos(2*x)
a = 0.; b = 10.; n = 100

intervalos = busqueda_incremental(f2,a,b,n)
print('\nIntervalos que contienen raíces de f2\n')
print(intervalos)