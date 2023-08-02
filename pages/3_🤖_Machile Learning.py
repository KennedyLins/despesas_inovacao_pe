import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt 
from sklearn.cluster import KMeans 


st.set_page_config(
    page_title="Inovação PE",
    page_icon="✍️",
)

desp20 = pd.read_csv('data/despesas_pe_2020.csv', sep=';')
desp21 = pd.read_csv('data/despesas_pe_2021.csv', sep=';')
desp22 = pd.read_csv('data/despesas_2022.csv', sep=';')
despConcat = pd.concat([desp20,desp21,desp22])

dataload = '''import pandas as pd
df = pd.read_csv('file')
'''

st.header("Machine Learning 🤖")

st.markdown('''Nesta seção faremos uma análise dos nossos dados basendo-se em alguns algoritmos de Machine Learning''')
st.divider()

st.subheader('# Carregando e visualizando os dados')
st.code(dataload, language='python')
st.write(despConcat)

st.divider()

st.subheader('# K-means [Em construção]')
st.code('''subdf = df['Valor Liquidado','Elemento da Despesa']
diff = subdf['Valor Liquidado'] > 0
print(diff)''', language='python')
sliceMl = despConcat[['Valor Liquidado','Elemento da Despesa']]


difZero = sliceMl[sliceMl['Valor Liquidado'] > 0]
st.write(difZero)

st.code('''plt.scatter(dataset[:,1], dataset[:,0])''',language='python')

st.code('''plt.xlim() #range do eixo x
plt.ylim() #range do eixo y
plt.grid()''',language='python')

st.code('''kmeans = KMeans(n_clusters = 3, #numero de clusters
init = 'k-means++', n_init = 10, #algoritmo que define a posição dos clusters de maneira mais assertiva
max_iter = 100) #numero máximo de iterações
pred_y = kmeans.fit_predict(difZero)
plt.scatter(difZero[:,1], difZero[:,0], c = pred_y) #posicionamento dos eixos x e y
plt.xlim() #range do eixo x
plt.ylim() #range do eixo y
plt.grid() #função que desenha a grade no nosso gráfico
plt.scatter(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0], s = 70, c = 'red') #posição de cada centroide no gráfico
plt.show()
''')


st.divider()

st.subheader('# Regressão Linear [Descontinuado]')
st.divider()