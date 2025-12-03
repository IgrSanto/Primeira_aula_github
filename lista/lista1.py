lista = []
num = 10.6
print(type(num))
print(type(lista))
print(type(num)==int)

print(len(lista))
lista.append(1)
print(len(lista))
novalista=["Bruno",10,7.7, True]
lista.append(5.7)
lista.append("Bruno")
lista.append(True)
print(len(lista))
print(lista.index("Bruno"))
lista.remove("Bruno")
print(len(lista))