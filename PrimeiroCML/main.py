import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

# pd.set_option('display.max_columns', None)

arquivo = pd.read_csv('~/Documents/IAAndPython/wine_dataset.csv')
print(arquivo.head())
print(arquivo.shape, '\n')

# Substitui o valor do campo style para valores numéricos
arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)
print(arquivo.head(), '\n')

# separa o datafram em duas partes, variáveis preditoras e variável alvo (atributo meta)
y = arquivo['style']
x = arquivo.drop('style', axis=1)

# separa os dados em treino e teste aleatoriamente
#    preditoras, alvo, porcentagem do conjunto teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# cria modelo (cria hipotese) depois triena o agente
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

# testa modelo com conjunto de teste
resultado = modelo.score(x_teste, y_teste)
print('Acurácia: ', resultado, '\n')

# printa 3 exemplos específicos
print(y_teste[400:403], ' ', x_teste[400:403], '\n')

# prevê os 3 exemplos a cima
previsoes = modelo.predict(x_teste[400:403])
print(previsoes)
