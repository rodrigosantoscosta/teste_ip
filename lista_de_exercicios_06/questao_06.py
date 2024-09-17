""" Seja criativo ao desenvolver este programa.

*Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.

*Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.

*Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.

*Modifique sua lista, substitua os desistentes por novos convidados.

*Exiba um novo convite para cada pessoa que continua presente em sua lista.
 """

from sys import argv

def salvaEmArquivo(arquivo, conteudo):
    with open(arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

def enviarConvites(listaDeConvidados):
    while True:
        entrada = input('Digite o nome de um amigo (caso não queira adicionar mais amigos na lista digite "0"): ')
        if entrada == '0':
            if len(listaDeConvidados) >= 5:
                break
            else:
                print(f'Voce so convidou {len(listaDeConvidados)} pessoas, convide pelo menos 5.')
        listaDeConvidados[entrada] = True

def confirmaPresenca(listaDeConvidados):
    listaAuxiliar = listaDeConvidados
    for key in listaAuxiliar:
        entrada = input(f'Voce {key} esta convidado para o evento, deseja participar? Responda com "Sim" ou "Não": ')   
        listaDeConvidados[key] = True if entrada == 'Sim' else False
        if not(entrada == 'Sim'):
            del listaDeConvidados[key]
            entrada = input(f'Adicione uma pessoa para substituir {key}: ')
            listaDeConvidados[entrada] = True

if __name__ == '__main__':

    listaDeConvidados = {}
    enviarConvites(listaDeConvidados)
    print(listaDeConvidados)
    confirmaPresenca(listaDeConvidados)
    print(listaDeConvidados)


""" # Creating a hash map (dictionary)
hash_map = {}

https://www.geeksforgeeks.org/hash-map-in-python/

# Adding key-value pairs
hash_map["name"] = "Alice"
hash_map["age"] = 25
hash_map["city"] = "New York"

# Accessing values
print(hash_map["name"])  # Output: Alice
print(hash_map["age"])   # Output: 25

# Modifying values
hash_map["age"] = 26

# Removing key-value pairs
del hash_map["city"]

# Checking for keys
if "name" in hash_map:
    print("Name is in the hash map") """
