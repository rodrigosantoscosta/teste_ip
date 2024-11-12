# Escreva um algoritmo que permita a leitura dos nomes de 5 clubes de futebol e armazene os nomes
# lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e
# depois escrever a mensagem ACHEI, se o nome estiver entre os 5 nomes lidos anteriormente
# (guardados no vetor), ou NÃO ACHEI caso contrário.

listaDeClubes = []

for i in range(len(listaDeClubes)):
    time = input('Digite um clube de futebol: ')
    listaDeClubes.append(time)

busca = input('Digite o clube que voce quer achar na lista: ')

for i in range(len(listaDeClubes)):
    if busca == listaDeClubes[i]:
        print('Achei')
    else:
        print('Não achei')