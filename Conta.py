from Historico import *

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = "001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        execedeu_saldo = valor > saldo

        if execedeu_saldo:
            print(" \n@@@ Operação falhou, você não tem saldo suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n ====== Saque realizado com sucesso ======")
            return True
        else:
            print("\n@@@@ Operação falhou, o valor informado é inválido ")

        return False


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n Depósito realizado com sucesso")
        else:
            print("\n Operação falhou, o valor informado é inválido")
            return False

        return True

