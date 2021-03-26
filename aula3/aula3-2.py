# importando as bibliotecas
import pandas as pd

# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
print(df)

# leitura de planilhas excel
# 2 abas (worksheets)

# leitura do arquivo todo
excel_file = pd.ExcelFile("https://pycourse.s3.amazonaws.com/temperature.xlsx")

# leitura da primeira aba (Sheet1)
# dados numéricos com separador decimal = '.'
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
print(df2)

# leitura da segunda aba (Sheet2)
# dados numéricos com separador decimal = ','
df3 = pd.read_excel(excel_file, sheet_name='Sheet2')
df3['temperatura'] = df3['temperatura'].str.replace(',', '.').astype('float')
print(df3)

# visualizando as primeiras n linhas
n = 3
df.head(n)

# visualizando as últimas n linhas
n = 3
df.tail(n)

# dtypes
df.dtypes

# estatísticas básicas
df.describe()

# dataframe info
df.info()

# nomes das colunas
df.columns  # é possível alterar
