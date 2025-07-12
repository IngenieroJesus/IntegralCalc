# clasificacion.py

from sympy import Symbol, sympify, expand, Function
from sympy.core.function import AppliedUndef

x = Symbol('x')

def identificar_tipo(expr_str):
    """
    Recibe una expresión como string y devuelve una tupla:
    (tipo_detectado, método_sugerido)
    """
    try:
        expr = sympify(expr_str)
        expr_expanded = expand(expr)

        # Detectar funciones trigonométricas
        if expr.has(Function("sin")) or expr.has(Function("cos")) or "sin" in str(expr) or "cos" in str(expr):
            return "Trigonométrica", "Se recomienda usar integración directa o por partes si hay producto."

        # Detectar logaritmos
        if expr.has(Function("log")) or "ln" in str(expr):
            return "Logarítmica", "Puede resolverse por partes, especialmente si está multiplicada por x."

        # Detectar funciones exponenciales
        if expr.has(Function("exp")) or "e" in str(expr):
            return "Exponencial", "Puede resolverse directamente o por partes si hay combinación con polinomios."

        # Detectar polinomios puros
        if expr.is_polynomial():
            return "Polinómica", "Aplicar la regla de potencia directamente."

        # Detectar raíces cuadradas u otras expresiones radicales
        if "sqrt" in str(expr) or expr.has(Function("sqrt")):
            return "Radical", "Podría requerir sustitución trigonométrica o racional."

        # Detectar funciones racionales
        if "/" in str(expr) or expr.is_rational_function():
            return "Racional o mixta", "Usar sustitución u otro método dependiendo de la complejidad del denominador."

        # Detectar funciones definidas por el usuario
        if expr.has(AppliedUndef):
            return "Función general", "Expresión simbólica sin estructura clasificable."

        return "Desconocida", "No se pudo clasificar la expresión correctamente."

    except Exception as e:
        return "Error de análisis", f"No se pudo procesar la expresión: {e}"