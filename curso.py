import professor as p
import banco_de_dados as db
import erros as e

class curso:
    def __init__(self):
        self.codCurso = 0
        self.nome = ""
        self.valor = 0
        self.cargaHoraria = 0
        self.qtdAlunos = 0
        self.nomeProfessor = ""
        self.cursos = {}
    def cadastrar_curso(self):
        listasCodCurso = [x.codCurso for x in db.DataBase('db/curso.pickle').loadObject()]
        msg = "Informe o código do curso: "
        self.codCurso = e.tratarExistenciaPositiva(msg, listasCodCurso)
        #self.codCurso = input("Informe o código do curso: ")
        self.nome = input("Informe o nome do curso: ")
        msg = "Informe o valor do curso: R$ "
        self.valor = e.tratarValorNegativo(msg)
        while True:
            matricularVar= input("Informe a matricula do professor que ministrará o curso: ")
            listaProfessores = db.DataBase('db/professor.pickle').loadObject()
            professorCod = list(filter(lambda x: x.matriculaProfessor == matricularVar, listaProfessores))
            if len(professorCod) == 0:
                print("Esse professor não está cadastrado, informe um professor que possui cadastro ou cadastre um novo professor")
            else:
                self.nomeProfessor = professorCod[0]
                break
        self.cargaHoraria = self.nomeProfessor.carga_horaria
        msg = "Informe a quantidade de alunos: "
        self.qtdAlunos = e.tratarValorNegativo(msg)
        print(f"Serão necessários no mínimo {self.calcular_valor_curso()} alunos para pagar o valor do curso")
        self.cursos = {'codCurso': self.codCurso, 'nome': self.nome, 'valor': self.valor,
                       'professor': self.nomeProfessor.nome, 'cargaHoraria': self.cargaHoraria,
                       'qtdAlunos': self.qtdAlunos, 'qntd_minima_alunos': self.calcular_valor_curso()}
        print("")
        print("CURSO CADASTRADO COM SUCESSO!!!")
        print("")
    def exibir_curso(self):
        return self.cursos
    def calcular_valor_curso(self):
        valorCurso = round((float(self.cargaHoraria)*float(self.nomeProfessor.salario_hora))/float(self.valor))
        return valorCurso

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.__str__()