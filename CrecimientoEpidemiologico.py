import numpy as np
import matplotlib.pyplot as plt

def main():

    # Parámetros iniciales
    S0 = 990
    I0 = 10
    R0 = 0
    beta = 0.3
    gamma = 0.1
    dt = 0.1
    dias = 50

    # Número de pasos
    n_steps = int(dias / dt)

    # Vectores para almacenar los valores
    S = np.zeros(n_steps + 1)
    I = np.zeros(n_steps + 1)
    R = np.zeros(n_steps + 1)

    # Condiciones iniciales
    S[0] = S0
    I[0] = I0
    R[0] = R0

    # Método de Euler
    for t in range(n_steps):
        dS = -beta * S[t] * I[t] / (S[t] + I[t] + R[t])
        dI = beta * S[t] * I[t] / (S[t] + I[t] + R[t]) - gamma * I[t]
        dR = gamma * I[t]
        
        S[t + 1] = max(S[t] + dS * dt, 0)
        I[t + 1] = max(I[t] + dI * dt, 0)
        R[t + 1] = max(R[t] + dR * dt, 0)

    print('Resultados finales:')
    print('Susceptibles:', S[-1])
    print('Infectados:', I[-1])
    print('Recuperados:', R[-1])

    # Crear el gráfico
    t = np.linspace(0, dias, n_steps + 1)
    plt.figure(figsize=(10,6))
    plt.plot(t, S, label='Susceptibles')
    plt.plot(t, I, label='Infectados')
    plt.plot(t, R, label='Recuperados')
    plt.xlabel('Días')
    plt.ylabel('Número de Individuos')
    plt.legend()
    plt.title('Modelo SIR - Método de Euler')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()