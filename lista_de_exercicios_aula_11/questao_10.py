# 10. Leia uma matriz 10 x 10 e escreva a localização (linha e a coluna) do maior valor.

import random

maio_valor = -1
matriz = []
localizacao_maior_valor = (0, 0)

for i in range(10):
    linha = []
    for j in range(10):
        
        valor = random.randint(0, 100)
        linha.append(valor)
        if valor > maio_valor:
            maio_valor = valor
            localizacao_maior_valor = (i, j)
        
    matriz.append(linha)
    

    
for i in range(10):
    for j in range(10):
        print(matriz[i][j], end=' ')
    print()
    
print(f'O maior da matriz é {maio_valor} na posição {localizacao_maior_valor}')
        