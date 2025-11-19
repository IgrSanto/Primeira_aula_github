operacao = input("Digite a opção: Soma | Subtração | divisão | Multiplicação:\n")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: ")) 

match operacao:
    case "Soma":
        resultado = num1+num2
        print(f"O resultado é : {resultado}")
    case "Subtração" | "Subtracao" | "subtração":
        resultado = num1-num2
        print(f"O resultado é : {resultado}")
    case "Divisão" | "Divisao":
        if num2 != 0:
            print("O resultado é : "+str(num1/num2))
        else:
            print("Erro:Divisão por zero não é permitida.")
        resultado = num1/num2
        print(f"O resultado é : {resultado}")  
    case "Multiplicação" | "Multiplicacao":
        resultado = num1*num2
        print(f"O resultado é : {resultado}")
    case _:
        print("Opera n ção invalida!") 

