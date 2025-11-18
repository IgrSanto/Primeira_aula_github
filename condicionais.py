#Verificar se voce e um robo
frase = input("Digite a frase secreta \n")
if frase == 'Senac rocks':
    print("Parabens voce nao e um robo!!!")
else:
    print("Erro, infelizmente voce e um robo!")    

print(45==45) #Igual #True
print(18>17) #Maior que #True 
print(45==45 and 18>17) #Dois testes #True

print(18<17) #Menor que #False
print(105>=50) #Maior ou Igual #True
print(18<17 and 105>=50) #False

print(105<=50) #Menor ou Igual #False          
print(45!=45) #Negação(!) Igual #False
print(105<=50 and 45!=45) #False

print(18>17) #Maior que #True 
print(18<17) #Menor que #False
print(18>17 or 18<17) #Preferencia ao verdadeiro #True

idade = int(input("Qual e a sua idade: "))
if idade <12:
    print("Crianca")
elif idade <18 :
    print("Adolecente")      
elif idade <60 :
    print("Adulto")
else:
    print('idoso')
