import pandas as pd
import numpy as np
from google.colab import drive
base = pd.read_csv("https://raw.githubusercontent.com/lucagpgirardi/DataMining/main/base_tratada.csv", sep=",")

print(base.describe())
print(base.info())

print(base.isnull().sum()) # Conta quantos dados estão ausentes

print(base.isnull()) #mostra a cada linha e coluna se os dados estão faltantes, TRUE é faltante
print(base.DBGG_PIB.isnull())

#Vamos criar uma base com base em um dicionário
#Função .Dataframe()
df = pd.DataFrame({'A':[1,2,np.nan], 'B':[2,5,5], 'C':[1,2,np.nan]})

print(df)

#Como retiramos as linhas com valores nulos?

print(df.dropna(axis=1))
print(df)

#Como preencher os valores ausentes?
#função .fillna(Conteudo que vai preencher)
print(df.fillna(value = 'Conteúdo'))

#Substituir valores pela mediana da coluna
#.median so calcula com os valores existentes
df['A']=df['A'].fillna(value = df['A'].median())
print(df)

#Vamos tirar a linha 3 porque tem dados ausentes
print(df.dropna()) #tira a linha
print(df.dropna(axis=1)) #axis = 1 remove a coluna

drive.mount('drive')
