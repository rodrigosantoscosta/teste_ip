# 1. Escreva um algoritmo que permita a leitura dos nomes de 5 clubes de futebol e armazene os nomes
# lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e
# depois escrever a mensagem ACHEI, se o nome estiver entre os 5 nomes lidos anteriormente
# (guardados no vetor), ou NÃO ACHEI caso contrário.


listaDeTimes = []

for i in range(5):
    time = input('Digite o nome de um time de futebol: ')
    listaDeTimes.append(time)

busca = input('Digite um outro time de futebol para buscar na lista de times: ')
achei = False

for i in range(5):
    if busca == listaDeTimes[i]:
        achei = True
        break

if achei:
    print('Achei')
else:
    print('Não achei')