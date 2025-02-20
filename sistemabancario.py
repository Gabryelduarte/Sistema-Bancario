from abc import ABC, abstractmethod
from datetime import date

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        return conta.sacar(self.valor)

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        return conta.depositar(self.valor)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero: int, agencia: str):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def sacar(self, valor: float):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(Saque(valor))
        return True

    def depositar(self, valor: float):
        if valor <= 0:
            return False
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, agencia: str, limite: float, limite_saques: int):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        if transacao.registrar(conta):
            conta.historico.adicionar_transacao(transacao)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class PessoaFisica1(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
