import streamlit as st

def mostrar_donaciones():
    st.markdown("### 🤝 Apóyanos")
    st.markdown("""
    Si esta app te ha sido útil, puedes ayudarme a seguir desarrollándola:

    - 💳 **PayPal**: [Donar vía PayPal](https://www.paypal.com/donate?hosted_button_id=TU_ID)
    - 📱 **Yape / Plin**: Escanea el código QR aquí abajo
    - 🏦 **Transferencia bancaria**: *CCI: 123-456-789-0000*
    """)
    st.image("yape_qr.png", caption="Escanea para donar", use_column_width=True)