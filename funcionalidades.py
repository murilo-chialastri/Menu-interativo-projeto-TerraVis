# 1- INFO
def informacoes():
    print("""\nTerraVis: plataforma de monitoramento orbital para o campo brasileiro.
Monitora saúde de lavouras (NDVI), risco de queimadas, enchentes
e janela ideal de plantio usando dados de satelites publicos.
Desenvolvido como prototipo academico pela equipe — FIAP 2026\n""")

#_________________________________________________________________________
# 2- NVDI
def menuNdvi():
    print("""Como esta sua lavoura atualmente?
1 - Plantio recente (solo ainda exposto)
2 - Crescimento inicial
3 - Desenvolvimento pleno
4 - Proximo da colheita
5 - Seca / estresse hidrico""")

def escolhaDeTalhao():
    talhao = input("nome do talhão: ")
    return talhao

def opcaoNdvi():
    talhao = escolhaDeTalhao()
    menuNdvi()
    opc = int(input("Opção: "))
    match opc:
        case 1:
            estado = "Plantio recente (solo ainda exposto)"
            red = 0.15
            nir = 0.10
            res = calculoNvdi(red, nir)
            nvdi = res[0]
            alerta = res[1]
            return red, nir, nvdi, alerta, estado, talhao
        case 2:
            estado = "Crescimento inicial"
            red = 0.12
            nir = 0.25
            res = calculoNvdi(red, nir)
            nvdi = res[0]
            alerta = res[1]
            return red, nir, nvdi, alerta, estado, talhao
        case 3:
            estado = "Desenvolvimento pleno"
            red = 0.07
            nir = 0.48
            res = calculoNvdi(red, nir)
            nvdi = res[0]
            alerta = res[1]
            return red, nir, nvdi, alerta, estado, talhao
        case 4:
            estado = "Proximo da colheita"
            red = 0.10
            nir = 0.38
            res = calculoNvdi(red, nir)
            nvdi = res[0]
            alerta = res[1]
            return red, nir, nvdi, alerta, estado, talhao
        case 5:
            estado = "Seca / estresse hidrico"
            red = 0.25
            nir = 0.18
            res = calculoNvdi(red,nir)
            nvdi = res[0]
            alerta = res[1]
            return red, nir, nvdi, alerta, estado, talhao
        case _:
            print("Opção inválida!")
            return None

def calculoNvdi(red, nir):
    # (NIR - RED) / (NIR + RED)
    ndvi = (nir - red) / (nir + red)
    if ndvi < 0.2:
        alerta = "CRÍTICO"
        return ndvi, alerta
    elif ndvi < 0.4:
        alerta = "ATENÇÃO"
        return ndvi, alerta
    elif ndvi < 0.6:
        alerta = "NORMAL"
        return ndvi, alerta
    else:
        alerta = "ÓTIMO"
        return ndvi, alerta

def dadosNvdi(red, nir, nvdi, alerta, estado, talhao):
    resultado = f"""== Resultado ==
Talhao: {talhao.upper()}
Estado: {estado}
RED: {red}  |  NIR: {nir}
NDVI calculado: {nvdi:.2f}

STATUS: {alerta}\n"""
    return resultado
#_________________________________________________________________________
# 3- QUEIMADA

def temperatura():
    menu = """Informe a temperatura atual da regiao (°C):"""
    temp = int(input(menu))
    if temp >= 0 and temp <= 60:
        return temp
    else:
        print("Temperatura inválida!\n A temperatura deve ser entre 0 e 60.")
        return None

def velocidadeVento():
    menu = """Informe a intensidade do vento (km/h)"""
    vento = int(input(menu))
    if vento > 0 and vento <= 120:
        return vento
    else:
        print("Vento inválido!\n O vento deve ser entre 0 e 120")
        return None

def umidadeRelativa():
    menu = """Informe a umidade do ar (%)"""
    umidade = int(input(menu))
    if umidade >= 0 and umidade <= 100:
        return umidade
    else:
        print("Umidade inválida!\n A umidade deve ser entre 0 e 100")
        return None

def chancesDeQueimada(temperatura, vento, umidade):
    if temperatura == None or vento == None or umidade == None:
        print("Dados inválidos!")
        return 0
    else:
        fatorTemp = temperatura / 50
        fatorUmidade = (100 - umidade) / 100
        fatorVento = vento / 100
        indice = (fatorTemp * 0.35) + (fatorUmidade * 0.45) + (fatorVento * 0.20)
        return indice

def classificacao(indice):
    if indice <= 0.29:
        risco = "Risco baixo (Condições normais)"
        return risco
    elif indice <= 0.54:
        risco = " Risco moderado (Atenção recomendada)"
        return risco
    elif indice <= 0.74:
        risco = " Risco moderado (Atenção recomendada)"
        return risco
    else:
        risco = "  Risco crítico (Emergência)"
        return risco

def prevQueimada():
    temp = temperatura()
    vento = velocidadeVento()
    umidade = umidadeRelativa()
    indice = chancesDeQueimada(temp, vento, umidade)
    clas = classificacao(indice)
    return clas
