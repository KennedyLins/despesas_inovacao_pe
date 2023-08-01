import streamlit as st
import pandas as pd
import numpy as np


gastos20 = pd.read_csv('data/despesas_pe_2020.csv', sep=';')
gastos21 = pd.read_csv('data/despesas_pe_2021.csv', sep=';')
gastos22 = pd.read_csv('data/despesas_2022.csv', sep=';')


selectPage = st.sidebar.selectbox(
    "O que voce esta procurando?",
    ("Home", "Analise Exploratoria", "Machine Learning")
)


if selectPage == "Home":
    st.write('Home')

#Analise Exploratoria
elif selectPage == "Analise Exploratoria":
    
    st.write('Analise Exploratoria')

    ano = st.radio(
    "Escolha um ano para a analise",
    ('2020', '2021', '2022', 'Todos'))

    if ano == '2020':  
        st.write(gastos20)
    elif ano == '2021':
        st.write(gastos21)
    elif ano == '2022':
        st.write(gastos22)
    else:
        st.write('Concat')

#Machine Learning
else:
    st.write('Machine Learning')






