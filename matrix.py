import random 
matrix =  []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(random.randint(0, 9))
    matrix.append(linha)

print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
    print('\n')