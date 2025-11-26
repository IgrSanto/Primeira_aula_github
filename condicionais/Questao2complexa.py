idade = input('Qual é sua idade: ')
try: 
    idade = int(idade) 
    if idade>=18:
        print('Acesso liberado ao sistema.')
except ValueError:
    print("Digite um número válido.")