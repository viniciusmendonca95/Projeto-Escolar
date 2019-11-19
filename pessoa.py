import endereco as e

class pessoa:
    def __init__(self):
        self.nome = ""
        self.celular = 0
        self.email = ""
        self.e = e.endereco()
        self.pessoa = {}
    def cadastrar_pessoa(self):
        self.nome = input("Informe o nome: ")
        self.celular = input("Informe o celular: ")
        self.email = input("Informe o email: ")
        self.e.cadastrar_endereco()
        logradouro, numero, complemento, bairro, cidade, uf = self.e.exibir_endereco()
        self.pessoa = {'nome': self.nome, 'celular': self.celular, 'email': self.email, 'logradouro': logradouro,
                       'numero': numero, 'complemento': complemento, 'bairro': bairro, 'cidade':
                           cidade, 'uf': uf}
    def exibir_pessoa(self):
        return self.pessoa