""" Faça um programa que receba um número e que calcule a tabuada desse número, e armazene o resultado em um arquivo de texto.
 """
from sys import argv

def calculaTabuada(numero):
    resultado = ""
    for i in range(1, 11):
        
        print(f'{numero} X {i} = {numero * i}')
        resultado = resultado + (f'{numero} X {i} = {numero * i}\n')
    return resultado

#Recebe um arquivo txt e imprime nele
def salvaEmArquivo(arquivo, conteudo):
    with open(arquivo, 'w') as arquivo:
        arquivo.write(conteudo)


if __name__ == '__main__':
    numero = int(input('Digite um numero para calcular a tabuada: '))
    tabuada = calculaTabuada(numero)
    
    arquivo = 'tabuada.txt' #Quando executado cria um arquivo com o nome tabuada.txt
    salvaEmArquivo(arquivo, tabuada)