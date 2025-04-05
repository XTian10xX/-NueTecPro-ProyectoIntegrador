import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

st.subheader("Uso de Pandas, para la visualización de datos de un archivo CSV")

st.markdown("""
Esta actividad usé una biblioteca de software llamada Pandas para lograr capturar y mostrar datos
específicos, de un archivo CSV, que es un achivo que guarda datos en forma de tabla. Y con todo esto, 
hice una aplicación con Streamlit para capturar estos datos y una que tu, el usuario, puedes interactuar.
""")

# Cargar el dataset
df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

st.dataframe()