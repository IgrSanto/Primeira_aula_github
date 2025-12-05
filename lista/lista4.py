dados = [1,6,6,7,10,9,10,4,5,1,15,4,4]
produtos = ["TV","TV","VIDEO GAME"]
#limpar os repetidos
 
limpar_repetidos = list(set(dados))
print(limpar_repetidos)

#quantas vezes repete
presenca = dados.count(4)
print(presenca)
print(produtos.count("TV"))

numeros = []
for i in range(5):
    n = int(input("Digite um número:"))
    numeros.append(n)
    
numeros.sort()    
print("Lista final",numeros)#ordena crescente
numeros.sort(reverse=True)
print("Lista final",numeros)#ordena decrescente

for i in numeros:
    print(f"{i}\n")

nomes = ["Hernios","Jorgi","Igor","Artorios"]
print("Nomes:")
print(sorted(nomes))
for n in range (4):
        print(f"{n}")


