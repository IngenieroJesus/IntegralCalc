import streamlit as st

def mostrar_instrucciones():
    with st.expander("📘 Instrucciones de uso"):
        st.markdown("""
        Bienvenido a la calculadora de integrales paso a paso. Aquí tienes algunas reglas para ingresar funciones correctamente:

        ### 🔣 Símbolos importantes

        - Para la **multiplicación**, usa el asterisco `*`  
          Ejemplo: `3*x` en lugar de `3x`

        - Para **elevar al cuadrado**, usa `**`  
          Ejemplo: `x**2` significa \\( x^2 \\)
        
        - Para **Usar Raiz Cuadrada**, usa la expresion `sqrt`  
          Ejemplo: Uno sobre raiz cuadrada de x elevado al cuadrado
          Escribe: 1/qrt(x**2)

        - Para funciones como seno y coseno, escribe `sin(x)`, `cos(x)`, etc.

        ### 📝 Ejemplos válidos:

        - `x**2 + 3*x`
        - `exp(x)`
        - `ln(x)`
        - `sin(x) * x**2`

        ### 🖼️ Ejemplo visual:
        """)
        
        st.image("./imagenes/ejemplo1.png", caption="sintaxis correcta meoow", use_container_width=True)