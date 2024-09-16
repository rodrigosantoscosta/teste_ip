""" Descrição: Um botânico está classificando plantas mágicas em uma floresta. Ele quer saber se
uma planta é pequena (menos de 1 metro), média (entre 1 e 3 metros), ou grande (mais de 3
metros). Crie um programa que receba a altura da planta e informe a sua classificação."""

def classificaPlantasMagicas(alturaPlanta):
    
    if alturaPlanta > 0 and altura < 1:
        print('É uma planta pequena.')
    elif alturaPlanta >= 1 and altura <= 3:
        print('É uma planta média.')
    elif alturaPlanta > 3:
        print('É uma planta grande.')
    else:
        print('Tente outra vez.')

if __name__ == '__main__':
    altura = float(input('Digite a altura da planta em metros: '))
    classificaPlantasMagicas(altura)
