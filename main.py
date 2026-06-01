import funcoesMenu
import funcionalidades
from funcionalidades import janelaDePlantio

while(True):
    lo = int(input("Fazer login (1)\nSair (2)"))
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
                        res = funcionalidades.opcaoNdvi()
                        dados = funcionalidades.dadosNvdi(res[0], res[1], res[2], res[3], res[4], res[5])
                        print(dados)
                        lotes.append(dados)
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
            print("email ou senha inválido")

    elif lo == 2:
        break
    else:
        print("Opção inválida!")
