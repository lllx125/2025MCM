import numpy as np
from scipy.optimize import minimize


def obj_function(vars):
    x, y = vars
    return (x - 1)**2 + (y - 2)**2

# Equality constraint: x + y = 2


def constraint_eq(vars):
    return vars[0] + vars[1] - 2


x0 = np.array([0.5, 0.5])  # initial guess

# Define constraints in a dictionary
cons = ({'type': 'eq', 'fun': constraint_eq})

# Define bounds for x, y as x >= 0, y >= 0
bnds = [(0, None), (0, None)]

# Solve
res = minimize(obj_function, x0, method='SLSQP', bounds=bnds,
               constraints=cons, options={'disp': True})

print("Final solution:", res.x)
print("Objective function value:", res.fun)
print("Equality constraint (should be 0):", constraint_eq(res.x))
