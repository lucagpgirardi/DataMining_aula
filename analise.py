import pandas as pd

# Lista dos arquivos com sep = ";" e que precisam de pouco tratamento (dados anuais)
arquivos = ['pib.csv', 'fbkf_maq.csv', 'FBKF.csv', 'fbkf_constru.csv', 'PIB_comercio.csv', 'PIB_constucaocivil.csv', 'PIB_demanda_familias.csv', 'PIB_eletrico.csv', 'pib_exportacoes.csv', 'pib_importacoes.csv', 'PIB_ind_extrativa_mineral.csv', 'pib_ind_transformacao.csv', 'IGPM.csv', 'IPCA.csv']
print(len(arquivos))
#Lista dos arquivos com sep = ";", com valores entre aspas e com Datas mensais
arquivos_pontovirgula = ['ptax.csv','resultado_primario.csv', 'ied.csv', 'dbgg_pib.csv']
print(len(arquivos_pontovirgula))
# Inicializar o DataFrame final com o primeiro arquivo
df_final = pd.read_csv(arquivos[0], sep=",")
df_final = df_final.iloc[:,:2]  # Selecionar apenas as duas primeiras colunas

# Mesclar cada arquivo restante com o DataFrame final
for arquivo in arquivos[1:]:
    df = pd.read_csv(arquivo, sep=",")
    df = df.iloc[:,:2]  # Selecionar apenas as duas primeiras colunas
    df_final = pd.merge(df_final, df, on="Data", how="outer")

#Vamos tratar os arquivos com ;, fazendo a mediana dos valores mensais, anualizando-os
#Vamos também usando pd.to_datetime transformar as datas em ano
for arquivo in arquivos_pontovirgula:
    df = pd.read_csv(arquivo, sep=';', quotechar='"')
    # Remover as aspas e converter os dados para float
    df['Data'] = df['Data'].str.replace('"', '')
    coluna_valor = df.columns[1]
    df[coluna_valor] = df[coluna_valor].str.replace('"', '').str.replace(',', '.').astype(float)

    # Converter 'Data' para datetime e extrair o ano
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.year

    # Calcular a mediana para cada ano
    df = df.groupby('Data', as_index=False).median()

    # Mesclar o DataFrame processado com o DataFrame final
    df_final = pd.merge(df_final, df, on="Data", how="outer")

#Selic.csv tem sep = ",", mas tem valores diários que temos que anualizar pela mediana
selic = pd.read_csv('selic.csv', usecols=[0, 1], parse_dates=['Data'], dayfirst=True)

# Agrupar os dados por ano e calcular a mediana dos valores diários
selic['Ano'] = selic['Data'].dt.year
selic_anualizada = selic.groupby('Ano').agg({'Selic Meta': 'median'}).reset_index()

# Criar a coluna de Data apenas com o ano
selic_anualizada['Data'] = selic_anualizada['Ano']

# Reordenar as colunas para que 'Data' seja a primeira coluna
selic_anualizada = selic_anualizada[['Data', 'Selic Meta']]
#Último merge adicionando a selic
df_final = pd.merge(df_final, selic_anualizada, on ="Data", how="outer")

# Salvar o DataFrame final como CSV
pasta = r"C:\Users\lucag\Downloads\DataMining\base_tratada.csv"
df_final.to_csv(pasta, index=False)

#Descobrindo o encoding da base gerada
with open('base_tratada.csv') as f:
    print(f)