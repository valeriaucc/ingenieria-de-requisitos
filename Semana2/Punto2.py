print ("area del rectangulo")
base_rectangulo = input("digite la base: ")
altura_rectangulo = input("digite la altura: ")
area_rectangulo = int(base_rectangulo)*int(altura_rectangulo)*3
print (f'la area del rectangulo es {area_rectangulo}')

valor_metro = int(input("digite el valor del metro cubico: "))
costo = area_rectangulo*valor_metro
print (f'la persona debe pagar {costo}')