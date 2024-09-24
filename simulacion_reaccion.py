import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definimos una función para modelar la cinética de una reacción de primer orden A -> B
def reaccion(y, t, k):
    A = y[0]
    B = y[1]
    dA_dt = -k * A  # La concentración de A disminuye con una constante de velocidad k
    dB_dt = k * A   # La concentración de B aumenta a medida que A se transforma en B
    return [dA_dt, dB_dt]

# Parámetros iniciales
A0 = 1.0  # Concentración inicial de A (mol/L)
B0 = 0.0  # Concentración inicial de B (mol/L)
y0 = [A0, B0]  # Condiciones iniciales

k = 0.3  # Constante de velocidad de la reacción (1/min)

# Escala de tiempo (en minutos)
t = np.linspace(0, 20, 100)

# Resolver la ecuación diferencial
solucion = odeint(reaccion, y0, t, args=(k,))

# Graficar los resultados
plt.plot(t, solucion[:, 0], label='[A]')
plt.plot(t, solucion[:, 1], label='[B]')
plt.xlabel('Tiempo (min)')
plt.ylabel('Concentración (mol/L)')
plt.legend()
plt.title('Cinética de la reacción A -> B')
plt.grid(True)
plt.show()
