# Escolha de Feitiços 
# a. Descrição: Um mago tem três feitiços: fogo, água e terra. Crie um programa que receba a escolha do usuário (1 para fogo, 2 para água, 3 para terra) e use o comando match-case para exibir o feitiço escolhido. 
# b. Conceito: Match-case, variáveis. 

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