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
    clas = f"""
    ================================
    {classificacao(indice)}
    ================================"""
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

            status = f"""\n
            ======== Situacao atual ========
            Nivel do rio: {nivelAtual:.1f}m
            Status: {avisoAtual}
        
            = Projecao para as proximas 24h =
            Precipitacao prevista: {precip}mm
            Nivel projetado: {nivelFinal:.1f}m
            Status: {avisoFinal}
            
            {situacao}
            ================================"""
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
mesesNomes = {
    1:  "Jan",
    2:  "Fev",
    3:  "Mar",
    4:  "Abr",
    5:  "Mai",
    6:  "Jun",
    7:  "Jul",
    8:  "Ago",
    9:  "Set",
    10: "Out",
    11: "Nov",
    12: "Dez",
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
            return plant

        elif cultivo == 2:
            plant = "milho"
            return plant

        elif cultivo == 3:
            plant = "trigo"
            return plant

        elif cultivo == 4:
            plant = "feijao"
            return plant

        elif cultivo == 5:
            plant = "algodao"
            return plant

        else:
            print("Opção inválida")



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

def infoMeses():
    while True:
        mes = int(input("Informe o mês atual(1,2,3...,12): "))
        mesAnterior = mes - 1
        mesPosterior = mes + 1
        if mes == 1:
            mesAnterior = 12
            break
        elif mes == 12:
            mesPosterior = 1
            break
        elif mes < 1 or mes > 12:
            print("Mês inválido")
        else:
            break
    return mes, mesAnterior, mesPosterior

def avisoMeses(plant, regiao ,mesAnterior, mes, mesPosterior):
    meses = janelas[plant][regiao]
    if len(meses) == 0:
        sts = "NÃO RECOMENDADO"
        aviso = "Esta plantação não e recomendada para esta região."
    elif mes in meses and mesAnterior in meses:
        sts = "MOMENTO PERFEITO"
        aviso = """Momento perfeito para o plantio!
        (Plante agora)."""
    elif mes in meses:
        sts = "MOMENTO IDEAL"
        aviso = """Momento ideal para o plantio!
        (Plante agora)."""
    elif not mes in meses and mesAnterior in meses:
        sts = "EM BREVE"
        aviso = """A janela de plantio está se aproximando.
        (Prepare o solo e aguarde o próximo mês)."""
    elif not mes in meses and mesPosterior in meses:
        sts = "ATENÇÃO"
        aviso = """A janela de plantio está se encerrando.
        (Aguardar o próximo ciclo)"""
    else:
        sts = "FORA DA JANELA"
        aviso = "Fora do periodo ideal para o plantio."
    return aviso, sts

def exibirInfo(plant, regiao, mes, aviso, status):
    meses = janelas[plant][regiao]
    mesAtual = mesesNomes[mes]
    mesesN = []
    for m in meses:
        mesesN.append(mesesNomes[m])
    # mesesN = str([meses[m] for m in meses])


    if status != "NÃO RECOMENDADO" :
        mensagem = f"""
        ================================
        JANELA DE PLANTIO - TERRAVIS
        ================================
        Cultura : {plant.upper()}
        Regiao  : {regiao.upper()}
        Mes atual: {mesAtual.upper()} ({mes})
        
        Status: {status}
        
        Recomendacao: {aviso}
        
        Meses recomendados: {", ".join(mesesN)}
        ================================"""
    else:
        mensagem = f"""
        ================================
        JANELA DE PLANTIO - TERRAVIS
        ================================
        Cultura : {plant.upper()}
        Regiao  : {regiao.upper()}
        
        Status: {status}
        
        Recomendacao: {aviso}
        ================================"""
    return mensagem

def janelaDePlantio():
    plantio = infoDePlantio()
    regiao = infoRegiao()
    meses = infoMeses()

    alertas = avisoMeses(plantio, regiao, meses[0], meses[1], meses[2])
    geral = exibirInfo(plantio, regiao, meses[1], alertas[0], alertas[1])

    return geral
