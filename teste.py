import numpy as np

# beta representa beta1 sem utilizar a função np.linalg.pinv()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [3, 5, 7, 9, 11, 13, 15, 17, 19]

# transformando para numpy e vetor coluna
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

# adicionando bias: para estimar o termo b
X = np.hstack((x, np.ones(x.shape)))

print('\nX:\n', X)

x_tr = X.T

print('\nx trans:\n', x_tr)

x_tr_x = np.dot(x_tr, X)

print('\nx trans x:\n', x_tr_x)

x_tr_x_inv = np.linalg.inv(x_tr_x)

print('\nx trans x inv:\n', x_tr_x_inv)

x_tr_x_inv_x_tr = np.dot(x_tr_x_inv, x_tr)

print('\nx trans x inv x trans:\n', x_tr_x_inv_x_tr)

beta = np.dot(x_tr_x_inv_x_tr, y)
beta1 = np.linalg.pinv(X).dot(y)

print()
print(beta)
print()
print(beta1)
