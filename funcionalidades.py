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
        risco = "Risco baixo (Sem necessidade de atenção)"
        return risco
    elif indice <= 0.54:
        risco = "Risco moderado (Condições normais)"
        return risco
    elif indice <= 0.74:
        risco = "Risco alto (Atenção recomendada)"
        return risco
    else:
        risco = "Risco crítico (Emergência)"
        return risco

def prevQueimada():
    temp = temperatura()
    vento = velocidadeVento()
    umidade = umidadeRelativa()
    indice = chancesDeQueimada(temp, vento, umidade)
    clas = classificacao(indice)
    return clas

#_________________________________________________________________________
# 4- ENCHENTES

def nivelDoRio():
    nivel = float(input("Informe a nivel do Rio em metros: "))

    if nivel > 0 and nivel <= 10 :

        if nivel <= 3:
            aviso = "Normal"

        elif nivel > 3 and nivel <= 4.5:
            aviso = "Atencao — monitorar"

        elif nivel > 4.5 and nivel <= 6.0:
            aviso = "Alerta — risco de alagamento"

        else:
            aviso = "Emergencia — evacuacao indicada"

        return nivel, aviso
    else:

        return None

def precipitacao(nivelAtual):
    prec = int(input("Informe a precipitação prevista nas próximas 24h (mm): "))
    if prec >= 0 and prec <= 400 and nivelAtual != None:
        prevFinal = nivelAtual + (prec / 10) * 0.3
        if prevFinal <= 3:
            aviso = "Normal"

        elif prevFinal > 3 and prevFinal <= 4.5:
            aviso = "Atencao — monitorar"

        elif prevFinal > 4.5 and prevFinal <= 6.0:
            aviso = "Alerta — risco de alagamento"

        else:
            aviso = "Emergencia — evacuacao indicada"
        return prec, aviso, prevFinal
    else:

        return None

def riscoEnchentes():
    nivelEAviso = nivelDoRio() #Guarda a lista [nivel, aviso]
    if nivelEAviso != None:
        nivelAtual = nivelEAviso[0]
        avisoAtual = nivelEAviso[1]
        precipitacoes = precipitacao(nivelAtual) #Guarda a lista [precipitação, aviso, nivelFinal]
        if precipitacoes != None:
            precip = precipitacoes[0]
            avisoFinal = precipitacoes[1]
            nivelFinal = precipitacoes[2]

            if len(avisoAtual) < len(avisoFinal): #Quanto pior a situação, mais caracteres tem na mensagem, isso serve como um "nível de risco"
                situacao = "[!] Atencao: a situacao vai piorar nas proximas 24 horas."
            else:
                situacao = "[ok] Situacao estavel. Sem mudancas previstas."

            status = f"""\n== Situacao atual ==
        Nivel do rio: {nivelAtual:.1f}m
        Status: {avisoAtual}
        
        == Projecao para as proximas 24h ==
        Precipitacao prevista: {precip}mm
        Nivel projetado: {nivelFinal:.1f}m
        Status: {avisoFinal}
        
        {situacao}"""
            return status
        else:
            print("A precipitação não foi informada corretamente!")
            return None
    else:
        print("O nível do rio não foi imformado corretamente!")
        return None
#_________________________________________________________________________
# 5- JANELA DE PLANTIO

janelas = {   #dicionário para busca eficiente de valores, a escolha do dicionario para esse tipo de função é necessaria para otimizar o código
    "soja": {
        "sul":          [10, 11, 12, 1],
        "sudeste":      [10, 11, 12],
        "centro-oeste": [10, 11, 12],
        "nordeste":     [11, 12, 1],
        "norte":        [11, 12, 1],
    },
    "milho": {
        "sul":          [9, 10, 11, 12],
        "sudeste":      [9, 10, 11],
        "centro-oeste": [9, 10, 11],
        "nordeste":     [4, 5, 6],
        "norte":        [4, 5, 6],
    },
    "trigo": {
        "sul":          [4, 5, 6],
        "sudeste":      [4, 5],
        "centro-oeste": [],
        "nordeste":     [],
        "norte":        [],
    },
    "feijao": {
        "sul":          [9, 10, 11],
        "sudeste":      [8, 9, 10],
        "centro-oeste": [8, 9, 10],
        "nordeste":     [3, 4, 5],
        "norte":        [3, 4, 5],
    },
    "algodao": {
        "sul":          [],
        "sudeste":      [10, 11],
        "centro-oeste": [10, 11],
        "nordeste":     [1, 2, 3],
        "norte":        [1, 2, 3],
    },
}

def infoDePlantio():
    while True:
        cultivo = int(input("Selecione o plantio\n"
                            "1- Soja\n"
                            "2- Milho\n"
                            "3- Trigo\n"
                            "4- Feijão\n"
                            "5- Algodao\n"))
        if cultivo == 1:
            plant = "soja"
            break
        elif cultivo == 2:
            plant = "milho"
            break
        elif cultivo == 3:
            plant = "trigo"
            break
        elif cultivo == 4:
            plant = "feijao"
            break
        elif cultivo == 5:
            plant = "algodao"
            break
        else:
            print("Opção inválida")
    return plant


def infoRegiao():
    while True:
        reg = int(input("Selecione a região\n"
                        "1- Sul\n"
                        "2- Sudeste\n"
                        "3- Centro-oeste\n"
                        "4- Nordeste\n"
                        "5- Norte\n"))
        if reg == 1:
            regiao = "sul"
            break
        elif reg == 2:
            regiao = "sudeste"
            break
        elif reg == 3:
            regiao = "centro-oeste"
            break
        elif reg == 4:
            regiao = "nordeste"
            break
        elif reg == 5:
            regiao = "norte"
            break
        else:
            print("Opcço inválida")
    return regiao


