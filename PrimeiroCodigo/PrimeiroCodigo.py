import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('/home/murillo/Documents/Notebooks/athlete_events.csv')

dados_copy = dados.copy()

faltantes = dados.isnull().sum()
print('Quantidade dados faltantes:', '\n', faltantes, '\n')

for x in dados.columns :
    if faltantes[x] > 0 :
        coluna = dados[x]
        print(x, '\n', coluna, '\n')