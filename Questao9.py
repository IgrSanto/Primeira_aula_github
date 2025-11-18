semana = input("Escolha um dia da semana")
match semana:
    case "Segunda-feira" | "Terça-feira" | "Quarta-feira" | "Quinta-feira" | "Sexta-feira":
        print("Dia de semana")
    case "Sabado" | "Domingo":
        print("Fim de semana")           