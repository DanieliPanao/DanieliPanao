class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    # metodo acessor get_saldo
    @property
    def saldo(self):
        return self.__saldo

    # metodo modificador
    def set_saldo (self, valor):
        self.__saldo = valor

    def depositar(self, valor):
        if valor < 0:
            return 'Valor deve ser positivo'
        self.__saldo += valor
        return 'Deposito realizado com Sucesso'

    def sacar(self, valor):
        if valor < 0:
            return 'Valor deve ser positivo'
        if valor > self.__saldo:
            return 'Saldo Insuficiente'
        self.__saldo -= valor
        return 'Saque realizado com Sucesso'


if __name__ == '__main__':
    c1 = Conta(1, 'Danieli')
