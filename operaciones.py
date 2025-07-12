# operaciones.py
from sympy import Symbol, sympify, integrate

x = Symbol('x')

def resolver_integral(expr_str):
    try:
        expr = sympify(expr_str)
        resultado = integrate(expr, x)
        return resultado
    except Exception as e:
        return f"Error: {e}"