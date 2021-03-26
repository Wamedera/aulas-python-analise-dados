# importando as bibliotecas
import pandas as pd

# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

# dtype
print(df.dtypes)

# transformando o tipo da coluna date para datetime
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)

# setando o índice
df = df.set_index('date')

# visualizando o índice
print(df)

# 5 primeiras linas
df.head()

# indexação booleana
# seleção de exemplos acima de 25 graus
cond = df['temperatura'] >= 25
df[cond]

# indexação booleana considerando datetime
# seleção de entradas até Março de 2020
cond = df.index <= '2020-03-01'
df[cond]

# indexação booleana considerando datetime
# seleção de entradas até Março de 2020 e
# slice na coluna classification
df.loc[df.index <= '2020-03-01', ['classification']]

# indexação booleana considerando datetime
# seleção de entradas até Março de 2020 e
# slice na coluna classification
df.iloc[df.index <= '2020-03-01', [-1]]
