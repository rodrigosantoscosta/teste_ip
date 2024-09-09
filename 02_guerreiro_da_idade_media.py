""" Descrição: Um guerreiro precisa de uma armadura especial para a batalha. Para forjar a
armadura, ele precisa de uma liga metálica que combina ferro e ouro. O ferreiro diz que a liga
precisa ter no mínimo 70% de ferro. Crie um programa que receba a quantidade de ferro e
ouro em kg e verifique se a porcentagem de ferro na liga é suficiente. """

ferro = float(input('Digite a quantidade de ferro: '))
ouro = float(input('Digite a quantidade de ouro: '))
total = ferro + ouro

if ferro / total >= 7/10:
    print('Tem ferro o suficiente')
else:
    print('Não tem ferro o suficiente')