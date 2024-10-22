# 2. Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
#   a. Imprima o resultado da soma de todos os valores da matriz no terminal;
#   b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3

import random

A = []

for linha in range(10):
    linha = []
    for coluna in range(10):
        valor = random.randint(0, 9)
        linha.append(valor)
    A.append(linha)
print('Matriz A:\n')

for linha in range(10):
    print(A[linha])
print('\n')
soma = 0

for linha in range(10):
    soma = soma + sum(A[linha])
print(f'Valor da soma de todos itens da matriz A: {soma}\n')

B = []

for linha in range(10):
    linhaB = []
    for coluna in range(10):
        linhaB.append(A[linha][coluna] * 3)
    B.append(linhaB)

print('Matriz B:\n')

for linha in range(10):
    print(B[linha])



