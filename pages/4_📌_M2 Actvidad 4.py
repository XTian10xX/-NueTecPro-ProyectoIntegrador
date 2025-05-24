import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

data = {
    'Nombre': ['Ana', 'Bob', 'Clara', 'David', 'Emma'],
    'Edad': [25, 30, 22, 35, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao'],
    'Puntuación': [85, 90, 88, 92, 87]
}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

st.write("Interactúa con el DataFrame usando `.loc` y `.iloc` para seleccionar, filtrar y modificar datos.")

st.subheader("Tabla de Personas")
st.dataframe(df)

st.subheader("Buscar por posición")
pos = st.number_input("Elige una posición (0-4):", min_value=0, max_value=4, step=1)
if st.button("Mostrar por posición"):
    st.write(df.iloc[pos])

st.subheader("Buscar por etiqueta")
etiqueta = st.selectbox("Elige una etiqueta de fila:", df.index)
if st.button("Mostrar por etiqueta"):
    st.write(df.loc[etiqueta])


st.subheader("Modificar Puntuación")
fila_mod = st.selectbox("Etiqueta a modificar:", df.index, key='mod')
nueva_puntuacion = st.slider("Nueva puntuación:", 0, 100, df.loc[fila_mod, 'Puntuación'])
if st.button("Actualizar puntuación"):
    df.loc[fila_mod, 'Puntuación'] = nueva_puntuacion
    st.success(f"Puntuación actualizada para {df.loc[fila_mod, 'Nombre']}")
    st.dataframe(df)

st.subheader("Filtrar por Ciudad")
ciudad_seleccionada = st.selectbox("Selecciona una ciudad:", df['Ciudad'].unique())
filtro = df.loc[df['Ciudad'] == ciudad_seleccionada]
st.write(f"Personas de {ciudad_seleccionada}:")
st.dataframe(filtro)

