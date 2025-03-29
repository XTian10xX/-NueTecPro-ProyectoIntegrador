import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

st.markdown("Solucion - Sebastián Álvarez")

st.markdown("Primeros pasos de Dataframes")

# Crear las Series
nombres = pd.Series(['Alicia', 'Bob', 'Carlos'])
edades = pd.Series([25, 30, 28])
ciudades = pd.Series(['Nueva York', 'Londres', 'París'])

# Crear el DataFrame a partir de las Series
mi_dataframe = pd.DataFrame({'Nombre': nombres, 'Edad': edades, 'Ciudad': ciudades})

# Imprimir el DataFrame
st.dataframe(mi_dataframe)