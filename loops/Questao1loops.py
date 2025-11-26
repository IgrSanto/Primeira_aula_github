while True:
    try : 
        n= int(input("Digite um número positivo: \n"))  
        if n >0:
            print("O número é positivo obrigado!",n)
        else:
            print("O número deve ser positivo!")
            break
    except ValueError:
        print("Entrada inválida. Tente novamente ")
        break
