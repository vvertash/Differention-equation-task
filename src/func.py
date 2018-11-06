import math

# function of my variant
def func(x, y):
    return - y - x

# function of my solution of IVP
def funcIVP(x):
    return 1 - x

# function counting delta for improved euler method
def delta_y(x, y, h):
    return h * func(x + h / 2, y + h / 2 * func(x, y))

# function for runge kutta method
def runge_kutta_delta_y(x, y, h):
    return h / 6 * (k1(x, y) + 2 * k2(x, y, h) + 2 * k3(x, y, h) + k4(x, y, h))

# first coefficient for runge kutta method
def k1(x, y):
    return func(x, y)

# second coefficient for runge kutta method
def k2(x, y, h):
    return func(x + h / 2, y + h * k1(x, y) / 2)

# third coefficient for runge kutta method
def k3(x, y, h):
    return func(x + h / 2, y + h * k2(x, y, h) / 2)

# forth coefficient for runge kutta method
def k4(x, y, h):
    return func(x + h, y + h * k3(x, y, h))

# euler method function
def euler(steps_amount):
    # Initial values
    x = [0.0]
    y = [1.0]
    # step size
    h = (5 - x[0]) / steps_amount

    for i in range(steps_amount):
        # drawing graph using points
        x.append(x[i] + h)
        y.append(y[i] + h * (func(x[i], y[i])))

    return x, y

