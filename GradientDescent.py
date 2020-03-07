from sympy import *

def gradient_descent(function, *variables):
    alpha = 0.01
    values = {v: 1 for v in variables}
    converge = False
    while not converge:
        new_values = dict()
        for v in variables:
            new_values[v] = values[v] - alpha * function.diff(v).subs(values)
        if new_values == values:
            converge = True
        else:
            values = new_values
    return new_values
