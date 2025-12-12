class Banco:
    def __init__(self, saldo=0):
        self.saldo = saldo
@property
def saldo(self):
    return self._saldo

def depositar(self,valor):
    if valor<=0:
        raise ValueError("Valor deve ser positivo")
        self._saldo += valor

b = Banco(100)
print(b.saldo)
b.depositar(50)
print(b.saldo)   