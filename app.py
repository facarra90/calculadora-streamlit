import streamlit as st

st.title("Tabla 3x3 con Sumas Automáticas")

st.write("Ingresa los números en cada celda:")

# Inicializar la tabla 3x3 (se usa para calcular las sumas)
tabla = [[0.0, 0.0, 0.0] for _ in range(3)]

# Mostrar la tabla con los inputs y calcular la suma de cada fila
for i in range(3):
    # Crear 4 columnas: 3 para los inputs y 1 para mostrar la suma de la fila
    cols = st.columns(4)
    for j in range(3):
        # Cada input tiene una clave única para mantener el estado
        tabla[i][j] = cols[j].number_input(
            label=f"({i+1},{j+1})", 
            value=tabla[i][j],
            key=f"celda_{i}_{j}"
        )
    # Calcular y mostrar la suma de la fila
    suma_fila = sum(tabla[i])
    cols[3].write(f"Suma fila: {suma_fila}")

# Calcular y mostrar la suma de cada columna
st.markdown("### Sumas de Columnas")
cols = st.columns(4)
for j in range(3):
    suma_col = sum(tabla[i][j] for i in range(3))
    cols[j].write(f"Columna {j+1}: {suma_col}")
cols[3].write("")  # Espacio vacío
