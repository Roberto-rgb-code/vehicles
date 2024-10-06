import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

df = load_data()

# Título de la aplicación
st.title('Análisis de anuncios de venta de coches')

# Histograma
st.header('Histograma de precios')
hist_button = st.button('Mostrar histograma de precios')

if hist_button:
    fig_hist = px.histogram(df, x="price", title="Distribución de precios")
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
st.header('Gráfico de dispersión: Precio vs. Año del Modelo')
scatter_button = st.button('Mostrar gráfico de dispersión')

if scatter_button:
    fig_scatter = px.scatter(df, x="model_year", y="price", title="Precio vs. Año del Modelo")
    st.plotly_chart(fig_scatter, use_container_width=True)

