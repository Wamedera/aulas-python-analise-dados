# importando as bibliotecas
import pandas as pd

# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

# groupby: agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification')

# groupby: agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification').mean()

# groupby: agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification').sum()

# drop: remoção de uma coluna
df.drop('temperatura', axis=1)

# cópia de um dataframe: evita compartilhamento de memória
# sem copy(), operações inplace em df2 também alteram df
# df2 = df.copy()
df2 = df

# argumento inplace
# inplace=True aplica a transformação no próprio objeto
df3 = df2.drop("temperatura", axis=1)

# argumento inplace
# inplace=True aplica a transformação no próprio objeto
df2.drop("temperatura", axis=1, inplace=True)
