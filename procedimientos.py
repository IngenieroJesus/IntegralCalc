# procedimientos.py
# procedimientos.py

def generar_pasos(expr_str, resultado, tipo=None):
    """
    Genera una lista de pasos explicativos en función del tipo de integral detectado.
    """
    pasos = []

    # Paso 1: reconocimiento
    pasos.append(f"🔍 Se detectó la expresión: `{expr_str}`")

    # Paso 2: clasificación si está disponible
    if tipo:
        pasos.append(f"📌 Clasificación: {tipo}")
    else:
        pasos.append("📌 No se pudo determinar la clasificación de la función.")

    # Paso 3: sugerencia de método según tipo
    recomendaciones = {
        "Polinómica": "Aplicamos la regla de potencia: ∫xⁿ dx = xⁿ⁺¹ / (n+1) + C.",
        "Exponencial": "Usamos la regla directa para exponenciales: ∫eˣ dx = eˣ + C.",
        "Logarítmica": "Aplicamos integración por partes si corresponde, como ∫ln(x) dx.",
        "Trigonométrica": "Aplicamos fórmulas básicas o por partes si hay producto.",
        "Racional o mixta": "Evaluamos si es posible una sustitución racional o fracciones parciales.",
        "Radical": "Consideramos una sustitución trigonométrica o racional para simplificar la raíz.",
        "Función general": "No se reconoce una estructura específica, se aplica integración simbólica.",
        "Desconocida": "Se resolvió usando métodos generales de cálculo simbólico."
    }

    metodo = recomendaciones.get(tipo, "Se aplicó un método simbólico estándar usando SymPy.")
    pasos.append(f"🧠 Método aplicado: {metodo}")

    # Paso 4: mostrar resultado
    pasos.append(f"✅ Resultado de la integral: `{resultado}`")

    # Paso 5: recomendación final
    pasos.append("🔁 Puedes verificar el resultado derivando la función integrada.")

    return pasos
#def generar_pasos(expr_str, resultado):
 #   pasos = [
  #      f"1️⃣ Se identificó la función a integrar: {expr_str}",
   #     "2️⃣ Se aplicó el método de integración simbólica con SymPy",
    #    f"3️⃣ El resultado de la integral es: {resultado}",
     #   "4️⃣ Se puede verificar el resultado derivando la expresión"
   # ]
    #return pasos