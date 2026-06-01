def menu (): #menu utilizado no While da main
    print("""
╔══════════════════════════════════╗
║         TERRAVIS - MENU          ║
╠══════════════════════════════════╣
║  [1]  Informacoes sobre o sistema║
║  [2]  Calcular NDVI              ║
║  [3]  Previsao de queimadas      ║
║  [4]  Previsao de enchentes      ║
║  [5]  Janela de plantio          ║
╠══════════════════════════════════╣
║  [0]  Sair                       ║
╚══════════════════════════════════╝
""")

def iniciar(): #Tela inicial do menu
    msg = """╔══════════════════════════════╗
║       BEM-VINDO AO           ║
║         TERRAVIS             ║
║  Inteligencia orbital para   ║
║      o campo brasileiro      ║
╠══════════════════════════════╣
║  [1] Entrar                  ║
║  [2] Sair                    ║
╚══════════════════════════════╝
"""
    return msg

def login (): #menu que pede senha e email
    print("""╔══════════════════════════════════╗
║         ACESSO AO SISTEMA        ║
╠══════════════════════════════════╣
║  Insira suas credenciais         ║
║  para continuar                  ║
╚══════════════════════════════════╝""")
    email = input("Email : ")
    senha = input("Senha : ")
    return email, senha


def loginValidacao (nome, senha): #verifica se o email tem "@" e senha tem mais de 3 caracteres
    if "@" in nome and len(senha) >= 3:
        return True
    else:
        return False