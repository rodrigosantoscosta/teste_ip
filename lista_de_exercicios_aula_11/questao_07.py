# 7. Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada. Calcular e escrever a
# quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.
import random
v1 = []
v2 = []

for i in range(10):
    v1.append(random.randint(0,9))

for i in range(10):
    v2.append(random.randint(0,9))
    
print(v1)
print(v2)

for i in range(len(v1)):
    for j in range(len(v2)):
        elementoV1 = v1[i]
        elementoV2 = v2[j]
        if elementoV1 == elementoV2:
            if i == j:
                print(f'O numero {v1[i]} existe nos dois vetores e na mesma posição {i}')