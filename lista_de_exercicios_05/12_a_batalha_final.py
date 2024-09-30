""" Descrição: Um herói precisa decidir qual arma usar na batalha final. Ele tem três armas: uma
espada, um arco e uma lança. Cada arma tem um poder de ataque e uma durabilidade. A
escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que
70. Crie um programa que receba os valores de ataque e durabilidade das três armas e
determine qual é a mais adequada. Se nenhuma atender, o programa deve sugerir que o herói
busque uma nova arma. """

#Verifica se as armas são válidas de acordo com os atributos de ataque e durabilidade
def verificaArma(ataque, durabilidade):
    if ataque > 50 and durabilidade > 70:
        return True
    else:
        return False


ataqueEspada, durabilidadeEspada  = map(int, input('Digite respectivamente o poder de ataque e a durabilidade da espada: ').split())
ataqueArco, durabilidadeArco = map(int, input('Digite respectivamente o poder do ataque e a durabilidade do arco: ').split())
ataqueLanca, durabilidadeLanca = map(int, input('Digite respectivamente o poder do ataque e a durabilidade da lança: ').split())

espadaValida = verificaArma(ataqueEspada, durabilidadeEspada)
arcoValido = verificaArma(ataqueArco, durabilidadeArco)
lancaValida = verificaArma(ataqueLanca, durabilidadeLanca)

if espadaValida or arcoValido or lancaValida:
    if espadaValida:
            print('A espada é mais adequada.')       
    if arcoValido:
            print('O arco é mais adequado.')
    if lancaValida:
            print('A lança é mais adequada.')
else:
    print('Procure uma outra arma.')

    