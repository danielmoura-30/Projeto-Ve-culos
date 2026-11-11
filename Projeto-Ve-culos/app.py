import pandas as pd
import plotly.express as px
import streamlit as st

# Ler os dados
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho do aplicativo
st.header('Análise de Anúncios de Vendas de Carros')
st.write(
    'Explore os dados de veículos usando os botões abaixo para gerar gráficos'
    ' interativos.'
)

# Botão para criar o histograma
hist_button = st.button('Criar histograma')
if hist_button:
  st.write('Criando um histograma para a quilometragem dos veículos')
  fig_hist = px.histogram(car_data, x='odometer')
  st.plotly_chart(fig_hist, use_container_width=True)

# Botão para criar o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')
if scatter_button:
  st.write('Criando um gráfico de dispersão entre Preço e Odômetro')
  fig_scatter = px.scatter(car_data, x='odometer', y='price')
  st.plotly_chart(fig_scatter, use_container_width=True)