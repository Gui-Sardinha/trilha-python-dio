from Cliente import *


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return (f"{self.__class__.__name__}: "
                f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}")
