import textwrap
from Conta import *
from Deposito import *
from PessoaFisica import *
from Saque import *


def menu():
    menu = """""\n
    +++++++++++++++++ MENU ++++++++++++++++++++++
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo Usuário
    [q]\tSair
    ==>"""
    return input(textwrap.dedent(menu))


def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possuí conta @@@")
        return
    #FIXME: não permite cliente escolher a conta
    return cliente.contas


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n  @@@ cliente não encontrado @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n@@@@ Cliente não encontrado @@@")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado ")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n===================== Extrato ==========================")
    transacoes = conta.Historico.transacoes()

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações. "
    else:
        for transacao in transacoes:
            extrato += (f"\n{transacao['tipo']}:\n\tR$ "
                        f"{transacao['valor']:/.2f}")

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-AAAA): ")
    endereco = input("Informe o endereco (logadouro, nº, bairro, cidade/sigla do estado): ")

    cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)

    clientes.append(cliente)

    print("\n===== Cliente criado com sucesso =====")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado @@@")
        return
    conta = Conta.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n===== Conta criada com sucesso =====")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
