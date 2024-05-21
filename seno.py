import numpy as np

# Para obtener el valor real y comparar.
f = lambda x: np.sin(x)

def ejercicio_3_seno():
    # Constantes: tolerancia máxima y número máximo de sumandos.
    tol = 1e-8
    max_num_sum = 100
    # Error (inicialmente infinito) y x0
    error = np.inf
    x0 = np.pi/4
    # Variables acumuladoras del factorial y las sumas.
    factorial = 1
    polinomio = 0
    # Variable de control.
    i = 0
    # Ahora, aparece el signo.
    signo = 1
    # Mientras se cumplan las dos condiciones.
    while i <= max_num_sum and error >= tol:
        # Guardamos el sumando i-ésimo (Ojo, cada 2).
        sumando = x0 ** (2 * i + 1) / factorial
        # Se lo sumamos al valor acumulado cambiando el signo.
        polinomio += (sumando * signo)
        # Incrementamos variable de control.
        i += 1
        # Actualizamos el factorial (para numeros impares).
        factorial *= 2 * i * (2 * i + 1)
        # Calculamos El Error.
        error = np.abs(sumando)
        # Cambiamos el signo.
        signo *= -1
    # Info por pantalla.
    print("E1: Aproximación para x = pi/4 -> ", polinomio)
    print("E1: Valor Real para x = pi/4   -> ", f(x0))
    print("E1: Número de iteraciones      -> ", i)
    # Devolvemos el resultado.
    return polinomio

ejercicio_3_seno()