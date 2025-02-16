import streamlit as st

st.title("Calculadora Simple")

# Entrada de números
numero1 = st.number_input("Ingrese el primer número:", value=0.0)
numero2 = st.number_input("Ingrese el segundo número:", value=0.0)

# Selección de la operación
operacion = st.selectbox("Elija una operación:", ("Suma", "Resta", "Multiplicación", "División"))

# Realizar la operación
if operacion == "Suma":
    resultado = numero1 + numero2
elif operacion == "Resta":
    resultado = numero1 - numero2
elif operacion == "Multiplicación":
    resultado = numero1 * numero2
elif operacion == "División":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error: División por cero"

st.write("El resultado es:", resultado)
