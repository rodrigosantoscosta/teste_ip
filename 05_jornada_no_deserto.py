""" Descrição: Um explorador está cruzando um deserto. Ele precisa saber se a quantidade de
água que tem é suficiente para chegar ao próximo oásis. Ele calcula que precisa de 2 litros de
água para cada quilômetro. Crie um programa que receba a quantidade de água disponível e a
distância até o oásis, e informe se a água é suficiente. """

distancia = float(input('Digite a distancia em quilometros ate o oasis: '))
agua = float(input('Digite quantos litros de agua voce tem: '))

if agua / distancia >= 2:
    print('Voce tem agua o suficiente')
else:
    print('Voce nao tem agua o suficiente')