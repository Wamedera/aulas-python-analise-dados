import numpy as np

""" notas = np.array([[6, 7, 6.3, 6.8], [8, 8.5, 9, 8.6], [5, 7, 8, 6.5]])

print(notas)

nova_nota = np.array([[8, 10, 9.5, 8.7]])
notas = np.vstack((notas, nova_nota))

print(notas)
 """


def inf_notas(notas_bim):
    notas_bim = []

    for i in range(5):
        nota = float(input('Digite a nota: '))
        notas_bim.append(nota)

    notas_bim = np.array([notas_bim])
    notas_bim = notas_bim.reshape(-1, 1)

    return notas_bim


notas = np.array([[1, 2, 3, 4, 5]])

opcao = int(input('Digite 1 para adicionar as notas: '))
while(opcao == 1):
    notas_bim = []

    for i in range(5):
        nota = float(input('Digite a nota: '))
        notas_bim.append(nota)

    notas_bim = np.array([notas_bim])

    notas = np.vstack((notas, notas_bim))

    opcao = int(input('Digite 1 para adicionar as notas: '))

print(notas)
print(np.linalg.inv(notas))
