import funcoesMenu
import funcionalidades

while(True):
    msg = funcoesMenu.iniciar()
    lo = int(input(msg))
    if lo == 1:
        acesso = funcoesMenu.login()
        permissao = funcoesMenu.loginValidacao(acesso[0], acesso[1])
        if permissao == True:
            lotes = []
            while(True):
                funcoesMenu.menu()
                opcao = int(input("opção: "))
                match opcao:
                    case 1:
                        funcionalidades.informacoes()
                    case 2:
                        dados = funcionalidades.calcular()
                        print(dados)
                    case 3:
                        previsaoQueimada = funcionalidades.prevQueimada()
                        print(previsaoQueimada)
                    case 4:
                        previsaoEnchentes = funcionalidades.riscoEnchentes()
                        print(previsaoEnchentes)
                    case 5:
                        janelaDePlantio = funcionalidades.janelaDePlantio()
                        print(janelaDePlantio)
                    case 0:
                        print("Fechando programa...")
                        break
                    case _:
                        print("Opção inválida!")
        else:
            print("Email ou senha inválidos")
    elif lo == 2:
        break
    else:
        print("Opção inválida!")
