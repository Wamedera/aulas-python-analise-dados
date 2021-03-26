# importando as bibliotecas
import pandas as pd

# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

# plot de linhas
df.plot()

# plot de linhas: tamanho
df.plot(figsize=(10, 5))

# plot de linhas: grid
df.plot(figsize=(10, 5), grid=True)

# plot de linhas: style
df.plot(style='-o', figsize=(10, 5), grid=True)
# df.plot(style='--', figsize=(10, 5), grid=True);
# df.plot(style='-.', figsize=(10, 5), grid=True);

# plot de linhas: linewidth
df.plot(style='-o', linewidth=2, figsize=(10, 5), grid=True)

# plot de linhas: color
df.plot(style='-o', linewidth=2.5, color='red', figsize=(10, 5), grid=True)

# plot de linhas: color
df.plot(style='-o', linewidth=2.5, color='#822fb5', figsize=(10, 5), grid=True)

# plot de barras
df['classification'].value_counts().plot.bar(figsize=(10, 5),
                                             rot=0)

# plot de barras
df.plot(kind='bar', figsize=(10, 5), rot=30)

# pie plot
df['classification'].value_counts().plot.pie(autopct='%1.1f%%',
                                             shadow=True,
                                             figsize=(10, 7))
