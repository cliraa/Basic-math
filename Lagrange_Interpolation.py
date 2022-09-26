import numpy as np
import sympy as sym

# Inputs:

xi = np.array([1, 2]) # x-coordinates of the points
fi = np.array([1, 0]) # y-coordinates of the points

# Procedure:

n = len(xi)
x = sym.Symbol('x')
pol = 0
for i in range(0,n,1):
    num = 1
    den = 1
    for j in range(0,n,1):
        if (i!=j):
            num = num*(x-xi[j])
            den = den*(xi[i]-xi[j])
        t = (num/den)*fi[i]
    pol = pol + t
polisimple = sym.expand(pol)

# Output:

print(polisimple)