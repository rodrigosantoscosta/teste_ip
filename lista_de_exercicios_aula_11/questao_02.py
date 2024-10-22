# 2. Escreva um algoritmo que permita a leitura das notas de uma turma de 5 alunos. Depois responda:
# a. Qual a média da turma?
# b. Quantos alunos obtiveram nota acima da média da turma?
# c. Imprimir a média da turma e o resultado da contagem.

notas = []
somaDasNotas = 0

for i in range(5):
    nota = float(input(f'Digite a nota nº{i + 1}: '))
    notas.append(nota)

for i in range(5):
    somaDasNotas = somaDasNotas + notas[i]

mediaDaTurma = somaDasNotas / 5

print(f'Média da turma: {mediaDaTurma:,.1f}\n')

notasAcimaDaMedia = 0

for i in range(5):
    nota = notas[i]    
    if nota > mediaDaTurma:
        notasAcimaDaMedia += 1

print(f'{notasAcimaDaMedia} alunos(s) tiveram notas acima da média.')