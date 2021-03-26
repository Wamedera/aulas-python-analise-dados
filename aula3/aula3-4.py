# importando as bibliotecas
import pandas as pd

# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

df.head()

# seleção de uma coluna
df['temperatura']

# tipo
type(df['temperatura'])

# seleção de múltiplas colunas
df[['date', 'classification', 'temperatura']]

# tipo
type(df[['date', 'classification']])

# indexação por índice
# selecionado todas as linhas e a coluna 1
# coluna 1: temperatura
a = df.iloc[:, 1]

# indexação por nome
# selecionado todas as linhas e a coluna 1
df.loc[:, 'temperatura']

# indexação por índice de múltiplas colunas
df.iloc[:, 1:]

# indexação por nome de múltiplas colunas
df.loc[:, ['temperatura', 'classification']]

# indexação por nome de múltiplas colunas
df.loc[:, 'temperatura':]
