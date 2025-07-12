import streamlit as st

def mostrar_anuncios():
    with st.expander("📢 Novedades y anuncios"):
        st.markdown("""
        ### 🚀 Últimas actualizaciones
        - Se agregó la sección de instrucciones paso a paso.
        - Mejora en la visualización de gráficos.
        - Optimización del rendimiento en cálculos simbólicos.

        ### 📅 Próximamente
        - Soporte para integrales definidas con funciones trigonométricas.
        - Modo oscuro para la interfaz.
        - Exportar resultados en PDF.
        """)