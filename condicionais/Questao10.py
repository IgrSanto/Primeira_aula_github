numero = input("Escolha o número a se seguir:\n")
match numero:
    case '1':
        print("Voçê escolheu o número 1!")
    
    case '2':
        print("Voçê escolheu o número 2!")

    case '3':
        print('Voçê escolheu o número 3!')
    
    case '4':
        print("Voçê escolheu o número 4!")
    
    case '5':
        print('Voçê escolheu o número 5!')

    case _:
        print("Esse numero não esta disponivel!")     
