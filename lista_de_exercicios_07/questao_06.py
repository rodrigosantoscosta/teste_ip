# Verificador de Número Primo:
# Contexto: Crie um programa que peça ao usuário um número inteiro e verifique se ele é primo. Utilize um loop para testar a divisibilidade do número por outros números menores.


def ehPrimo(numero):
    
    if numero == 2:
        return True
    
    if numero == 3:
        return True
    
    if numero > 1 :
        for i in range (1, numero + 1):
            if numero % i == 0:
                if numero > i != numero and i != 1:
                    return False
            
            else:
                return True
    else:
        False

if __name__ == '__main__':
    numero = int(input('Digite um numero para verificar se é primo: '))

    if ehPrimo(numero):
        print('É primo')
    else:
        print('Não é primo')
