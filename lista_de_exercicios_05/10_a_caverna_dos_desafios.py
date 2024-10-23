""" Descrição: Um aventureiro encontrou uma caverna cheia de portas, cada uma com um número
de 1 a 5. Atrás de cada porta há um desafio. Crie um programa que receba o número da porta
escolhido pelo aventureiro e use match-case para mostrar qual desafio ele enfrentará. """

escolha = int(input('Escolha um numero de 1 a 5'))

match escolha:
    case 1:
        print('Desafio 1')
    case 2:
        print('Desafio 2')
    case 3:
        print('Desafio 3')
    case 4:
        print('Desafio 4')
    case 5:
        print('Desafio 5')