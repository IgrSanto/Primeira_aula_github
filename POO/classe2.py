class produto:
    def __init__(self,nome,preco,data_validade):
        self.nome = nome
        self.preco = preco
        self.data_validade = data_validade
        



coca = produto("Coca-cola",5.57,"15/01/2025")
uva = produto("Uva",1.57,"05/01/2025")
print(coca.preco,coca.data_validade)
print(uva.nome,uva.preco,uva.data_validade)
fanta_preco = 12.50
fanta_validade = '29/11/2025'
fanta_nome = 'Fanta'
fanta = produto()
print(fanta.fanta_nome,fanta.fanta_validade,fanta.fanta_preco)