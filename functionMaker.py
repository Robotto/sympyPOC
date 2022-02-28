# Example code to parse a string to a mathematical function and plot it with matplotlib
# Use with caution, and it won't hurt you.
# 2022 Mark Moore

import numpy as np
import sympy as sym
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt

#only works with 2D functions right now:
def getFunctionFromString(inputString='y= x**2'):

    #Tjek efter om brugeren har tastet = ind i.
    if '=' in inputString:
        user_input = inputString.split('=')[1]  # Del input strengen op ved '=', og giv anden del tilbage.
    else:
        user_input=inputString

    print(f'This is the mathematical function we are about to make into a real python funktion: {user_input}')

    x, y = sym.symbols('x y')

    expr = parse_expr(user_input)

    f = sym.lambdify([x], expr)

    return f


def getPlot(f,x0=0,x1=100,step=0.1): #default values are used if none are given.

    fig, ax = plt.subplots()

    X = np.arange(x0, x1, step)
    Y = f(X)
    ax.plot(X, Y)

    #THIS IS WHERE I WOULD DECORATE THE PLOT WITH AXIS LABELS AND TITLES AND STUFF
    ax.set_title('test')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    #return the plot
    return plt

#Translate a string to a function using sympy parser and labdify:
f = getFunctionFromString('y=x**2')

#CREATE THE PLOT WITH THE CORRECT function, START, STOP, and STEP:
plt = getPlot(f)
#plt = getPlot(f, x0 = -100, x1 = 100, step = 1)


plt.show()