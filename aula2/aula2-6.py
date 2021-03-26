import numpy as np

# criação de dois arrays x e y
x = np.ones((2, 2))
y = np.eye(2)
print('x:\n', x)
print('y:\n', y)

# soma
print('soma de dois arrays:\n', x + y)
print('soma com float/int:\n', x + 2)  # broadcasting

# subtração
print('subtração de dois arrays:\n', x - y)
print('subtração com float/int:\n', x - 2)  # broadcasting

# divisão
print('divisão de dois arrays:\n', x / y)
print('divisão com float/int:\n', x / 2)  # broadcasting

# quando o broadcasting não funciona
# np.array([1, 2, 3]) + np.array([1, 2])
