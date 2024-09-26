# Verificador de Número Primo:
# Contexto: Crie um programa que peça ao usuário um número inteiro e verifique se ele é primo. Utilize um loop para testar a divisibilidade do número por outros números menores.


def ehPrimo(numero):

    if numero > 1:
        for i in range (2, numero):
            if numero % i == 0:
                return False
            
            else:
                return True
    else:
        False

if __name__ == '__main__':
    numero = int(input('Digite um numero para verificar se é primo'))

    if ehPrimo(numero):
        print('É primo')
    else:
        print('Não é primo')
