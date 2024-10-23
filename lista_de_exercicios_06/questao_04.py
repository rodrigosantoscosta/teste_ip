""" Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada pessoa acessando cada elemento da lista um de cada vez """
from sys import argv

def salvaEmArquivo(arquivo, conteudo):
    with open(arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

def adicionaAmigos(listaDeAmigos):
    while True:
        entrada = input('Digite o nome de um amigo (caso não queira adicionar mais amigos na lista digite "0"): ')
        if entrada == '0':
            break
        listaDeAmigos.append(entrada)

def exibirListaDeAmigos(listaDeAmigos):
    
    for i in range(0, len(listaDeAmigos)):
       print(listaDeAmigos[i]) 

if __name__ == '__main__':
    listaDeAmigos = []
    adicionaAmigos(listaDeAmigos)
    exibirListaDeAmigos(listaDeAmigos)