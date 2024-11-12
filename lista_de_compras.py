lista_de_compras = []
status = -1

def exibir_menu():
    print('\n------------MENU=---------')
    print('1 - Adicionar um item')
    print('2 - Remover item')
    print('3 - Exibir lista')
    print('4 - Sair do programa')
    print('---------------------------')
    
while status != 4:
    exibir_menu()
    try:
        status = int(input('Digite a opção do menu: '))
    except: 
        print('Tente novamente com um valor valido.')
    
        
    match status:
        case 1:
            lista_de_compras.append(input('Digite o item que você quer adicionar na lista de compras: '))
        
        case 2:
            lista_de_compras.remove(input('Digite o item que você quer remover da lista de compras: '))
        
        case 3:
            print('Lista de compras: ')
            for i in range(len(lista_de_compras)):
                print(f'{i + 1} - {lista_de_compras[i]}')
        case 4:
            status = 4
        
        case _:
            print('Digite um valor valido para opção do menu: ')