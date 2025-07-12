import streamlit as st
from sympy import Symbol, sympify, integrate, lambdify
import matplotlib.pyplot as plt
import numpy as np
from clasificacion import identificar_tipo
from procedimientos import generar_pasos

# Definimos la variable simbólica
x = Symbol('x')

# Configuración de la página
st.set_page_config(page_title="Calculadora de Integrales", page_icon="🧮")
st.title("🧮 Calculadora de Integrales - Paso a Paso")

from donaciones import mostrar_donaciones



# Sección de anuncios destacados


# Layout con columna principal y columna de donaciones
col1, col2 = st.columns([4, 1])

with col1:
    # Todo el contenido de cálculo, inputs, resultados, pasos y gráficas
    ...
    
with col2:
    # Sección de apoyo y donaciones
    mostrar_donaciones()
# Selección del modo
modo = st.radio("Selecciona el tipo de cálculo:", ["Integral indefinida", "Área bajo la curva"])

# Campo para función
expr_str = st.text_input("Ingresa la función (usa 'x'):", "x**2")

# Campos para límites (si corresponde)
a = b = None  # inicializamos las variables
if modo == "Área bajo la curva":
    a = st.number_input("Límite inferior (a):", value=0.0)
    b = st.number_input("Límite superior (b):", value=2.0)

# Procesamiento
if expr_str:
    try:
        expr = sympify(expr_str)

        # Clasificación automática
        tipo, recomendacion = identificar_tipo(expr_str)
        st.subheader("🧠 Clasificación automática")
        st.write(f"Tipo de integral detectado: **{tipo}**")
        st.info(f"Método sugerido: {recomendacion}")

        # Resolución según el modo
        if modo == "Integral indefinida":
            resultado = integrate(expr, x)
            st.subheader("🧮 Resultado simbólico")
            st.latex(f"\\int {expr_str} \\, dx = {resultado}")
        else:
            resultado = integrate(expr, (x, a, b))
            st.subheader("📐 Área bajo la curva")
            st.write(f"Desde `a = {a}` hasta `b = {b}`:")
            st.latex(f"\\int_{{{a}}}^{{{b}}} {expr_str} \\, dx = {resultado}")

        # Pasos explicativos
        pasos = generar_pasos(expr_str, resultado, tipo)
        st.subheader("🧭 Procedimiento explicado")
        for paso in pasos:
            st.markdown(paso)

        # Graficar función
        st.subheader("📊 Visualización de la función")
        f_numeric = lambdify(x, expr, modules=["numpy"])
        x_min = float(a) if modo == "Área bajo la curva" else -10
        x_max = float(b) if modo == "Área bajo la curva" else 10
        x_vals = np.linspace(x_min, x_max, 400)
        y_vals = f_numeric(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label="f(x)", color="blue")
        if modo == "Área bajo la curva":
            ax.fill_between(x_vals, y_vals, alpha=0.3, color="skyblue")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error al procesar la función: {e}")