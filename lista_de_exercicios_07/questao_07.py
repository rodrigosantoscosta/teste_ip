# Contexto: Implemente um programa que calcule o fatorial de um número fornecido pelo usuário. Utilize um loop para realizar as multiplicações necessárias.

def calculaFatorial(numero):
    fatorial = 1
    
    for i in range (1, numero + 1):
        fatorial = fatorial * i
    
    return fatorial

if __name__ == '__main__':
    
    numero = int(input('Digite um numero para calcular o fatorial: '))

    print(f' O fatorial de {numero} é igual a {calculaFatorial(numero)}.')

