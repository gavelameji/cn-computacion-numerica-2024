import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

"""
Calcular raices (aproximación) conociendo la derivada
RECIBE:
    f, df: Función y su derivada.
    x0: Inicial
DEVUELVE:
    Apoximación de raiz, iteraciones.
"""
def newton(f,df,x0,tol=1.e-6,max_iter=100):
    i = 0
    error = np.inf
    x = x0
    while error > tol and i < max_iter:
        x_ant = x
        x = x - (f(x) / df(x))
        error = np.abs(x-x_ant)
        i+=1
    return x, i

#------------------------
def main():
    f =  lambda x: x**5 - 3 * x**2 + 1.6
    df = lambda x: 5 * x**4 - 6 * x

    sol = np.zeros(3)

    x0 = -0.7
    sol[0], i0 = newton(f,df,x0)
    print(sol[0], i0)

    x1 = 0.8
    sol[1], i1 = newton(f,df,x1)
    print(sol[1], i1)

    x2 = 1.2
    sol[2], i2 = newton(f,df,x2)
    print(sol[2], i2)

    x = np.linspace(-1.,1.5,100)

    plt.figure()
    plt.plot(x,f(x))
    plt.plot(x,0*x,'k')
    plt.plot(sol,np.zeros(3),'ro')
    plt.show()
    #--------------------------------
    x = sym.Symbol('x', real=True)
    f_sim   = sym.cos(x)*(x**3+1)/(x**2+1)
    df_sim  = sym.diff(f_sim,x)

    f   = sym.lambdify([x], f_sim,'numpy')
    df  = sym.lambdify([x], df_sim,'numpy')

    x0 = -2.
    sol[0], i0 = newton(f,df,x0)
    print('%.5f' % sol[0])

    x1 = -0.5
    sol[1], i1 = newton(f,df,x1)
    print('%.5f' % sol[1])

    x2 = 2.
    sol[2], i2 = newton(f,df,x2)
    print('%.5f' % sol[2])

    x = np.linspace(-3,3,100)

    plt.figure()
    plt.plot(x,f(x))
    plt.plot(x,0*x,'k')
    plt.plot(sol,np.zeros(3),'ro')
    plt.show()

if __name__ == "__main__":
    main()