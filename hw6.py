import matplotlib.pyplot as plt
import numpy as np

class Derivative:
    def __init__(self, func):
        self.func = func
        self.h = 1e-5

    def __call__(self, x):
        return (self.func(x + self.h) - self.func(x - self.h)) / (2 * self.h)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return lambda x: self(x)  

class ExponentialFunction:
    def __init__(self, a):
        self.a = a
        self.derivative = Derivative(self)  

    def __call__(self, x):
        return self.a * np.exp(x)

if __name__ == "__main__":
    exp_func = ExponentialFunction(a=2)

    print(f"f(0) = {exp_func(0)}")
    print(f"f'(0) = {exp_func.derivative(0)}")

    x = np.linspace(-2, 2, 100)
    y = exp_func(x)
    y_derivative = exp_func.derivative(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="f(x) = 2e^x")
    plt.plot(x, y_derivative, label="f'(x) = 2e^x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Графики функции и ее производной")
    plt.legend()
    plt.grid(True)
    plt.show()
