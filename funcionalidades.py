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

def opcaoNdvi():
    menuNdvi()
    opc = int(input("Opção: "))
    match opc:
        case 1:
            red = 0.15
            nir = 0.10
            return red, nir
        case 2:
            red = 0.12
            nir = 0.25
            return red, nir
        case 3:
            red = 0.07
            nir = 0.48
            return red, nir
        case 4:
            red = 0.10
            nir = 0.38
            return red, nir
        case 5:
            red = 0.25
            nir = 0.18
            return red, nir
        case _:
            print("Opção inválida!")
            return None

def calculoNvdi(red, nir):
    return red + nir