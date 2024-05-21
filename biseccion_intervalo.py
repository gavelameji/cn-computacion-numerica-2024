import numpy as np
import matplotlib.pyplot as plt

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


def biseccion(f,a,b,tol=1E-6,max_iter=100):
    i = 0
    m = a
    error = np.inf
    while error > tol and i < max_iter:
        m_ant = m
        m = (a+b)/2
        f_a = f(a)
        f_b = f(b)
        f_m = f(m)
        if f_a * f_m < 0:
            b = m
        elif f_b * f_m < 0:
            a = m
        else:
            return m, i+1
        error = np.abs(m - m_ant)
        i += 1
    return m, i

def raices_bisec(f,a,b):
    intv = busqueda_incremental(f,a,b,100)
    res = np.zeros((len(intv)))
    for i in range(len(intv)):
        res[i] = biseccion(f, intv[i, 0], intv[i, 1])[0]

    # Pintar la gráfica.
    x = np.linspace(a,b,200)
    # Importante esta linea antes.
    plt.figure()
    # Pintar: Valores x, sus imagenes, umbral x, donde sea cero. (real)
    plt.plot(x, f(x), x, 0*x,'k')
    # Sobre lo que ya estaba: los valores aprox, donde sea cero.
    plt.plot(res,0*res,'ro')
    # Mostrar
    plt.show()

    print(res)

    return res

#%%
f1 = lambda x: np.cos(x)**2+x/10
f2 = lambda x: x**5-3*x**4+x+1.1
#%%
a = -10.; b = 0.
f = f1
raices_bisec(f,a,b)
#%%
a = -1.; b = 3.1
f = f2
raices_bisec(f,a,b)
