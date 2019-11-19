import folhaPagamento as folha
import aluno as a
import professor as prof
import funcionario as f
import curso as c
import banco_de_dados as db
import erros as e

class menu:
    def __init__(self):
        self.aluno = a.aluno()
        self.professor = prof.professor()
        self.funcionario = f.funcionario()
        self.curso = c.curso()
        self.dbAluno = db.DataBase('db/aluno.pickle')
        self.dbProfessor = db.DataBase('db/professor.pickle')
        self.dbFuncionario = db.DataBase('db/funcionario.pickle')
        self.dbCurso = db.DataBase('db/curso.pickle')
    def menuPrincipal(self):
        while True:
            print("========== SISTEMA ESCOLAR =========")
            print("1- Menu Aluno\n2- Menu Professor\n3- Menu Funcionário\n4- Menu Curso\n5- Exibir folha de pagamento\n"
                  "6- Sair do programa")
            print("="*35)
            msg = "Informe uma opção: "
            op = e.tratarMenu(msg)
            if op == 1:
                while True:
                    print("=========== MENU ALUNO ===========")
                    print("1- Cadastrar aluno\n2- Exibir aluno\n3- Voltar pro menu anterior")
                    print("=" * 34)

                    opMenu = int(input("Informe uma opção: "))
                    if opMenu == 1:
                        if len(self.dbCurso.loadObject()) > 0:
                            self.aluno.cadastrar_aluno()
                            self.dbAluno.saveObject(self.aluno)
                        else:
                            print()
                            print("Nenhum curso cadastrado.")
                            print()
                    if opMenu == 2:
                        listaAlunos = self.dbAluno.loadObject()
                        matriculaAluno = input('Informe a matricula do aluno para exibir: ')
                        aluno = list(filter(lambda x: x.matricula == matriculaAluno, listaAlunos))
                        if (len(aluno) >= 1):
                            print(aluno[0].exibir_aluno())
                        else:
                            print("Nenhum aluno encontrado com essa matricula.")
                    if opMenu == 3:
                        break
            if op == 2:
                while True:
                    print("========= MENU PROFESSOR =========")
                    print("1- Cadastrar professor\n2- Exibir professor\n3- Voltar pro menu anterior")
                    print("=" * 34)
                    opMenu = int(input("Informe uma opção: "))
                    if opMenu == 1:
                        self.professor.cadastrar_professor()
                        self.dbProfessor.saveObject(self.professor)
                    if opMenu == 2:
                        listaProfessores = self.dbProfessor.loadObject()
                        matriculaProfessor = input('Informe a matricula do professor para exibir: ')
                        professor = list(filter(lambda x: x.matriculaProfessor == matriculaProfessor, listaProfessores))
                        if (len(professor) >= 1):
                            print(professor[0].exibir_professor())
                        else:
                            print("Nenhum professor encontrado com essa matricula.")
                    if opMenu == 3:
                        break
            if op == 3:
                while True:
                    print("======== MENU FUNCIONARIO ========")
                    print("1- Cadastrar Funcionario\n2- Exibir Funcionario\n3- Voltar pro menu anterior")
                    print("=" * 34)
                    opMenu = int(input("Informe uma opção: "))
                    if opMenu == 1:
                        self.funcionario.cadastrar_funcionario()
                        self.dbFuncionario.saveObject(self.funcionario)
                    if opMenu == 2:
                        listaFuncionarios = self.dbFuncionario.loadObject()
                        matriculaFuncionario = input('Informe a matricula do funcionário para exibir: ')
                        funcionario = list(filter(lambda x: x.matriculaFuncionario == matriculaFuncionario, listaFuncionarios))
                        if (len(funcionario) >= 1):
                            print(funcionario[0].exibir_funcionario())
                        else:
                            print("Nenhum funcionário encontrado com essa matricula")
                    if opMenu == 3:
                        break
            if op == 4:
                while True:
                    print("=========== MENU CURSO ===========")
                    print("1- Cadastrar curso\n2- Exibir curso\n3- Voltar pro menu anterior")
                    print("=" * 34)
                    opMenu = int(input("Informe uma opção: "))
                    if opMenu == 1:
                        if len(self.dbProfessor.loadObject()) > 0:
                            self.curso.cadastrar_curso()
                            self.dbCurso.saveObject(self.curso)
                        else:
                            print()
                            print("Nenhum professor cadastrado.")
                            print()
                    if opMenu == 2:
                        listaCursos = self.dbCurso.loadObject()
                        codCurso = input('Informe o código do curso para exibir: ')
                        curso = list(filter(lambda x: x.codCurso == codCurso, listaCursos))
                        if (len(curso) >= 1):
                            print(curso[0].exibir_curso())
                        else:
                            print("Nenhum curso encontrado com esse código")
                    if opMenu == 3:
                        break
            if op == 5:
                while True:
                    print("========== FOLHA DE PAGAMENTO ===========")
                    print("1- Exibir folha de pagamento professores\n2- Exibir Folha de pagamento funcionários\n3- Voltar pro me"
                          "nu anterior")
                    print("=" * 41)
                    opMenu = int(input("Informe uma opção: "))
                    if opMenu == 1:
                        listaProfessoresFolha = self.dbProfessor.loadObject()
                        matriculaProfessorFolha = input('Informe a matricula do professor para exibir a folha de pagamento: ')
                        salario_brutoProfessor = list(filter(lambda x: x.matriculaProfessor == matriculaProfessorFolha, listaProfessoresFolha))
                        if (len(salario_brutoProfessor) >= 1):
                            professor = salario_brutoProfessor[0].exibir_professor()
                            folha.folhaPagamento(professor['salario_bruto']).exibir_folha_pagamento_prof(matriculaProfessorFolha, professor['nome'], professor['plus_salario'], professor['salario_bruto'], professor['salario_liquido'], professor['inss'], professor['irrf'])
                        else:
                            print("Nenhum professor encontrado com essa matricula.")
                    if opMenu == 2:
                        listaFuncionariosFolha = self.dbFuncionario.loadObject()
                        matriculaFuncionarioFolha = input('Informe a matricula do funcionário para exibir a folha de pagamento: ')
                        salario_brutoFuncionario = list(filter(lambda x: x.matriculaFuncionario == matriculaFuncionarioFolha, listaFuncionariosFolha))
                        if (len(salario_brutoFuncionario) >= 1):
                            funcionario = salario_brutoFuncionario[0].exibir_funcionario()
                            folha.folhaPagamento(funcionario['salario_bruto']).exibir_folha_pagamento_func(matriculaFuncionarioFolha, funcionario['nome'], funcionario['salario_bruto'], funcionario['salario_liquido'], funcionario['inss'], funcionario['irrf'])
                        else:
                            print("Nenhum funcionário encontrado com essa matricula")
                    if opMenu == 3:
                        break
            if op == 6:
                print("=" * 34)
                print("       FINALIZANDO SISTEMA")
                print("=" * 34)
                break
