# Desenho de Padrões com Caracteres:
# Contexto: Crie um programa que desenhe padrões simples com caracteres, como triângulos, quadrados ou losangos. Utilize loops aninhados para controlar a quantidade de linhas e colunas e a exibição dos caracteres.

def desenhaTriangulo(numero):
    for i in range(numero):
        print(' ' * (numero - i - 1) + '*' * (2 * i + 1))
    print('\n')

def desenhaQuadrado(numero):
    for i in range(numero):
        print('*' * numero)
    print('\n')

def desenhaLosango(numero):
    for i in range(numero):
        print(' ' * (numero - i - 1) + '*' * (2 * i + 1))
    for i in range(numero - 2, -1, -1):
        print(' ' * (numero - i - 1) + '*' * (2 * i + 1))
    print('\n')

if __name__ == "__main__":
   
    numero = int(input("Digite a altura/lado dos desenhos: "))
    
    desenhaTriangulo(numero)
    desenhaQuadrado(numero)
    desenhaLosango(numero)
