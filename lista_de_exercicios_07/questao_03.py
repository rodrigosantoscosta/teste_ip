# Contador de Vogais e Consoantes:
# Contexto: Crie um programa que peça ao usuário uma frase e conte o número de vogais e consoantes presentes nela. Utilize um loop para percorrer cada caractere da frase e realizar a contagem.
numeroConsoantes = 0
numeroVogais = 0
frase = input("Digite uma frase: ").lower()
vogais =  ["a", "e", "i", "o", "u"]
consoantes = ["b", "c", "d","f", "g", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", 
"y", "z", "ç", "h"]


for i in frase:
    if i in vogais:
        numeroVogais = numeroVogais + 1
    if i in consoantes:
        numeroConsoantes = numeroConsoantes + 1

print(f'Numero de vogais na frase: {numeroVogais}\nNumero de consoantes: {numeroConsoantes}')