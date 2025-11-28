nome_funcionario = input("Digite o nome do funcionário >> ")
cpf_do_funcionario = input("Informe o CPF do funcionário >> ")
def boas_vindas(nome_funcionario,cpf_do_funcionario):
    print(f"Seja bem-vindo(a) ao sistema Senac-RJ, {nome_funcionario}")
    print(f"Seu CPF é {cpf_do_funcionario}")

boas_vindas(nome_funcionario,cpf_do_funcionario)    

nome = input("Digite o seu nome: \n")
if nome =="Igor":
    print(boas_vindas("Igor Santo",99421419214),nome)
