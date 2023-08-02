
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib 
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Inovação PE",
    page_icon="✍️",
)


desp20 = pd.read_csv('data/despesas_pe_2020.csv', sep=';')
desp21 = pd.read_csv('data/despesas_pe_2021.csv', sep=';')
desp22 = pd.read_csv('data/despesas_2022.csv', sep=';')
despConcat = pd.concat([desp20,desp21,desp22])

text3col  = "# A partir de agora vamos trabalhar apenas com três colunas"
code3col  = '''sub_df = df["Empenho","Valor Liquidado", "Elemento da Despesa"]
print(sub_df)'''
var3col   = ["Empenho","Valor Liquidado", "Elemento da Despesa"]
codedf = '''import pandas as pd

df = pd.read_csv('file')
print(df)'''

codeZero = '''print(df['Valor Liquidado'].isnull().sum())
'''
codeNull = '''print(df[df["Valor Liquidado"] > 0)
'''
textValNull = "# Verificando se existem valores liquidados nulos"
textDifZero = "# Filtrando os valores liquidados diferentes de zero"
minMaxMed   = "# Verificando mínimo, médio e máximo valor liquidado"
codeminMaxMed = '''print(Valor mínimo:  + str(df['Valor Liquidado'].min()))
print(Valor mínimo:  + str(df['Valor Liquidado'].min()))
print(Valor mínimo:  + str(df['Valor Liquidado'].min()))
'''
textQtdEmpenho = "# Quantidade de empenho por cada elemento de despesa"
codeQtdEmpenho = '''st.bar_chart(df['Elemento da Despesa'].value_counts())
'''


st.header("Análise Exploratória de Dados")

st.markdown('''Os dados analisados abaixo foram extraídos do portal da transparência do estado de Pernambuco. 
A ideia inicial era extrair os dados do programa 0109 - APOIO À INOVAÇÃO, MODERNIZAÇÃO E COMPETITIVIDADE NO ESTADO DE PERNAMBUCO,
porém, esses dados não estavam disponíveis pois, segundo a Controladoria Geral do Estado, não tinham previsão na Lei Orçamentária
Anual (LOA). Dessa forma, extraimos os dados do programa 1090 - FOMENTO À INOVAÇÃO DO ESTADO DE PERNAMBUCO entre os anos de
2020 e 2022.
''')
st.divider()

ano = st.radio(
"Escolha um ano para a análise",
('2020', '2021', '2022', 'Todos'))
st.divider()

if ano == '2020':        
    
    st.code(codedf, language='python')
    st.write('Este conjunto de dados contém ' + str(desp20.shape[0]) + ' linhas e ' + str(desp20.shape[1]) + ' colunas.')
    st.write(desp20)
    st.subheader(text3col)
    st.code(code3col, language='python')
    sliceDesp20 = desp20[var3col]
    st.write(sliceDesp20)
    
    st.divider()
    st.subheader(textValNull)
    st.code(codeZero,language='python')
    st.write('Existe(m)' + " " + str(sliceDesp20['Valor Liquidado'].isnull().sum()) + " " + 'valor(es) nulo(s)')

    st.divider()
    st.subheader(textDifZero)
    st.code(codeNull,language='python')
    difZeroDesp20 = sliceDesp20[sliceDesp20['Valor Liquidado'] > 0]
    st.write(difZeroDesp20)

    st.divider()
    st.subheader(minMaxMed)
    st.code(codeminMaxMed, language='python')
    st.write('Valor mínimo: ' + str(difZeroDesp20['Valor Liquidado'].min()))
    st.write('Valor médio: ' + str(difZeroDesp20['Valor Liquidado'].mean()))
    st.write('Valor máximo: ' + str(difZeroDesp20['Valor Liquidado'].max()))

    st.divider()
    st.subheader(textQtdEmpenho)
    st.code(codeQtdEmpenho, language='python')
    countElement = difZeroDesp20['Elemento da Despesa'].value_counts()
    countElement.plot()
    st.bar_chart(countElement)
    

