import streamlit as st
import pandas as pd
import numpy as np

gastos20 = pd.read_csv('data/despesas_pe_2020.csv', sep=';')

gastos21 = pd.read_csv('data/despesas_pe_2021.csv', sep=';')

gastos22 = pd.read_csv('data/despesas_2022.csv', sep=';')


print('Gastos 2020 ---------------------------------')

print(gastos20.head())

print('Gastos 2021 ---------------------------------')

print(gastos21.head())

print('Gastos 2022 ---------------------------------')

print(gastos22.head())

