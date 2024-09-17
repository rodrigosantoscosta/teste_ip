from sys import argv

with open('vingadores.txt', 'r') as listaVingadores:
    for each in listaVingadores:
        print(f'Saudações, {each.strip()}!')