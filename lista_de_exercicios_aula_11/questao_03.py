 
import random

vetorQ = []

for i in range(20):
    valor = random.randint(0, 200)
    vetorQ.append(valor)

maiorValor = vetorQ[0]
menorValor = vetorQ[0]

print(vetorQ)

for i in range(20):
    if vetorQ[i] > maiorValor:
        maiorValor = vetorQ[i]
        posicao = i

print(f"O maior valor é {maiorValor} e está na posição {posicao} do vetor.")

for i in range(20):
    if vetorQ[i] < menorValor:
        menorValor = vetorQ[i]
        posicao = i

print(f"O menor valor é {menorValor} e está na posição {posicao} do vetor.")