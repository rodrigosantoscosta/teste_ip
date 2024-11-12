# Escreva um algoritmo que permita a leitura das notas de uma turma de 5 alunos. Depois responda:
# a. Qual a média da turma?
# b. Quantos alunos obtiveram nota acima da média da turma?
# c. Imprimir a média da turma e o resultado da contagem.

listaDeNotas = []


for i in range(len(listaDeNotas)):
    nota = int(input('Digite a nota '))
    listaDeNotas.append(nota)

# somaDasNotas = 0

# for i in listaDeNotas:
#     somaDasNotas = listaDeNotas[i] + somaDasNotas

# mediaDaTurma = somaDasNotas / len(listaDeNotas)

# print(f'Media da turma: {mediaDaTurma:,.2f}')
print(listaDeNotas)
