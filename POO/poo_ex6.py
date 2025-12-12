class Veiculo:
    def __init__(self,marca):
        self.marca = marca

class Carro(Veiculo):
    seguro = True

class Moto(Veiculo):
    seguro = True

Cerato = Carro('Kia')
Cerato.cor = ('Prata')
Cerato.seguro = False#se tiver nao precisa adicionar essa linha*


Pop100 = Moto('Honda')
Pop100.cor = 'Vermelha'

print(Cerato.marca,Cerato.cor,Cerato.seguro)
print(Pop100.marca,Pop100.cor,Pop100.seguro)