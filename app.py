import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv') 
car_data["is_4wd"] = car_data["is_4wd"].fillna(0).astype(bool)
st.header("Visualizacion de Datos de Vehículos en USA")

hist_button = st.checkbox('Construir histograma de años')
if hist_button:
    st.write("Creacion de un Histograma de Años de los Vehículos")
    fig = px.histogram(car_data, x='model_year', nbins=30, title='Distribución de Años de los Vehículos')
    st.plotly_chart(fig, use_container_width=True)

hist_button = st.checkbox('Construir histograma de odometro')
if hist_button:
    st.write("Creacion de un Histograma del Odometro de los Vehículos")
    fig = px.histogram(car_data, x='odometer', nbins=30, title='Distribución del odometro de los Vehículos')
    st.plotly_chart(fig)

hist_button = st.checkbox('Construir histograma de cilindros')
if hist_button:
    st.write("Creacion de un Histograma de los cilindros de los Vehículos")
    fig = px.histogram(car_data, x='cylinders', title='Distribución de los cilindros de los Vehículos')
    st.plotly_chart(fig)

hist_button = st.checkbox('Construir histograma de 4WD')
if hist_button:
    st.write("Creacion de un Histograma del 4WD de los Vehículos")
    fig = px.histogram(car_data, x='is_4wd', title='Distribución del 4WD de los Vehículos')
    st.plotly_chart(fig)

hist_button = st.checkbox('Construir histograma de transmision')
if hist_button:
    st.write("Creacion de un Histograma del tipo de transmision de los Vehículos")
    fig = px.histogram(car_data, x='transmission', title='Distribución del tipo de transmision de los Vehículos')
    st.plotly_chart(fig)

hist_button = st.checkbox('Construir histograma del tipo de combustible')
if hist_button:
    st.write("Creacion de un Histograma del tipo de combustible de los Vehículos")
    fig = px.histogram(car_data, x='fuel', title='Distribución del tipo de transmision de los Vehículos')
    st.plotly_chart(fig)

hist_button = st.checkbox('Construir histograma de precio')
if hist_button:
    st.write("Creacion de un Histograma del precio de los Vehículos")
    fig = px.histogram(car_data, x='price', nbins=200, title='Distribución del precio de los Vehículos')
    st.plotly_chart(fig)


disp_button = st.checkbox('Construir gráfico de dispersión de odometro vs precio')
if disp_button:
    st.write("Gráfico de Dispersión: Odometro vs Precio")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig)

disp_button = st.checkbox('Construir gráfico de dispersión de año vs odometro')
if disp_button:
    st.write("Gráfico de Dispersión: Año vs Odometro")
    fig = px.scatter(car_data, x="model_year", y="odometer")
    st.plotly_chart(fig)

disp_button = st.checkbox('Construir gráfico de dispersión de Condicion vs precio')
if disp_button:
    st.write("Gráfico de Dispersión: Condicion vs Precio")
    fig = px.scatter(car_data, x="condition", y="price")
    st.plotly_chart(fig)
