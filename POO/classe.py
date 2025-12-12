class Carro: 
    def __str__ (self):
        return self.modelo,self.cor,self.tipo,self.ano,self.condicao,self.preco


corolla= Carro()
corolla.modelo = corolla
corolla.cor = 'preto'
corolla.tipo= 'sport'
corolla.porta= 4
corolla.ano = '2025'
corolla.condicao = "novo"
corolla.preco = 196.000
print(corolla.__str__())

