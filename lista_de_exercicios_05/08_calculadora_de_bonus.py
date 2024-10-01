# Calculadora de Bônus 
# a. Descrição: Um rei deseja distribuir bônus aos seus cavaleiros com base em suas conquistas. Se um cavaleiro completou mais de 10 missões, ele recebe um bônus de 100 moedas de ouro. Se completou entre 5 e 10 missões, recebe 50 moedas de ouro. Se completou menos de 5, recebe 10 moedas de ouro. Crie um programa que receba o número de missões completadas e informe o valor do bônus. 
# b. Conceito: Desvio condicional aninhado, operadores relacionais. 

def bonus(numeroMissoes):
    
    if numeroMissoes > 10:
        print(f'Numero de missoes: {numeroMissoes}\nBonus: 100 moedas de ouro')
    elif numeroMissoes >= 5 and numeroMissoes <= 10:
        print(f'Numero de missoes: {numeroMissoes}\nBonus: 50 moedas de ouro')
    else:
        print(f'Numero de missoes: {numeroMissoes}\nBonus: 10 moedas de ouro')

if __name__ == '__main__':
    numeroMissoes = int(input('Digite o numero de missoes concluidas: '))
    bonus(numeroMissoes)