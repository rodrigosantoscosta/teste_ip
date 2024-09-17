from sys import argv

with open('aula05_TED/vingadores.txt', 'r') as listaVingadores:
    for each in listaVingadores:
        print(f'Saudações, {each.strip()}!')