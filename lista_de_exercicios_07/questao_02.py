# Tabuada Personalizada:
# Contexto: Desenvolva um programa que peça ao usuário um número e gere a tabuada completa desse número (de 1 a 10). Utilize um loop para realizar as multiplicações e exibir os resultados de forma organizada.

def calculaTabuada(numero):
    
    for i in range(1, 11):
        print(f'{numero} X {i} = {numero * i}')


if __name__ == '__main__':
    numero = int(input('Digite o numero que voce quer exibir a tabuada: '))
    calculaTabuada(numero)
        