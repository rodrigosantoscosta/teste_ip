# 1. Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
# números repetidos no vetor VET e em que posições se encontram.

VET = []

for i in range(10):
    valor  = int(input(f'Digite o valor da posição nº {i}: '))
    VET.append(valor)

for i in range(len(VET)):
    for j in range(i + 1, len(VET)):   
        if VET[i] == VET[j]:
            print(f'Numeros repetidos nas posições {i} e {j}')
