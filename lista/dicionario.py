pessoa ={
    "nome": "Ana",
    "sobrenome": "Bolina",
    "data nasc": "22/09/2000",
    "CPF": "777.244.333.12",
    "Cel": "(21)6999-3020"
}
pessoa['Cidade'] = 'Rio de Janeiro'
pessoa["nome"] = 'Janne'
pessoa["sobrenome"] = 'Benine'
pessoa['Peso'] = '75'
pessoa['Altura'] = '171'
del pessoa['data nasc'] # remover chave e valor
if 'data nasc' in pessoa:
    pessoa['data nasc'] = '19/07/2003'
else:
    print('Chave inexistente')
print(pessoa)
print('Seu IMC é:')
print(pessoa['Peso']/(pessoa['Altura']*pessoa['Altura']))
print(f"Bem vindo(a).\nNome: {pessoa['nome']}\nSobrenome: {pessoa['sobrenome']}\ndata nasc: {pessoa['data nasc']}\nCPF: {pessoa['CPF']}\nCelular: {pessoa['Cel']}\nCidade: {pessoa['Cidade']}\nPeso: {pessoa['Peso']}kg")

