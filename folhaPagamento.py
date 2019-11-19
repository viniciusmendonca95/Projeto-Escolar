class folhaPagamento:
    def __init__(self, salario_bruto):
        self.salario_bruto = salario_bruto
        self.inss = 0
        self.irrf = 0
        self.salario_liquido = 0
    def calcular_inss(self):
        inss = 0
        if self.salario_bruto <= 1693.72:
            inss = self.salario_bruto * 0.08
        elif self.salario_bruto > 1693.72 and self.salario_bruto <= 2822.90:
            inss = self.salario_bruto * 0.09
        elif self.salario_bruto > 2822.90 and self.salario_bruto <= 5645.80:
            inss = self.salario_bruto * 0.11
        elif self.salario_bruto > 5645.80:
            inss = 621.04
        self.inss = inss
        return inss
    def calcular_irrf(self):
        irrf = 0
        if self.salario_bruto < 1903.98:
            irrf = 0
        elif self.salario_bruto > 1903.98 and self.salario_bruto < 2826.66:
            irrf = self.salario_bruto * 0.075
        elif self.salario_bruto >= 2826.66 and self.salario_bruto < 3751.06:
            irrf = self.salario_bruto * 0.15
        elif self.salario_bruto >= 3751.06 and self.salario_bruto < 4664.69:
            irrf = self.salario_bruto * 0.225
        elif self.salario_bruto >= 4664.69:
            irrf = self.salario_bruto * 0.275
        self.irrf = irrf
        return irrf
    def calcular_salario_liquido(self):
        self.calcular_inss()
        self.calcular_irrf()
        salario_liquido = self.salario_bruto - self.inss - self.irrf
        self.salario_liquido = salario_liquido
        return self.salario_liquido
    def exibir_folha_pagamento_prof(self, matriculaProfessorFolha, nomeProfessor, plusSalario, salario_bruto, salario_liquido, inss, irrf):
        self.calcular_salario_liquido()
        print("")
        print("========== FOLHA DE PAGAMENTO PROFESSORES ==========")
        print(f"Matricula: {matriculaProfessorFolha} ")
        print(f"Nome: {nomeProfessor}")
        print(f"Salário bruto: R${salario_bruto:.2f}")
        print(f"Plus salário: R${plusSalario}")
        print(f"INSS: R${inss:.2f}")
        print(f"IRRF: R${irrf:.2f}")
        print(f"Salário líquido: R${salario_liquido}")
        print("")
    def exibir_folha_pagamento_func(self, matriculaFuncionarioFolha, nomeFuncionario, salario_bruto, salario_liquido, inss, irrf):
        print("")
        print("========== FOLHA DE PAGAMENTO FUNCIONÁRIOS ==========")
        print(f"Matricula: {matriculaFuncionarioFolha} ")
        print(f"Nome: {nomeFuncionario}")
        print(f"Salário bruto: R${salario_bruto:.2f}")
        print(f"INSS: R${inss:.2f}")
        print(f"IRRF: R${irrf:.2f}")
        print(f"Salário líquido: R${salario_liquido}")
        print("")

