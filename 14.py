""" Descrição: Um sábio está julgando um duelo entre dois guerreiros. Ele quer saber qual
guerreiro deve ser considerado vencedor, com base em suas habilidades de ataque e defesa.
Crie um programa que receba os valores de ataque e defesa dos dois guerreiros e determine o
vencedor (aquele com maior soma de ataque e defesa). Se houver empate, o programa deve
considerar a defesa como critério de desempate. """

class Guerreiro:
    def __init__(self, ataque, defesa):
        self.ataque = ataque
        self.defesa = defesa
    def somaAtributos(self):
        return self.ataque + self.defesa

ataque_primeiro, defesa_primeiro = map(float,(input('Digite o ataque e defesa do primeiro guerreiro: ')).split())
ataque_segundo, defesa_segundo  = map(float,(input('Digite o ataque e defesa do segundo guerreiro: ')).split())

soma_primeiro = ataque_primeiro + defesa_primeiro
soma_segundo = ataque_segundo + defesa_segundo


if ataque_primeiro < 0 or defesa_primeiro < 0 or ataque_segundo < 0 or defesa_segundo < 0:
    print('Digite valores válidos.')

if soma_primeiro > soma_segundo:
    print('O primeiro guerreiro venceu.')
if soma_segundo > soma_primeiro:
    print('O segundo guerreiro venceu.')

if soma_primeiro == soma_segundo:
    if defesa_primeiro > defesa_segundo:
        print('O primeiro guerreiro venceu, sua defesa é maior.')
    elif ataque_primeiro == ataque_segundo and defesa_primeiro == defesa_segundo:
        print('Os dois guerreiros tem os mesmos atributos de ataque e defesa')
    else:
        print('O segundo guerreiro ganhou, sua defesa é maior.')