import numpy as np
from scipy.optimize import fsolve

# Datos del problema
N = 300
y0 = 15
y4 = 56
t1 = 4

# Ecuación para encontrar k
def equation(k):
    return y4 - (N / (1 + ((N - y0) / y0) * np.exp(-k * t1)))

# fsolve para encontrar k
k_guess = 0.1
k = fsolve(equation, k_guess)[0]

# Calcular la población en 12 días
t2 = 12

def population(t, k):
    return N / (1 + ((N - y0) / y0) * np.exp(-k * t))

y12 = population(t2, k)


# Tiempo cuando la población es 150
def equation_t(t):
    return 150 - population(t, k)

t_guess = 10
t_fastest_growth = fsolve(equation_t, t_guess)[0]

print("---------------------------------------------------------------------------------------------------")
print("|  La constante k aproximada, es: =", k, "                                          |")
print("|  La poblacion de mariposas despues de 12 dias sera aproximadamente: ", y12, "        |")
print("|  La poblacion de mariposas crece mas rapido (llega a 150) alrededor del dia: ", t_fastest_growth, "|")
print("---------------------------------------------------------------------------------------------------")


