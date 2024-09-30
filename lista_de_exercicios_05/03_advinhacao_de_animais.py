""" Descrição: Imagine que você é um mago que pode adivinhar o animal favorito das pessoas.
Crie um programa que pergunte à pessoa se seu animal favorito é mamífero ou réptil. Se for
mamífero, o programa deve sugerir que é um cachorro; se for réptil, o programa deve sugerir
que é uma tartaruga. """

animal_favorito = input('O seu animal favorito é mamifero ou reptil?, digite ele: ')

if animal_favorito == 'mamifero':
    print('Seu animmal favorito é um cachorro')

elif animal_favorito == 'reptil':
    print('Seu animal favorito é um reptil')
else:
    print('Digite novamente.')