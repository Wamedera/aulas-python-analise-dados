# importando as bibliotecas
import pandas as pd

# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

# ordenação crescente por uma coluna
print(df.sort_values(by='temperatura'))
print()

# ordenação crescente por uma coluna
print(df.sort_values(by='classification'))
print()

# ordenação crescente por mais de uma coluna
print(df.sort_values(by=['classification', 'temperatura']))
print()

# ordenação decrescente por uma coluna
print(df.sort_values(by=['classification', 'temperatura'], ascending=False))
print()

# ordenação crescente pelo índice
print(df.sort_index())
print()

# ordenação decrescente pelo índice
print(df.sort_index(ascending=False))
