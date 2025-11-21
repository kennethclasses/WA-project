import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('/users/amkalmah/project/WA-project/vehicles_us.csv') 
st.header("Car Data Visualization")
hist_button = st.button('Construir histograma de años')
if hist_button:
    st.write("Creacion de un Histograma de Años de los Vehículos")
    fig = px.histogram(car_data, x='model_year', nbins=50, title='Distribución de Años de los Vehículos')
    st.plotly_chart(fig)
hist_button = st.button('Construir histograma de odometro')
if hist_button:
    st.write("Creacion de un Histograma del Odometro de los Vehículos")
    fig = px.histogram(car_data, x='odometer', title='Distribución del odometro de los Vehículos')
    st.plotly_chart(fig)