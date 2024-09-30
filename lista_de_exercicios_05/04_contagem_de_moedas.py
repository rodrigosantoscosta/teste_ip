""" Descrição: Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de 25 centavos. Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o valor total que o colecionador tem. 
 """
quantidade_1real = int(input('Digite a quantidade de moedas de 1 real: '))
quantidade_50centavos = int(input('Digite a quantidade de moedas de 50 centavos: '))
quantidade_25centavos = int(input('Digite a quantidade de moedas de 25 centavos: '))

print(f'O valor total é: R$ {((quantidade_1real) + (quantidade_50centavos * 0.50) + (quantidade_25centavos * 0.25)):,.2f}')
