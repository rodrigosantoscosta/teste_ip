# Conversor de Decimal para Binário:
# Contexto: Desenvolva um programa que converta um número decimal fornecido pelo usuário para sua representação binária. Utilize um loop para realizar as divisões sucessivas por 2 e armazenar os restos.

def converteParaBinario(numero):
    quociente = 1
    resultado = ''
    resto = 1
    
    while not(quociente == 0):
        quociente = numero // 2
        resto = numero % 2
        #print(resto)
        resultado = resultado + str(resto)
        numero = numero // 2
    
    #Inverte a string
    resultado = resultado[::-1]
    
    return resultado

if __name__ == '__main__':
    numero = int(input('Digite um numero na base decimal para converter para binario: '))
    
    print(f'{numero} na base binaria = {converteParaBinario(numero)}')