import streamlit as st
import pandas as pd

st.title("Tabla 3x3 con Sumas Automáticas")

# Crear un DataFrame 3x3 con valores iniciales en 0.0
df = pd.DataFrame([[0.0, 0.0, 0.0] for _ in range(3)], columns=["A", "B", "C"])

st.write("Edita los valores en la tabla (haz click en cada celda para modificarlos):")

# Mostrar el DataFrame en un editor de datos (apariencia similar a Excel sin botones de más/menos)
edited_df = st.experimental_data_editor(df, num_rows="fixed", use_container_width=True)

# Calcular la suma de cada fila y cada columna
row_sums = edited_df.sum(axis=1)
col_sums = edited_df.sum(axis=0)

# Construir una nueva tabla que incluya los totales
tabla_con_sumas = edited_df.copy()
tabla_con_sumas["Suma"] = row_sums

# Crear una fila con las sumas de cada columna y el total general
suma_total = col_sums.sum()
fila_sumas = col_sums.append(pd.Series({"Suma": suma_total}))
fila_sumas = pd.DataFrame(fila_sumas).T

# Asignar un índice descriptivo para la fila de sumas
fila_sumas.index = ["Suma"]

# Combinar la tabla editable con la fila de sumas
tabla_final = pd.concat([tabla_con_sumas, fila_sumas])

st.write("### Tabla con Sumas")
st.table(tabla_final)
