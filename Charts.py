import matplotlib.pyplot as plt
import numpy as np

def main():
    function = input("Podaj wzór funkcji w zmiennej x (np. x**2 + 2*x - 5): ")

    def funkcja(x):
        return eval(function)

    x = np.linspace(-10, 10, 400)
    y = funkcja(x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Wykres funkcji: {function}')
    plt.grid(True)
    plt.show()
