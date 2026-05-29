def menu ():
    print("""Menu opções
    1- Informações
    2
    3""")



def login ():
    print("Boas-vindas!\n"
          "entre com o seu login\n")
    email = input("Insira seu email: ")
    senha = input("Insira sua senha: ")
    return email, senha



def loginValidacao (nome, senha):
    if "@" in nome and len(senha) >= 3:
        return True
    else:
        return False