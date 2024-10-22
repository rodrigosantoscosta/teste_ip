# 5. Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. Exemplo: A[0] +
# B[0] deverá ser salva em N[0].

import random

N = []
A = []
B = []

for i in range(5):
    valor = random.randint(0 ,9)
    A.append(valor)

for i in range(5):
    valor = random.randint(0 ,9)
    B.append(valor)

for i in range(5):
    soma = A[i] + B[i]
    N.append(soma)

print(f'A matriz A:\n{A}\n')
print(f'A matriz B:\n{B}\n')
print(f'A matriz N:\n{N}\n')