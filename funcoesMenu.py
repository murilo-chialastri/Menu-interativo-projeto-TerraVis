def menu ():
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

def iniciar():
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
def login ():
    print("""╔══════════════════════════════════╗
║         ACESSO AO SISTEMA        ║
╠══════════════════════════════════╣
║  Insira suas credenciais         ║
║  para continuar                  ║
╚══════════════════════════════════╝""")
    email = input("Email : ")
    senha = input("Senha : ")
    return email, senha


def loginValidacao (nome, senha):
    if "@" in nome and len(senha) >= 3:
        return True
    else:
        return False