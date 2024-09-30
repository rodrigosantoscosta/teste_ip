# Sequência de Fibonacci:
# Contexto: Desenvolva um programa que gere os primeiros N números da sequência de Fibonacci, onde N é fornecido pelo usuário. Utilize um loop para calcular e exibir os termos da sequência.


def calculaFibonaci(numero):
    primeiroNumeroFibonaci = 0
    segundoNumeroFibonaci = 1
    proximoNumero = segundoNumeroFibonaci
    
    for i in range (numero):
        print(proximoNumero)
        primeiroNumeroFibonaci = segundoNumeroFibonaci
        segundoNumeroFibonaci = proximoNumero
        proximoNumero = primeiroNumeroFibonaci + segundoNumeroFibonaci


if __name__ == "__main__":
    
    numero = int(input('Digite quantos numeros da sequencia de Fibonaci a serem exibidos: '))
    calculaFibonaci(numero)