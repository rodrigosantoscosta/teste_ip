#Desenvolva um programa que verifique e mostre os numeros entre 1000 e 2000 que, quando divididos por 11 produzam o resto igual a 5


def calculaResto():
    for i in range (1000, 2001):
        if i % 11 == 5:
            print(i)    

if __name__ == '__main__':
    calculaResto()