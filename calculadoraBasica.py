cuenta = input("Elegir tipo de operacion(suma,resta,multiplicaicon,division,potencia): ").lower()
num1 = float(input("Insertar Primer Numero: "))
num2 = float(input("Insertar Segundo Numero: "))

if cuenta == "suma" :
    resultado = num1 + num2
elif cuenta == "resta" :
    resultado = num1 - num2
elif cuenta == "multiplicacion" :
    resultado = num1 * num2
elif cuenta == "division" :
    if num2 != 0 :
        resultado = num1 / num2
    else :
        resultado = "ERROR - No es posible dividir por cero"
elif cuenta == "potencia" :
    resultado = num1 ** num2
else :
    resultado = "ERROR - No existe esa opcion"
    
resultado = f'El resultado es: {resultado}'
print(resultado)