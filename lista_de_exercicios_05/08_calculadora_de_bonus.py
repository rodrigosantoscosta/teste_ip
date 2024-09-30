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