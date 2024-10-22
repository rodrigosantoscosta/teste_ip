# 6. Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número
# qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve gerar um novo
# vetor sem esse número. (Considere que não há números repetidos no vetor).

vetor = []

for i in range(20):
    valor = int(input(f'Digite o elemento nº{i} do vetor: '))

busca = int(input('Digite o valor a ser buscado no vetor: '))

for i in range(20):
    indice = i 
    if vetor[i] == busca:
        while(vetor[i] != busca):
            valor = int(input('Esse valor existe no vetor, tente um outro valor pra substituir na busca.'))

