from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError
from leitor import LeitorDeArquivo


class Cliente:

    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidos = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, agencia):
        if not isinstance(agencia, int):
            raise ValueError("O atributo agencia deve ser um inteiro", agencia)
        if agencia <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")
        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, numero):
        if not isinstance(numero, int):
            raise ValueError("O atributo numero deve ser um inteiro")
        if numero <= 0:
            raise ValueError("O atributo numero deve ser maior que zero")
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O atributo saldo deve ser um inteiro")
        self.__saldo = valor

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidos += 1
            E.args = ()
            raise OperacaoFinanceiraError("Operação não finalizada") from E
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        if valor > self.__saldo:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError('', self.saldo, valor)
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

# def main():
#     import sys
#
#     contas = []
#     while True:
#         try:
#             nome = input("Nome do cliente:\n")
#             agencia = input("Número da agencia:\n")
#             breakpoint()
#             numero = input("número da conta corrente:\n")
#
#             cliente = Cliente(nome, None, None)
#             conta_corrente = ContaCorrente(nome, agencia, numero)
#             contas.append(conta_corrente)
#         except KeyboardInterrupt:
#             print(f"\n\n{len(contas)}(s) criadas")
#             sys.exit()
#
#
# if __name__ == '__main__':
#     main()


# conta = ContaCorrente(None, 400, 4584894)
# conta1 = ContaCorrente(None, 401, 4584895)
#
# print(f'saldo conta: {conta.saldo} saldo conta1: {conta1.saldo}')
#
# try:
#     conta.sacar(1000)
#     print(f'saldo conta: {conta.saldo} saldo conta1: {conta1.saldo}')
# except OperacaoFinanceiraError as E:
#     breakpoint()
#     pass

with LeitorDeArquivo("arquivo.txt") as leitor:
    leitor.ler_proxima_linha()













