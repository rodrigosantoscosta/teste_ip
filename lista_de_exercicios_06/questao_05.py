""" Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.
 """

def adicionaAmigos(listaDeAmigos):
    while True:
        entrada = input('Digite o nome de um amigo (caso não queira adicionar mais amigos na lista digite "0"): ')
        if entrada == '0':
            break
        listaDeAmigos.append(entrada)

def exibirListaDeAmigos(listaDeAmigos):
    
    for i in range(0, len(listaDeAmigos)):
       print(f'Olá {listaDeAmigos[i]}, como vai você?') 

if __name__ == '__main__':
    listaDeAmigos = []
    adicionaAmigos(listaDeAmigos)
    exibirListaDeAmigos(listaDeAmigos)