import datetime
from classes.Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):       # Construtor = Certidão de nascimento da minha classe.
        self.clientes = clientes                                   # O atributo 'numero' da minha classe 'Conta' recebe o valor de numero
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()                        # Está relacionada por Composição

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPÓSITO", valor, datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True     # Não tem saldo suficiente
        else:
            return False    # Saque realizado com sucesso

    def transfereValor(self, conta_destino, valor):
        if self.saldo < valor:
            return  ("Não existe saldo suficiente")
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERÊNCIA", valor, datetime.datetime.today()])
            return ("Transferência Realizada")

    def gerar_saldo(self):
        print(f'Numero: {self.numero}\nSaldo: R$ {self.saldo}')

    """
    def gerar_dados(self):
        for c in self.clientes:
            print(f'Cliente: {c[1]} | Endereço: {c[2]}')
    """