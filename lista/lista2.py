fruta = ['maçã','uva','banana']
print(len(fruta))
fruta.append('pera')
print(len(fruta))

print(f"Eu gosto muito de " +fruta[3])
print(f"Eu não gosto de fruta {fruta[1]}")
print(fruta)
print("uva" in fruta)
print("Amor e carinho" not in fruta)
fruta.reverse()
print(fruta)
print(fruta[-0])
print(fruta[-2])

#possiveis erros
#print(fruta.index('jaca'))
#print(fruta[454])