""" Descrição: O sistema de defesa de um castelo mágico precisa estar sempre ativo quando o
exército do rei está fora. Crie um programa que receba a posição do exército (dentro ou fora
do castelo) e use match-case para ativar ou desativar o sistema de defesa automaticamente. """

posicao = input('Digite a posição do exercito do rei se está dentro ou fora do castelo, responda com "fora" ou "dentro": ').lower()

match posicao:
    case 'dentro':
        print('Sistemas de segurança desativado.')
    case 'fora':
        print('Sistema de segurança ativado.')
    case _:
        print('Tente novamente.')