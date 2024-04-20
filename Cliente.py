class Cliente:
    def __init__(self, endereco):
        self. endereco = endereco
        self.contas = []

    @staticmethod
    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)