
import streamlit as st
import pandas as pd
import numpy as np

desp20 = pd.read_csv('data/despesas_pe_2020.csv', sep=';')
desp21 = pd.read_csv('data/despesas_pe_2021.csv', sep=';')
desp22 = pd.read_csv('data/despesas_2022.csv', sep=';')

despConcat = pd.concat([desp20,desp21,desp22])

selectPage = st.sidebar.selectbox(
    "O que voce esta procurando?",
    ("Home", "Analise Exploratoria", "Machine Learning")
)


if selectPage == "Home":
    st.write('Home')

#Analise Exploratoria
elif selectPage == "Analise Exploratoria":
    
    ano = st.radio(
    "Escolha um ano para a analise",
    ('2020', '2021', '2022', 'Todos'))

    if ano == '2020':        
        st.write('O dataframe contém, ' + str(desp20.shape[0]) + ' linhas e ' + str(desp20.shape[1]) + ' colunas.')
        sliceDesp20 = desp20[["Empenho","Valor Liquidado", "Elemento da Despesa"]]
        st.write(sliceDesp20)
    elif ano == '2021':   
        st.write('O dataframe contém, ' + str(desp21.shape[0]) + ' linhas e ' + str(desp21.shape[1]) + ' colunas.') 
        sliceDesp21 = desp21[["Empenho","Valor Liquidado", "Elemento da Despesa"]]
        st.write(sliceDesp21)
    elif ano == '2022':
        st.write('O dataframe contém, ' + str(desp22.shape[0]) + ' linhas e ' + str(desp22.shape[1]) + ' colunas.')
        sliceDesp22 = desp22[["Empenho","Valor Liquidado", "Elemento da Despesa"]]
        st.write(sliceDesp22)
    else:        
        st.write('O dataframe contém, ' + str(despConcat.shape[0]) + ' linhas e ' + str(despConcat.shape[1]) + ' colunas.')
        sliceConcat = despConcat[["Empenho","Valor Liquidado", "Elemento da Despesa"]]
        st.write(sliceConcat)
#Machine Learning
else:
    st.write('Machine Learning')







