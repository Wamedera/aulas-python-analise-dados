import numpy as np

# criação de dois arrays x e y
x = np.ones((2, 2))
y = np.eye(2)
print('x:\n', x)
print('y:\n', y)

# multiplicação
print('multiplicação de dois arrays:\n', x * y)
print('multiplicação com float/int:\n', x * 2)  # broadcasting

# multiplicação matricial
print('multiplicação matricial (np.dot):\n', np.dot(x, y))
print('multiplicação matricial (@):\n', x @ y)
print('multiplicação matricial (.dot):\n', x.dot(y))

'''
Exemplo:
Solução de um sistema de equações:
    1*a + 2*b = 7
    3*a - 2*b = -11
    solução analítica: (a, b) = (-1, 4)
Matricialmente, este problema tem a seguinte forma:
    Ax = c, onde:
    -> x = [a, b]
    -> A = [[1, 2], [3, -2]]
    -> c = [7, -11]
    solução numérica: x = inv(A) @ c
'''

# definição do problema
A = np.array([[1, 2], [3, -2]])
c = np.array([7, -11])
print('A:\n', A)
print('c:\n', c)

# solução
# função np.linalg.inv([matriz]) retorna o inverso da matriz
x = np.dot(np.linalg.inv(A), c)
# x = np.linalg.inv(A) @ c
print('(a, b): ', x.ravel())
