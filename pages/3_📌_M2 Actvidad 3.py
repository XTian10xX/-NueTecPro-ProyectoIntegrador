import datetime
import streamlit as st
import pandas as pd
import numpy as np
import random
import faker

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

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

# Configurar Faker para Colombia
fake = faker.Faker('es_CO')

# Establecer semilla para reproducibilidad
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# Crear datos
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

# Crear DataFrame
df = pd.DataFrame(data)

df_filtrado = df.copy()

# Introducir algunos valores nulos
df.loc[3:5, 'ingreso_mensual'] = np.nan
df.loc[15:17, 'ocupacion'] = np.nan

# Convertir fecha_nacimiento a datetime
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

st.title("Aplicación de Filtros Dinámicos")

# Using object notation
st.sidebar.title('FILTROS')

filtro_edad = st.sidebar.checkbox("Filtrar por rango de edad")
if filtro_edad:
    edad_min, edad_max = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (20, 60))
    df_edad = df_filtrado[df_filtrado['edad'].between(edad_min, edad_max)]
    st.subheader("Filtro: Edad")
    st.dataframe(df_edad)
else:
    df_edad = df_filtrado


filtro_municipio = st.sidebar.checkbox("Filtrar por municipios")
municipios = ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja',
              'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 
              'Leticia', 'Puerto Inírida']
if filtro_municipio:
    municipios_sel = st.sidebar.multiselect("Selecciona municipios", municipios)
    if municipios_sel:
        df_municipio = df_edad[df_edad['municipio'].isin(municipios_sel)]
    else:
        df_municipio = df_edad
    st.subheader("Filtro: Municipios")
    st.dataframe(df_municipio)
else:
    df_municipio = df_edad

filtro_ingreso = st.sidebar.checkbox("Filtrar por ingreso mensual mínimo")
if filtro_ingreso:
    ingreso_min = st.sidebar.slider("Ingreso mensual mínimo (COP)", 800000, 12000000, 1000000, step=100000)
    df_ingreso = df_municipio[df_municipio['ingreso_mensual'] > ingreso_min]
    st.subheader("Filtro: Ingreso Mensual Mínimo")
    st.dataframe(df_ingreso)
else:
    df_ingreso = df_municipio

filtro_ocupacion = st.sidebar.checkbox("Filtrar por ocupación")
ocupaciones = ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico',
               'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero']
if filtro_ocupacion:
    ocupaciones_sel = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones)
    if ocupaciones_sel:
        df_ocupacion = df_ingreso[df_ingreso['ocupacion'].isin(ocupaciones_sel)]
    else:
        df_ocupacion = df_ingreso
    st.subheader("Filtro: Ocupación")
    st.dataframe(df_ocupacion)
else:
    df_ocupacion = df_ingreso


filtro_vivienda = st.sidebar.checkbox("Filtrar personas sin vivienda propia")
if filtro_vivienda:
    df_vivienda = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]
    st.subheader("Filtro: Sin vivienda propia")
    st.dataframe(df_vivienda)
else:
    df_vivienda = df_filtrado


filtro_nombre = st.sidebar.checkbox("Filtrar por nombre")
if filtro_nombre:
    texto_nombre = st.sidebar.text_input("Ingresa una subcadena para buscar en nombres:", value="")
    if texto_nombre:
        df_nombre = df_vivienda[df_vivienda['nombre_completo'].str.contains(texto_nombre, case=False, na=False)]
    else:
        df_nombre = df_vivienda
    st.subheader("Filtro: Nombre contiene subcadena")
    st.dataframe(df_nombre)
else:
    df_nombre = df_vivienda

filtro_anio = st.sidebar.checkbox("Filtrar por año de nacimiento")
if filtro_anio:
    anios = list(range(1949, 2010))
    anio_seleccionado = st.sidebar.selectbox("Selecciona el año de nacimiento", anios)
    df_anio = df_nombre[df_nombre['fecha_nacimiento'].dt.year == anio_seleccionado]
    st.subheader(f"Filtro: Año de nacimiento = {anio_seleccionado}")
    st.dataframe(df_anio)
else:
    df_anio = df_nombre


filtro_internet = st.sidebar.checkbox("Filtrar por acceso a internet")
if filtro_internet:
    acceso = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])
    tiene_internet = acceso == "Sí"
    df_internet = df_anio[df_anio['acceso_internet'] == tiene_internet]
    st.subheader(f"Filtro: Acceso a internet = {acceso}")
    st.dataframe(df_internet)
else:
    df_internet = df_anio


filtro_nulos = st.sidebar.checkbox("Filtrar por ingresos nulos")
if filtro_nulos:
    df_nulos = df_internet[df_internet['ingreso_mensual'].isnull()]
    st.subheader("Filtro: Ingresos mensuales nulos")
    st.dataframe(df_nulos)
else:
    df_nulos = df_internet


filtro_fechas = st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento")
if filtro_fechas:
    fecha_min = datetime.date(1949, 1, 1)
    fecha_max = datetime.date(2009, 12, 31)
    fecha_inicio, fecha_fin = st.sidebar.date_input("Selecciona el rango de fechas de nacimiento",
                                                    [fecha_min, fecha_max],
                                                    min_value=fecha_min,
                                                    max_value=fecha_max)
    if len([fecha_inicio, fecha_fin]) == 2:
        df_fechas = df_nulos[df_nulos['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio),
                                                                   pd.to_datetime(fecha_fin))]
    else:
        df_fechas = df_nulos
    st.subheader("Filtro: Rango de fechas de nacimiento")
    st.dataframe(df_fechas)
else:
    df_fechas = df_nulos

st.subheader("Resultado Final (Todos los filtros aplicados)")
st.dataframe(df_fechas)