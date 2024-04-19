#Importação de dados no pandas
import pandas as panda
reservas_bacen = panda.read_csv("bcdata.sgs.23043.csv", sep=";")
print(reservas_bacen)
#panda read (base, sep, encoding - como utf-8 ou )
# Abertura de arquivos armazenados no GOOGLE DRIVE
"""
# 1) Montagem do Drive
from google.colab import drive
drive.mount('/content/drive',force_remount=True)
"""

#Juntar várias bases em um mesmo csv

pib_bacen = panda.read_csv("pib.csv", sep=";")
merge1 = panda.merge(reservas_bacen, pib_bacen, on= "data", how="inner")

#Merge te permite juntar csvs. Os parâmetros são (csv1, csv2, on é a coluna que ambos compartilham e
#how é a maneira que eles vão ser interpolados)



#Para renomear uma coluna usando pandas:
merge1.rename(columns={"valor_x": "Reservas internacionais"}, inplace=True)
print(merge1)

base_alunos = panda.read_excel("https://github.com/danieltb3006/DM_Ibmec/raw/main/base_alunos.xlsx")
#print(base_alunos)

#Se eu quero listar as primeiras X linhas do dataframe, usamos nomedele.head(numero de linhas)

print(base_alunos.head(10))

#Se eu quero listar as últimas X linhas do dataframe, usamos nomedele.tail(numero linhas)

print(base_alunos.tail(2))

#Gera uma tabela estatística com média, mediana, quartis

print(base_alunos.describe())

#Traz informações básicas sobre a tabela, tipo de dado, nome de coluna

print(base_alunos.info())

#Para acessar uma coluna específica, usamos nomedodf["nome da coluna"]

#Método .iloc [numero linha, numero coluna] - ex coluna AP1 todas as linhas

print(base_alunos.iloc[:,2])

#Método.loc [nome linha, nome coluna]

print(base_alunos.loc[:, "AP1"])

#Fazendo operações com algumas colunas de um dataframe
#Use base[[todas as colunas q quiser]]
recorte_base = base_alunos[["AP1", "AP2", "AP3"]]

print(recorte_base)

media_ponderada = base_alunos["AP1"]*0,4 + base_alunos["AP2"]*0,6

print(media_ponderada)

#filtrando dados no pandas
#filtrando alunos que fazem direito

direito = base_alunos [base_alunos["Curso"] == "DIR"]

print(direito)

#filtrando com mais de uma condição, usamos () para cada uma das condições e &
#Ex: Direito e nota melhor que 7

direito_nota = base_alunos[(base_alunos["Curso"] == "DIR") & (base_alunos["Nota"] > 7.0) ]

print(direito_nota)

#Função .groupby Se eu quiser agrupar e fazer operações agrupadas
#Média das notas por curso
#agrupado = base_alunos.groupby(by="Curso").mean()["Nota"]

#Se você quiser mudar o nome da COLUNA ou LINHA, usamos. rename
#Se você quiser mudar o conteúdo de uma célula usamos .loc ou .iloc

for i in range(len(base_alunos)):
    if base_alunos.loc[i,"Curso"] == "ADM":
        base_alunos.loc[i, "Curso"] = "Administração"
    #repara que foi usado == para saber se era true e depois = para mudar
        

print(base_alunos)




