import Menu

clientes = []
contas = []

while True:
    opcao = Menu.menu()

    if opcao == "d":
        Menu.depositar(clientes)

    elif opcao == "s":
        Menu.sacar(clientes)

    elif opcao == "e":
        Menu.exibir_extrato(clientes)

    elif opcao == "nu":
        Menu.criar_cliente(clientes)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        Menu.criar_conta(numero_conta, clientes, contas)

    elif opcao == "lc":
        Menu.listar_contas(contas)

    elif opcao == "q":
        break