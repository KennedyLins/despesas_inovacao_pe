import streamlit as st

st.set_page_config(
    page_title="Inovação PE",
    page_icon="✍️",
)

st.header("Algoritmos de Machine Learning")

st.markdown('''Os dados analisados abaixo foram extraídos do portal da transparência do estado de Pernambuco. 
A ideia inicial era extrair os dados do programa 0109 - APOIO À INOVAÇÃO, MODERNIZAÇÃO E COMPETITIVIDADE NO ESTADO DE PERNAMBUCO,
porém, esses dados não estavam disponíveis pois, segundo a Controladoria Geral do Estado, não tinham previsão na Lei Orçamentária
Anual (LOA). Dessa forma, extraimos os dados do programa 1090 - FOMENTO À INOVAÇÃO DO ESTADO DE PERNAMBUCO entre os anos de
2020 e 2022.
''')
st.divider()