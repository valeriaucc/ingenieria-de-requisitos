print ("encargo de telas")
produccion_metros = input("digite telas en metros: ")
print ("conversion")
conversion = int(produccion_metros)*float(0.0254)

print ("valor pulgada")
valor = input("digite el valor: ")

print ("costo")
costo = round(conversion*int(valor))
print (f'la costo del productor es {costo}')