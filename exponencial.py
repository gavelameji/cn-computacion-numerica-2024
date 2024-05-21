import numpy as np
import matplotlib.pyplot as plt

# Para obtener el valor real y comparar.
f = lambda x: np.exp(x)

"""
EJERCICIO 2 BEGIN
"""
def ejercicio_2_fun_exp(x0, tol, max_num_sum):
    # Error (inicialmente infinito) y x0
    error = np.inf
    # Variables acumuladoras del factorial y las sumas.
    factorial = 1
    polinomio = 0
    # Variable de control.
    i = 0
    # Mientras se cumplan las dos condiciones.
    while i < max_num_sum and error > tol:
        # Guardamos el sumando i-ésimo.
        sumando = x0**i/factorial
        # Se lo sumamos al valor acumulado.
        polinomio += sumando
        # Actualizamos el factorial.
        factorial *= i + 1
        # Incrementamos variable de control.
        i += 1
        # Calculamos El Error (OJO: en este caso, el máximo de todos los sumandos).
        error = np.max(sumando)
    # Devolvemos el resultado.
    return polinomio

# Con vectores: Creamos un linspace de 50 valores entre -1 y 1.
valores_x = np.linspace(-1,1)
# Le aplicamos la funcion.
res_y = ejercicio_2_fun_exp(valores_x, 1E-8, 100)

# Pintamos la gráfica.
plt.figure()
plt.plot(valores_x,f(valores_x),'y', linewidth = 4,label = 'f')
plt.plot(valores_x,res_y,'b--',label = 'Aproximación f')
plt.plot(valores_x,valores_x*0,'k')
plt.legend()
plt.title('Aproximación de f con el polinomio de McLaurin')
plt.show()

"""
EJERCICIO 2 END
"""