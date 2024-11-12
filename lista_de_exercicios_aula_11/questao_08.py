# 8. Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer,
# calcular e escrever quantas vezes esse número aparece no vetor.
import random

vetor = []
vezes = 0
busca = int(input('Digite o numero que voce quer buscar no vetor: '))

for i in range(30):
    vetor.append(random.randint(0, 9))

print(f'Vetor: {vetor}')

for i in range(len(vetor)):
    if vetor[i] == busca:
        vezes += 1

print(f'O numero {busca} aparece {vezes} vezes.')