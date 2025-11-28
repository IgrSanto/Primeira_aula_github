def boas_vindas():
    return"Seja bem vindo(a) ao sistema Senac-RJ!"

print(boas_vindas())

nome = input("Digite o seu nome: \n")
if nome =="Igor":
    print(boas_vindas(),nome)

nome = input("Digite o seu nome: \n")#sem controle
print(boas_vindas(),nome)