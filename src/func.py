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

# function counting delta for Runge-Kutta method
def runge_kutta_delta_y(x, y, h):
    return h / 6 * (k1(x, y) + 2 * k2(x, y, h) + 2 * k3(x, y, h) + k4(x, y, h))

# first coefficient for Runge-Kutta method
def k1(x, y):
    return func(x, y)

# second coefficient for Runge-Kutta method
def k2(x, y, h):
    return func(x + h / 2, y + h * k1(x, y) / 2)

# third coefficient for Runge-Kutta method
def k3(x, y, h):
    return func(x + h / 2, y + h * k2(x, y, h) / 2)

# forth coefficient for Runge-Kutta method
def k4(x, y, h):
    return func(x + h, y + h * k3(x, y, h))

# euler method function
def euler(steps):

    # Initial values
    x = [0.0]
    y = [1.0]

    # step size
    h = (5 - x[0]) / steps

    # drawing graph using points
    for i in range(steps):
        x.append(x[i] + h)
        y.append(y[i] + h * (func(x[i], y[i])))

    return x, y

# IVP graph function
def IVP(steps):

    # Initial values
    x = [0.0]
    y = []

    # step size
    h = (5 - x[0]) / steps

    # drawing graph using points
    for i in range(steps):
        x.append(x[i] + h)
        y.append(funcIVP(x[i]))

    y.append(funcIVP(x[-1]))
    return x, y

# Runge-Kutta graph function
def runge_kutta(steps):

    # Initial values
    x = [0.0]
    y = [1.0]

    # step size
    h = (5 - x[0]) / steps

    # drawing graph using points
    for i in range(steps):
        x.append(x[i]+h)
        y.append(y[i] + runge_kutta_delta_y(x[i], y[i], h))
    return x, y

