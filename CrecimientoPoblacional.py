import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Datos del problema
N = 300
Y0 = 15
Y4 = 56
T1 = 4


def main():
    k = guess_k()
    pass


# Ecuación para encontrar k
def equation(k):
    return Y4 - (N / (1 + ((N - Y0) / Y0) * np.exp(-k * T1)))


def guess_k():
    k = fsolve(equation, 0)
    return k[0]


class EulerMethod:
    def __init__(self, delta_x: float, x_end: float, x0: float, y0: float, function: callable):
        self.delta_x = delta_x
        self.x_end = x_end
        self.x0 = x0
        self.y0 = y0
        self.function = function
        self.y_points = [y0]
        self.x_points = [x0]
        self.slopes = []

    def _get_y(self, slope: float, x):
        return slope * self.delta_x + self.y0

    def solve(self):
        slope = self.function(self.x0, self.y0)
        self.slopes.append(slope)
        while self.x0 < self.x_end:
            y1 = self._get_y(slope, self.x0 + self.delta_x)
            x1 = self.x0 + self.delta_x
            slope = self.function(x1, y1)
            self.slopes.append(slope)

            self.x0 = x1
            self.y0 = y1

            self.x_points.append(self.x0)
            self.y_points.append(self.y0)

        self._show_graph()

    def _show_graph(self):
        # Creating the scatter plot
        plt.scatter(self.x_points, self.y_points)

        # Optional: Adding customization
        plt.title('Sample Scatter Plot')
        plt.xlabel('X axis label')
        plt.ylabel('Y axis label')

        # Display the plot
        plt.show()


def fun(x, y):
    return y


if __name__ == "__main__":
    delta_x = 1
    x_end = 10
    x0 = 0
    y0 = 1

    euler = EulerMethod(delta_x, x_end, x0, y0, fun)
    euler.solve()
