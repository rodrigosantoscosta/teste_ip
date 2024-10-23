# 6. Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número
# qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve gerar um novo
# vetor sem esse número. (Considere que não há números repetidos no vetor).

vetor = []

for i in range(20):
    valor = int(input(f'Digite o elemento nº {i} do vetor: '))
    vetor.append(valor)

print(f'Vetor: {vetor}\n')

busca = int(input('Digite o valor a ser buscado no vetor: '))
achei = False

for i in range(len(vetor)):  
    if vetor[i] == busca:
        print(f'O numero {busca} está no vetor.')
        vetor.remove(busca)
        achei = True
        
        break

if not achei:
    print(f'O numero {busca} não está no vetor')

print(f'Novo vetor: {vetor}')