elif ano == '2021':   
    
    st.code(codedf, language='python')
    st.write('Este conjunto de dados contém ' + str(desp21.shape[0]) + ' linhas e ' + str(desp21.shape[1]) + ' colunas.')
    st.write(desp21)
    st.subheader(text3col)
    st.code(code3col, language='python')
    sliceDesp21 = desp21[var3col]
    st.write(sliceDesp21)

    st.divider()
    st.subheader(textValNull)
    st.code(codeZero,language='python')
    st.write('Existe(m)' + " " + str(sliceDesp21['Valor Liquidado'].isnull().sum()) + " " + 'valor(es) nulo(s)')

    st.divider()
    st.subheader(textDifZero)
    st.code(codeNull,language='python')
    difZeroDesp21 = sliceDesp21[sliceDesp21['Valor Liquidado'] > 0]
    st.write(difZeroDesp21)

    st.divider()
    st.subheader(minMaxMed)
    st.code(codeminMaxMed, language='python')
    st.write('Valor mínimo: ' + str(difZeroDesp21['Valor Liquidado'].min()))
    st.write('Valor médio: ' + str(difZeroDesp21['Valor Liquidado'].mean()))
    st.write('Valor máximo: ' + str(difZeroDesp21['Valor Liquidado'].max()))

    st.divider()
    st.subheader(textQtdEmpenho)
    st.code(codeQtdEmpenho, language='python')
    countElement = difZeroDesp21['Elemento da Despesa'].value_counts()
    countElement.plot()
    st.bar_chart(countElement)

elif ano == '2022':
    
    st.code(codedf, language='python')
    st.write('Este conjunto de dados contém ' + str(desp22.shape[0]) + ' linhas e ' + str(desp22.shape[1]) + ' colunas.')
    st.write(desp22)
    st.subheader(text3col)
    st.code(code3col, language='python')
    sliceDesp22 = desp22[var3col]
    st.write(sliceDesp22)

    st.divider()
    st.subheader(textValNull)
    st.code(codeZero,language='python')
    st.write('Existe(m)' + " " + str(sliceDesp22['Valor Liquidado'].isnull().sum()) + " " + 'valor(es) nulo(s)')

    st.divider()
    st.subheader(textDifZero)
    st.code(codeNull,language='python')
    difZeroDesp22 = sliceDesp22[sliceDesp22['Valor Liquidado'] > 0]
    st.write(difZeroDesp22)

    st.divider()
    st.subheader(minMaxMed)
    st.code(codeminMaxMed, language='python')
    st.write('Valor mínimo: ' + str(difZeroDesp22['Valor Liquidado'].min()))
    st.write('Valor médio: ' + str(difZeroDesp22['Valor Liquidado'].mean()))
    st.write('Valor máximo: ' + str(difZeroDesp22['Valor Liquidado'].max()))

    st.divider()
    st.subheader(textQtdEmpenho)
    st.code(codeQtdEmpenho, language='python')
    countElement = difZeroDesp22['Elemento da Despesa'].value_counts()
    countElement.plot()
    st.bar_chart(countElement)

else:
    st.code(codedf, language='python')        
    st.write('Este conjunto de dados contém ' + str(despConcat.shape[0]) + ' linhas e ' + str(despConcat.shape[1]) + ' colunas.')
    st.write(despConcat)
    st.subheader(text3col)
    st.code(code3col, language='python')
    sliceConcat = despConcat[var3col]
    st.write(sliceConcat)

    st.divider()
    st.subheader(textValNull)
    st.code(codeZero,language='python')
    st.write('Existe(m)' + " " + str(sliceConcat['Valor Liquidado'].isnull().sum()) + " " + 'valor(es) nulo(s)')

    st.divider()
    st.subheader(textDifZero)
    st.code(codeNull,language='python')
    difZeroDespConcat = sliceConcat[sliceConcat['Valor Liquidado'] > 0]
    st.write(difZeroDespConcat)

    st.divider()
    st.subheader(minMaxMed)
    st.code(codeminMaxMed, language='python')
    st.write('Valor mínimo: ' + str(difZeroDespConcat['Valor Liquidado'].min()))
    st.write('Valor médio: ' + str(difZeroDespConcat['Valor Liquidado'].mean()))
    st.write('Valor máximo: ' + str(difZeroDespConcat['Valor Liquidado'].max()))

    st.divider()
    st.subheader(textQtdEmpenho)
    st.code(codeQtdEmpenho, language='python')
    countElement = difZeroDespConcat['Elemento da Despesa'].value_counts()
    countElement.plot()
    st.bar_chart(countElement)



