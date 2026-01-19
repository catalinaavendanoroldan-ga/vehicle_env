import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Vehicle Ads Dashboard')

car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
build_histogram = st.checkbox('Build histogram')

if build_histogram:
    st.write('Histogram of vehicle mileage')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para scatter plot
build_scatter = st.checkbox('Build scatter plot')

if build_scatter:
    st.write('Price vs Mileage')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
