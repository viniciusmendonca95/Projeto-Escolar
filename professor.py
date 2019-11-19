import pessoa as p
import folhaPagamento as folha
import erros as e
import banco_de_dados as db

class professor(p.pessoa):
    def __init__(self):
        super().__init__()
        self.matriculaProfessor = ""
        self.titulacao = ""
        self.especialidade = ""
        self.plus_salario = 0
        self.salario_hora = 0
        self.linkedin = ""
        self.lattes = ""
        self.nivel = 0
        self.carga_horaria = 0
        self.salario_bruto = 0
        self.salario_bruto_plus = 0
        self.salario_hora = 0
        self.salario_liquido = 0
        self.curso = ""
    def cadastrar_professor(self):
        super().cadastrar_pessoa()
        listasMatricula = [x.matriculaProfessor for x in db.DataBase('db/professor.pickle').loadObject()]
        msg = "Informe a matricula do professor: "
        self.matriculaProfessor = e.tratarExistenciaPositiva(msg, listasMatricula)
        self.titulacao = input("Informe a titulação: ")
        self.linkedin = input("Informe o linkedin: ")
        self.lattes = input("Informe o lattes: ")
        msg = "Informe o nível (1 a 4): "
        self.nivel = e.tratarNivel(msg)
        msg = "Informe a carga horária mensal do professor (em horas): "
        self.carga_horaria = e.tratarValorNegativo(msg)
        print("="*22)
        print("0 - Sem especialidade\n1 - Especialista\n2 - Mestre\n3 - Doutor")
        print("="*22)
        msg = "Informe o especialidade: "
        self.especialidade = e.tratarEspecialidade(msg)
        self.calcular_salario_prof()
        inss = round(folha.folhaPagamento(self.salario_bruto_plus).calcular_inss(), 2)
        irrf = round(folha.folhaPagamento(self.salario_bruto_plus).calcular_irrf(), 2)
        salario_hora = round(self.salario_hora, 2)
        plus_salario = round(self.plus_salario, 2)
        salario_liquido = round(self.salario_liquido, 2)
        new = {'matricula_professor': self.matriculaProfessor, 'titulacao': self.titulacao, 'nivel': self.nivel,
               'carga_horaria': self.carga_horaria, 'especialidade': self.especialidade, 'linkedin': self.linkedin,
               'lattes': self.lattes, 'salario_bruto': self.salario_bruto, 'plus_salario': plus_salario,
               'salario_hora': salario_hora, 'inss': inss, 'irrf': irrf, 'salario_liquido': salario_liquido}
        self.pessoa.update(new)
        print("")
        print("PROFESSOR CADASTRADO COM SUCESSO!!!")
        print("")
    def calcular_salario_prof(self):
        if self.nivel == 1:
            self.salario_bruto = 2570
        elif self.nivel == 2:
            self.salario_bruto = 3685
        elif self.nivel == 3:
            self.salario_bruto = 4843.33
        elif self.nivel == 4:
            self.salario_bruto = 5223.77
        if self.especialidade == 0:
            self.salario_bruto_plus = self.salario_bruto
            self.plus_salario = 0
            self.especialidade = "Sem especialidade"
        elif self.especialidade == 1:
            self.salario_bruto_plus = self.salario_bruto * 1.05
            self.plus_salario = self.salario_bruto_plus - self.salario_bruto
            self.especialidade = "Especialista"
        elif self.especialidade == 2:
            self.salario_bruto_plus = self.salario_bruto * 1.15
            self.plus_salario = self.salario_bruto_plus - self.salario_bruto
            self.especialidade = "Mestre"
        elif self.especialidade == 3:
            self.salario_bruto_plus = self.salario_bruto * 1.25
            self.plus_salario = self.salario_bruto_plus - self.salario_bruto
            self.especialidade = "Doutor"
        self.salario_liquido = folha.folhaPagamento(self.salario_bruto + self.plus_salario).calcular_salario_liquido()
        self.salario_hora = float(self.salario_bruto_plus)/float(self.carga_horaria)
    def exibir_professor(self):
        return self.pessoa

