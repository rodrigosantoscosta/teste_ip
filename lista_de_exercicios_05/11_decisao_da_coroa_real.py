""" Descrição: O conselho real precisa tomar uma decisão crítica: selecionar o próximo
governante entre três candidatos, baseado na sua pontuação em uma série de provas. Crie um
programa que receba as notas dos três candidatos e determine qual deles teve a maior média.
Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando
que há um empate. """

mediaPrimeiro = float(input('Digite a media do primeiro candidato: '))
mediaSegundo = float(input('Digite a media do segundo candidato: '))
mediaTerceiro = float(input('Digite a media do terceiro candidato: '))

if mediaPrimeiro >= 0 and mediaSegundo >=0 and mediaTerceiro >=0:
    if mediaPrimeiro > mediaSegundo and mediaPrimeiro > mediaTerceiro:
        print('O primeiro candidato é o novo governante')
    elif mediaSegundo > mediaPrimeiro and mediaSegundo > mediaTerceiro:
        print('O segundo candidato é o novo governante')
    elif mediaTerceiro > mediaPrimeiro and mediaTerceiro > mediaSegundo:
        print('O terceiro candidato é o novo governante')
    elif mediaPrimeiro == mediaSegundo and mediaPrimeiro == mediaTerceiro:
        print('Há um empate entre os três candidatos.')
    elif mediaPrimeiro == mediaSegundo:
        print('Há um empate entre o primeiro e o segundo candidato.')
    elif mediaPrimeiro == mediaTerceiro:
        print('Há um empate entre o primeiro e o terceiro candidato.')
    elif mediaSegundo == mediaTerceiro:
        print('Há um empate entre o segundo e o terceiro candidato.')
else:
    print('Tente novamente.')