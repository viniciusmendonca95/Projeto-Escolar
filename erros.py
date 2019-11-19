def tratarNivel(msg):
    try:
        nivel = int(input(msg))
        if nivel > 0 and nivel <= 4:
            return nivel
        else:
            print("Informação invalida, digite um nível entre 1 e 4")
            return tratarNivel(msg)
    except:
        print("Informação invalida, digite um nível entre 1 e 4")
        return tratarNivel(msg)


def tratarMenu(msg):
    try:
        opcao = int(input(msg))
        if opcao > 0 and opcao <= 6:
            return opcao
        else:
            print("Informação invalida, digite uma opção entre 1 e 6")
            return tratarMenu(msg)
    except:
        print("Informação invalida, digite uma opção entre 1 e 6")
        return tratarMenu(msg)


def tratarEspecialidade(msg):
    try:
        especialidade = int(input(msg))
        if especialidade >= 0 and especialidade  <= 3:
            return especialidade
        else:
            print("Informação invalida, digite uma especialidade entre 0 e 3")
            return tratarEspecialidade(msg)
    except:
        print("Informação invalida, digite um nível entre 0 e 3")
        return tratarEspecialidade(msg)


def tratarValorNegativo(msg):
    try:
        valor = int(input(msg))
        if valor > 0:
            return str(valor)
        else:
            print("Informação invalida, digite um valor maior que 0")
            return tratarValorNegativo(msg)
    except:
        print("Informação invalida, digite um valor maior que 0")
        return tratarValorNegativo(msg)


def tratarExistenciaPositiva(msg, lista):
    existencia = tratarValorNegativo(msg)
    if (existencia not in lista):
        lista.append(existencia)
        return existencia
    else:
        print("Esse valor já existe, por favor, informe outro valor")
        return tratarExistenciaPositiva(msg, lista)