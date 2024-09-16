def castFeitico(escolha):
    match escolha:
        case 1:
            print('Feitiço do tipo fogo')
        case 2:
            print('Feitiço do tipo água')
        case 3:
            print('Feitiço do tipo terra')
            
        case _:
            print('Tente novamente')

if __name__ == '__main__':
    
    escolha = int(input('Escolha "1" , 2" ou "3" para lançar um feitiço: '))
    castFeitico(escolha)