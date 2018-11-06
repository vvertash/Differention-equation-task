import math

# function of my variant
def func(x, y):
    return - y - x

# function of my solution of IVP
def funcIVP(x):
    return 1 - x

# function for improved euler method
def delta_y(x, y, h):
    return h * func(x + h / 2, y + h / 2 * func(x, y))


