import streamlit as st
import pandas as pd

st.title("Tabla 3x3 con Sumas Automáticas")

# Crear un DataFrame 3x3 con valores iniciales en 0.0
df = pd.DataFrame([[0.0, 0.0, 0.0] for _ in range(3)], columns=["A", "B", "C"])

st.write("Edita los valores en la tabla:")

# Utiliza la función disponible según la versión de Streamlit
if hasattr(st, 'data_editor'):
    edited_df = st.data_editor(df, num_rows="fixed", use_container_width=True)
else:
    edited_df = st.experimental_data_editor(df, num_rows="fixed", use_container_width=True)

# Calcular la suma de cada fila y cada columna
row_sums = edited_df.sum(axis=1)
col_sums = edited_df.sum(axis=0)

# Agregar la suma de cada fila como una nueva columna
tabla_con_sumas = edited_df.copy()
tabla_con_sumas["Suma"] = row_sums

# Crear una fila con las sumas de cada columna y el total general
suma_total = col_sums.sum()
fila_sumas = col_sums.copy()
fila_sumas["Suma"] = suma_total
fila_sumas = pd.DataFrame(fila_sumas).T
fila_sumas.index = ["Suma"]

# Combinar la tabla editable con la fila de sumas
tabla_final = pd.concat([tabla_con_sumas, fila_sumas])

st.write("### Tabla con Sumas")
st.table(tabla_final)

