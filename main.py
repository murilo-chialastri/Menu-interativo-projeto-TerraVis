import funcoesMenu
import funcionalidades


while(True):

    acesso = funcoesMenu.login()
    permissao = funcoesMenu.loginValidacao(acesso[0], acesso[1])
    if permissao == True:
        while(True):
            funcoesMenu.menu()
            opcao = int(input("opção: \n"))
            match opcao:
                case 1:
                    funcionalidades.informacoes()
                case 2:
                    break
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
