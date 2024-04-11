class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("numero da conta:", self.numero)
        print("titular:", self.titular)
        print("saldo:", self.saldo)


    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("saldo insuficiente")

numero_conta = input("digite o numero da conta:")
titular_conta = input("digite o titular da conta:")
saldo_incicial = float(input("digite o saldo inicial da conta:"))


valor_deposito = float(input("digite o valor a ser depositado").replace(",","."))
valor_saque = (input("digite o valor do saque:"))

conta_da_manu = ContaBancaria("1234-5", "manu", 100)
conta_da_manu.depositar(1000)
conta_da_manu.sacar(200)

conta_da_manu.exibir_detalhes()

