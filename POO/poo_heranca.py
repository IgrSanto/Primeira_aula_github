class Animal:
    def som(self):
        print("som genérico")
    def comer(self):
        print(f"O animal esta comendo")
    
class Cachorro(Animal):
    def __init__(self,nome):
        self.nome = nome
    
    def falarNome(self):
        print("Meu nome é {self.nome} AU!")

    def som(self):
        self("AUUUU")


animal =  Animal()
print(animal.comer())
cachorro = Cachorro("Julius")
print(cachorro.falarNome())

class Gato():
    def comer(self):
        print("O gato esta comendo")