import pandas as pd
base = pd.read_csv(('https://raw.githubusercontent.com/lucagpgirardi/DataMining/main/base_tratada.csv'), sep=",")
print(base.isnull().sum())

