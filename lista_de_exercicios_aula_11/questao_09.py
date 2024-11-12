# 9. Ler uma matriz D 5 x 5 (considere que não serão informados valores duplicados). A seguir, leia um
# número X e escreva uma mensagem indicando se o valor de X existe ou NÃO na matriz.

import random
M = 5
N = 5

# for i in range(5):
#     linha = []
#     for j in range(5):
#         linha.append(random.sample(range(9), 1))
#     matriz.append(linha)

matrix = [[random.randint(0 , 9) for _ in range(N)] for _ in range(M)]

print(matrix)