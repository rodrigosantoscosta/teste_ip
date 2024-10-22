# 4. Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável x. Armazenar
# em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o
# vetor M.

A = []

for i in range(10):
    valor = int(input(f'Digite o valor {i} do vetor A: '))
    A.append(valor)

print(A)

x = int(input('Digite a variavel x: '))

M = []

for i in range(10):
    mult = A[i] * x
    M.append(mult)

print(f'A matriz M:\n{M}')


