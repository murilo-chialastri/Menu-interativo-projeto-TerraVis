import funcoesMenu
import funcionalidades


while(True):

    acesso = funcoesMenu.login()
    permissao = funcoesMenu.loginValidacao(acesso[0], acesso[1])
    if permissao == True:
        lotes = []
        while(True):

            funcoesMenu.menu()
            opcao = int(input("opção: \n"))
            match opcao:
                case 1:
                    funcionalidades.informacoes()
                case 2:
                    res = funcionalidades.opcaoNdvi()
                    # red = res[0]
                    # nir = res[1]
                    # nvdi = res[2]
                    # alerta = res[3]
                    # estado = res[4]
                    # talhao = res[5]
                    dados = funcionalidades.dadosNvdi(res[0], res[1], res[2], res[3], res[4], res[5])
                    print(dados)
                    lotes.append(dados)
                case 3:
                    previsao = funcionalidades.prevQueimada()
                    print(previsao)
                case 4:
                    print()





            # match-case

    else:
        print("email ou senha inválido")
        op = int(input("deseja continuar?\n"
                       "+-------------------+\n"
                       "| Sim (1) | Não (2) |\n"
                       "+-------------------+\n"))
        if op == 1:
            continue
        elif op == 2:
            break
