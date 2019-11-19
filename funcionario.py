import pessoa as p
import folhaPagamento as folha
import erros as e
import banco_de_dados as db

class funcionario(p.pessoa):
    def __init__(self):
        super().__init__()
        self.matriculaFuncionario = 0
        self.cargo = ""
        self.setor = ""
        self.cpf = 0
        self.salario_mes = 0
        self.nivel = 0
        self.salario_liquido = 0
    def cadastrar_funcionario(self):
        super().cadastrar_pessoa()
        listasMatricula = [x.matriculaFuncionario for x in db.DataBase('db/funcionario.pickle').loadObject()]
        msg = "Informe a matricula do funcionário: "
        self.matriculaFuncionario = e.tratarExistenciaPositiva(msg, listasMatricula)
        self.cargo = input("Informe o cargo: ")
        self.setor = input("Informe o setor: ")
        self.cpf = input("Informe o CPF: ")
        msg = "Informe o nível (1 a 4): "
        self.nivel = e.tratarNivel(msg)
        self.calcular_salario_func()
        inss = round(folha.folhaPagamento(self.salario_mes).calcular_inss(), 2)
        irrf = round(folha.folhaPagamento(self.salario_mes).calcular_irrf(), 2)
        salario_liquido = round(self.salario_liquido, 2)
        new = {'matricula_funcionario': self.matriculaFuncionario, 'cargo': self.cargo, 'setor': self.setor, 'cpf': self
            .cpf, 'nivel': self.nivel, 'salario_bruto': self.salario_mes, 'inss': inss , 'irrf': irrf, 'salario_liquido': salario_liquido}
        self.pessoa.update(new)
        print("")
        print("FUNCIONÁRIO CADASTRADO COM SUCESSO!!!")
        print("")
    def calcular_salario_func(self):
        if self.nivel == 1:
            self.salario_mes = 1500
        elif self.nivel == 2:
            self.salario_mes = 2380
        elif self.nivel == 3:
            self.salario_mes = 3500
        elif self.nivel == 4:
            self.salario_mes = 4277.32
        self.salario_liquido = folha.folhaPagamento(self.salario_mes).calcular_salario_liquido()
    def exibir_funcionario(self):
        return self.pessoa
