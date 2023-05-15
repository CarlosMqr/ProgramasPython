tipo = int(input("que operacion desea realizar\n1: suma\n2: resta\n3: multiplicacion\n4: divicion\n"))
valorA = int(input("Ingresa primer valor entero\n"))
valorB = int(input("Ingresa segundo valor valor entero\n"))

resultado =0

if tipo == 1:
    resultado = (valorA + valorB)
    print("La suma es: ", resultado)

elif tipo == 2:
    resultado = (valorA - valorB)
    print("La resta es: ", resultado)

elif tipo == 3:
    resultado = (valorA * valorB)
    print("La multiplicacion es: ", resultado)

elif tipo == 4:
    resultado = (valorA / valorB)
    print("La divicion es: ", resultado)