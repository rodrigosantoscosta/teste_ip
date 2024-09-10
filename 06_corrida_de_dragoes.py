""" Descrição: Em um campeonato de corrida de dragões, cada dragão corre uma determinada distância em um certo tempo. Crie um programa que receba a distância e o tempo de dois dragões diferentes e determine qual dragão é mais rápido, ou se ambos têm a mesma velocidade. """

distancia1, tempo1 = map(float, input('Digite a distancia em km e o tempo em horas do primeiro dragao: ').split())
distancia2, tempo2 = map(float, input('Digite a distancia em km e o tempo em horas do segundo dragao: ').split())
velocidade_dragao1 = distancia1 / tempo1
velocidade_dragao2 = distancia2 / tempo2

if velocidade_dragao1 == velocidade_dragao2:
    print('A velocidade dos dois é igual')
elif velocidade_dragao1 > velocidade_dragao2:
    print('O primeiro dragao é mais rapido')
elif velocidade_dragao1 < velocidade_dragao2:
    print('O segundo dragao é mais rapido')
else:
    print('Tente novamente')
