""" Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora. """


class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome,
        self.idade = idade,
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"

def cadastrarUsuario(lista):
     while True:
        nome = input('Digite o nome do usuario: ')
        idade = input('Digite a idade do usuario: ')
        email = input('Digite o email do usuario: ')
        
        if nome == idade == email == '0':
             break
        usuario = Usuario(nome, idade, email)
        lista.append(usuario)

""" def exibirUsuarios(lista):
    for i in range(0, len(lista)):
        print (str(lista[i])) """

if __name__ == '__main__':
    lista = []
    cadastrarUsuario(lista)
    print(*lista)