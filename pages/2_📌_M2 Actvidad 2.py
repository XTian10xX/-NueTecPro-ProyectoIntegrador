import streamlit as st
import pandas as pd
import io

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
df = pd.read_csv("estudiantes_colombia.csv")

st.dataframe(df)

opciones_disponibles = st.selectbox(
    'Selecciona una Opción...',
    ['1. Ver las 5 primeras filas',
     '2. Ver las 5 Últimas filas',
     '3. Resumen de la Base de Datos',
     '4. Seleccionar Columnas',
     '5. Filtrar estudiantes']
)

if opciones_disponibles == '1. Ver las 5 primeras filas':
    st.dataframe(df.head())
elif opciones_disponibles == '2. Ver las 5 Últimas filas':
    st.dataframe(df.tail())
elif opciones_disponibles == '3. Resumen de la Base de Datos':
    st.markdown("Con .info:")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str=buffer.getvalue()
    st.text(info_str)
    st.markdown("Con .describe:")
    st.dataframe(df.describe())
elif opciones_disponibles == '4. Seleccionar Columnas':
    opciones_para_selecTabla = st.selectbox(
        'Selecciona la Columna...',
        ['Id',
         'Nombre',
         'Edad',
         'Ciudad',
         'Promedio',
         'Asistencia']
    )
    if opciones_para_selecTabla == 'Id':
        tablaId = st.dataframe(df['id'])
    elif opciones_para_selecTabla == 'Nombre':
        tablaNom = st.dataframe(df['nombre'])
    elif opciones_para_selecTabla == 'Edad':
        tablaNom = st.dataframe(df['edad'])
    elif opciones_para_selecTabla == 'Ciudad':
        tablaNom = st.dataframe(df['ciudad'])
    elif opciones_para_selecTabla == 'Promedio':
        tablaNom = st.dataframe(df['promedio'])
    elif opciones_para_selecTabla == 'Asistencia':
        tablaNom = st.dataframe(df['asistencia'])
elif opciones_disponibles == '5. Filtrar estudiantes':
    #deslizar_rango_promedio = st.slider("Rango para Promedio", 0.0, 5.0, (0.5, 4.5))
    #st.write(df['promedio'])

# Definir el rango del slider basado en los valores mínimos y máximos de la columna
    min_value = df['promedio'].min()
    max_value = df['promedio'].max()

    # Slider para seleccionar el rango
    selected_range = st.slider(
        "Selecciona el rango de valores",
        min_value=0.0,
        max_value=5.0,
        value=(min_value, max_value)
    )

    # Filtrar los datos según el rango seleccionado
    filtered_data = df[(df['promedio'] >= selected_range[0]) & (df['promedio'] <= selected_range[1])]

    # Calcular el promedio de los datos filtrados
    average_value = filtered_data['promedio'].mean()
    st.write(filtered_data)
