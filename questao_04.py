# Jogo de Adivinhação:
# Contexto: Implemente um jogo onde o computador escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar. Utilize um loop para permitir que o usuário faça várias tentativas, fornecendo dicas (maior ou menor) a cada tentativa.
from random import randrange
numeroAleatorio = randrange(1, 100)
tentativa = 0

while True:
    tentativa = int(input('Tente advinhar um numero entre 1 e 100: '))
    
    if tentativa == numeroAleatorio:
        print(f'Voce acertou! O numero é {numeroAleatorio}')
        break
    if tentativa > numeroAleatorio:
        print('O numero é menor.')
    if tentativa < numeroAleatorio:
        print('O numero é maior.')