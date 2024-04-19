import pandas as pd

base = pd.read_csv("base_tratada.csv", sep=',')

#Parâmetros importantes para leitura da base
#encoding = 'ISO-8859-1', 'utf-8', 'cp1252'
#sep = "," ou ";"

print(base)
