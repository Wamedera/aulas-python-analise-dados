import numpy as np

# array
x = np.array([[1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]])
print('x:\n', x)

# reshape: transformar a matriz em um vetor coluna
# (3, 3) vira (9, 1): 3 * 3 = 9 * 1 = 9
print('Transformação de x em um vetor coluna:\n', x.reshape(9, 1))

# transposição de matriz
print('x transposta:\n', x.T)

# np.sum: soma em um dado eixo, axis = {0: linha, 1: coluna}
print('x:\n', x)
print('Soma de todos os elementos de x: ', np.sum(x))
print('Soma de x ao longo das linhas: ', np.sum(x, axis=0))
print('Soma de x ao longo das colunas: ', np.sum(x, axis=1))

# np.mean: média em um dado eixo, axis = {0: linha, 1: coluna}
print('x:\n', x)
print('Média de todos os elementos de x: ', np.mean(x))
print('Média de x ao longo das linhas: ', np.mean(x, axis=0))
print('Média de x ao longo das colunas: ', np.mean(x, axis=1))

# np.median: mediana em um dado eixo, axis = {0: linha, 1: coluna}
print('x:\n', x)
print('Mediana de todos os elementos de x: ', np.median(x))
print('Mediana de x ao longo das linhas: ', np.median(x, axis=0))
print('Mediana de x ao longo das colunas: ', np.median(x, axis=1))

# np.where: identificação dos índices onde uma dada condição
# é atendida. Uso conjunto com indexação booleana
cond = x % 2 == 0  # números pares
print('Condição:\n', cond)
i, j = np.where(cond)  # índices x[i, j] = x[cond]
print('Índice i (linhas):', i)
print('Índice j (colunas):', j)

# indexação booleana e slicing: selecionar as linhas
# de x que possuem algum número par
print('x:\n', x)
cond = x % 2 == 0  # números pares
print('Condição\n', cond)

# se houver alguma condição True na linha, a soma será maior que 0
i_row = np.where(np.sum(cond, axis=1))[0]
print('Índice das linhas que possuem números pares: ', i_row)
print('Linhas que possuem números pares:\n', x[i_row, :])
