import numpy as np

# help(np.array)

# criação de um array 1D: [1, 2, 3]
l = [1, 2, 3]
x = np.array(l)
print('x:\n', x)
print('shape: ', x.shape)
print(type(x))


# criação de um array 2D: listas aninhadas
l = [[1, 2], [3, 4]]
x = np.array(l, dtype=int)
print('x:\n', x)
print('shape: ', x.shape)
print(type(x))
print(type(x[0, 0]))


# array contendo apenas 0's
dim = (2, 2)  # (linhas, colunas)
x = np.zeros(dim)
print('x:\n', x)
print('shape: ', x.shape)
print(type(x))


# array contendo apenas 1's
dim = (12, 9)  # (linhas, colunas)
x = np.ones(dim)
print('x:\n', x)
print('shape: ', x.shape)
print(type(x))


# criação de valores dentro de um intervalo
# valores uniformes entre 5 e 15
x_min, x_max = 5, 17
x = np.linspace(start=x_min, stop=x_max, num=6)
print('x:\n', x)
print('shape: ', x.shape)


# criação da matriz identidade
n = 7
x = np.eye(n)
print('x:\n', x)
print('shape: ', x.shape)


# criação de valores aleatórios
# np.random.seed(10) -> gera números aleatórios predeterminados
x = np.random.random(size=(4, 7))
print('x:\n', x)
print('x:', x.shape)
