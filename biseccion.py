import numpy as np
import matplotlib.pyplot as plt

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

#------------------------
def main():
    f = lambda x: x**5 - 3 * x**2 + 1.6

    sol = np.zeros(3)

    a = -0.7; b = -0.6
    sol[0], i0 = biseccion(f,a,b)
    print(sol[0], i0)

    a = 0.8; b = 0.9
    sol[1], i1 = biseccion(f,a,b)
    print(sol[1], i1)

    a = 1.2; b = 1.3
    sol[2], i2 = biseccion(f,a,b)
    print(sol[0], i2)

    x = np.linspace(-1,1.5,100)

    plt.figure()
    plt.plot(x,f(x))
    plt.plot(x,0*x,'k')
    plt.plot(sol,np.zeros(3),'ro')
    plt.show()

    #-------------------------
    print('')
    f = lambda x: np.cos(x)*(x**3+1)/(x**2+1)

    sol = np.zeros(3)

    a = -2.; b = -1.5
    sol[0], i0 = biseccion(f,a,b)
    print('%.5f' % sol[0])

    a = -1.5; b = 0.
    sol[1], i1 = biseccion(f,a,b)
    print('%.5f' % sol[1])

    a = 1.; b = 2.
    sol[2], i2 = biseccion(f,a,b)
    print('%.5f' % sol[2])

    x = np.linspace(-3,3,100)

    plt.figure()
    plt.plot(x,f(x))
    plt.plot(x,0*x,'k')
    plt.plot(sol,np.zeros(3),'ro')
    plt.show()

if __name__ == "__main__":
    main()


