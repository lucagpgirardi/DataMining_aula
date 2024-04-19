import pandas as panda
#Primeiro exercício
renda = panda.read_csv('https://github.com/danieltb3006/DM_Ibmec/raw/main/base_renda_atualizado.csv')
renda.info()
renda["UF"] = renda["UF"].astype("category")
renda["Genero"] = renda["Genero"].astype("category")
renda.info()
#Exercício dois
#Para dividir todas as células de uma coluna,
#usamos o comando .div(numero)
print(renda["Renda"])
renda["Renda"] = renda["Renda"].div(1412)
print(renda.head)

#Exercício 3
#para inserir uma nova coluna podemos simplesmente
#Usar .insert(loc=posição, collumn="nome da coluna", valores=[])
#Ou podemos renda["nova coluna"] e ela é colocada no final

for i in range (len(renda)):
    if renda.loc[i,"Idade"] > 0 and renda.loc[i,"Idade"] <= 14:
        renda.loc[i, "Faixa_etaria"] = "Criança"
    elif renda.loc [i,"Idade"] > 18 and renda.loc[i,"Idade"]  <= 60:
        renda.loc[i, "Faixa_etaria"] = "Adolescente"
    
print(renda["Faixa_etaria"])

