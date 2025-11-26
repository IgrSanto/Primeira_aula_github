nota = input("Sua nota: ")
try:
    nota = float(nota)
    if nota >=7 :
        print("Aprovado!")
    else :
        print("Reprovado!")    
except ValueError:
    print("Digite uma nota valida")    
