valor = input('Qual o valor da compra:\n')
try:
    valor = float(valor)
    if valor >=100 :
        print("Desconto aplicado")
    else  :
        print('Desconto não se aplica ao valor')
except ValueError:
    print('Use caracteres validos')