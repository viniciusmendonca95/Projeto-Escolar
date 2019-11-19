class endereco:
    def __init__(self):
        self.logradouro = ""
        self.numero = 0
        self.complemento = ""
        self.bairro = ""
        self.cidade = ""
        self.uf = ""
    def cadastrar_endereco(self):
        self.logradouro = input("Informe o logradouro: ")
        self.numero = input("Informe o número: ")
        self.complemento = input("Informe o complemento: ")
        self.bairro = input("Informe o bairro: ")
        self.cidade = input("Informe a cidade: ")
        self.uf = input("Informe a UF: ")
    def exibir_endereco(self):
        return self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.uf
