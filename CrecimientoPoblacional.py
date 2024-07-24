import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Datos del problema
N = 300
Y0 = 15
Y4 = 56
T1 = 4
k = 0


class EulerMethod:
    def __init__(self, delta_x: float, x_end: float, x0: float, y0: float, function: callable,
                 actual_function: callable = None):
        self.delta_x = delta_x
        self.x_end = x_end
        self.x0 = x0
        self.y0 = y0
        self.function = function
        self.actual_function = actual_function
        self.y_points = [y0]
        self.x_points = [x0]
        self.slopes = []

    def _get_y(self, slope: float):
        """
        This function computes the next y value using the Euler's Method
        :param slope:
        :return:
        """
        return slope * self.delta_x + self.y0

    def solve(self):
        """
        This function cmputes the aproximation to the solution using the Euler's Method
        :return:
        """
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

        self._show_graph(self.actual_function)

    def _show_graph(self, actual_function: callable = None):
        """
        This function plots the Euler aproximation
        :param actual_function: this optional parameter plots the actual function along with the
        aproximation in order to compare the aproximation with the actual values of the function
        :return: None
        """
        # Creating the scatter plot
        plt.scatter(self.x_points, self.y_points)

        # Connecting dots with lines
        plt.plot(self.x_points, self.y_points, '-o')

        if actual_function:
            # Plotting the actual function
            x_range = np.linspace(min(self.x_points), max(self.x_points), 100)  # Generating 100 points for smoothness
            y_actual = [actual_function(x) for x in x_range]  # Replace `self.actual_function` with your actual function
            plt.plot(x_range, y_actual, label='Actual Function')

        # Optional: Adding customization
        plt.title('Euler Method Aproximation')
        plt.xlabel('X axis label')
        plt.ylabel('Y axis label')

        # Display the plot
        plt.show()


# Ecuación para encontrar k
def solved_model(k):
    """
    This is the solution to the logistic model, this function is used to find the value of k
    :param k: constant k
    :return:
    """
    return Y4 - (N / (1 + ((N - Y0) / Y0) * np.exp(-k * T1)))


def equation(x, y):
    """
    This is the equation for the logistic model
    :param x:
    :param y:
    :return:
    """
    global k, N
    return k * (1 - y / N) * y


def main():
    global k

    # We compute the value of k
    k = fsolve(solved_model, 0)[0]

    # We define the parameters for the Euler's Method
    delta_x = 0.1
    x_end = 12
    x0 = 4
    y0 = 56

    euler = EulerMethod(delta_x, x_end, x0, y0, equation)
    euler.solve()


if __name__ == "__main__":
    main()
