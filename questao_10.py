# Simulador de Lançamento de Dados:
# Contexto: Implemente um programa que simule o lançamento de um dado de 6 faces várias vezes, conforme especificado pelo usuário. Utilize um loop para realizar os lançamentos e exibir os resultados.
import random

def jogarDado():
    return random.randrange(1, 6)

if __name__ == '__main__':
    vezes = int(input('Digite quantas vezes você quer que o dado seja lançado: '))

    for i in range (1, vezes + 1):
        print (f'Resuldado do {i}° lançamento: {jogarDado()}')