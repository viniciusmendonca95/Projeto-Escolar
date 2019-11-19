import pessoa as p
import curso as c
import banco_de_dados as db
import erros as e

class aluno(p.pessoa):
    def __init__(self):
        super().__init__()
        self.rg = 0
        self.cpf = 0
        self.telefone = 0
        self.convenio = ""
        self.matricula = ""
        self.curso = None
        self.facebook = ""
        self.linkedin = ""
        self.instagram = ""
    def cadastrar_aluno(self):
        self.cadastrar_pessoa()
        self.rg = input("Informe o RG: ")
        self.cpf = input("Informe o CPF: ")
        self.telefone = input("Informe o telefone: ")
        self.convenio = input("Informe o convenio: ")
        listasMatricula = [x.matricula for x in db.DataBase('db/aluno.pickle').loadObject()]
        msg = "Informe a matricula do aluno: "
        self.matricula = e.tratarExistenciaPositiva(msg, listasMatricula)
        while True:
            codCursoVar = input("Informe o código do curso do aluno: ")
            listaCursos = db.DataBase('db/curso.pickle').loadObject()
            curso = list(filter(lambda x: x.codCurso == codCursoVar, listaCursos))
            if len(curso) == 0:
                print("Curso não existente!! Se não houver cursos, cadastre um novo curso ou informe o código de curso existente")
            else:
                self.curso = curso[0]
                break
        self.facebook = input("Informe o facebook: ")
        self.linkedin = input("Informe linkedin: ")
        self.instagram = input("Informe o instagram: ")
        new = {'rg': self.rg, 'cpf': self.cpf, 'telefone': self.telefone, 'convenio': self.convenio, 'matricula':
            self.matricula, 'curso': self.curso, 'facebook': self.facebook, 'linkedin': self.linkedin,
               'instagram': self.instagram}
        self.pessoa.update(new)
        print("")
        print("ALUNO CADASTRADO COM SUCESSO!!!")
        print("")
    def exibir_aluno(self):
        return self.pessoa
