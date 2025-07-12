import streamlit as st

def mostrar_donaciones():
    st.markdown("### 🤝 Apóyanos")
    st.markdown("""
    Si te ha sido útil, puedes apoyarme a seguir brindandote más herramientas:
    """)
    st.image("yape_qr.png", caption="Escanea para donar", use_container_width=True)
    st.markdown("""
    
    - 💳 **PayPal**: [Donar vía PayPal](https://www.paypal.com/donate?hosted_button_id=TU_ID)
    - 📱 **Yape / Plin**: 971 138 761
    - 🏦 **Transferencia bancaria**: *CCI: 123-456-789-0000*
    """)
    