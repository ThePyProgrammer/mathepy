# mathepy/calculus.py

import sympy as sp

x, y = sp.symbols("x y")

def diff(f = x**2, q = x): return sp.simplify(sp.diff(f, q))

def solveEqn(exp1 = x, exp2 = y, f = y, q = x):
	return sp.solve(sp.Eq(exp1, exp2))[0][q]

def implicit(exp1 = x, exp2 = y, up = y, down = x):
	solved = sp.solve(sp.Eq(exp1, exp2))
	return diff(solved[0][y], x)

def integrate(f, q):
	return sp.simplify(sp.integrate(f, q))
