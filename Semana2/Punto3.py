print ("digite primer numero")
primer_numero = input("primer digito: ")
print ("digite segundo numero")
segundo_numero = input("segundo digito: ")

if primer_numero == segundo_numero:
    print(f'los numeros son iguales')

elif primer_numero >= segundo_numero:
    print(f'{primer_numero} es mayor que {segundo_numero}')

elif segundo_numero >= primer_numero:
    print(f'{primer_numero} es menor que {segundo_numero}')
