# Calculadora de Média de Notas:
# Contexto: Crie um programa que peça ao usuário para inserir várias notas de um aluno e calcule a média. Utilize um loop para continuar pedindo notas até que o usuário digite um valor específico para encerrar a entrada (por exemplo, -1).

totalNotas = 0
quantidadeNotas = 0
somaNotas = 0

while True:
    nota = float(input('Digite a a nota, para exibir a média digite -1: '))
    if nota == -1:
        break
    somaNotas = somaNotas + nota
    quantidadeNotas = quantidadeNotas + 1

if quantidadeNotas > 0:
    media = somaNotas / quantidadeNotas
    print(f'A media é {(media):,.2f}')
else:
    print('Digite pelo menos uma nota, tente novamente.')