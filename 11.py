""" Descrição: O conselho real precisa tomar uma decisão crítica: selecionar o próximo
governante entre três candidatos, baseado na sua pontuação em uma série de provas. Crie um
programa que receba as notas dos três candidatos e determine qual deles teve a maior média.
Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando
que há um empate. """

mediaPrimeiro = float(input('Digite a media do primeiro candidato'))
mediaSegundo = float(input('Digite a media do segundo candidato'))
mediaTerceiro = float(input('Digite a media do terceiro candidato'))

if mediaPrimeiro > mediaSegundo and mediaPrimeiro > mediaTerceiro:
    print('O primeiro candidato é o novo governante')
    
