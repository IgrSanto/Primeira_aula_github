opcao = input("Digite a área que você quer acessar:\n")

match opcao:
    case 'Home':
        print('Bem-vindo a página inicial!')
    case 'Esportes':
        print('Bem-vindo a página de Esportes!')
    case 'Games':
        print('Bem-vindo a página de Games!')
    case _:
        print('A página não existe!')    


letra = input("Digite uma letra:\n")

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("É uma vogal")
    case _:
        print("É uma consoante")