cuenta = input("Elegir tipo de operacion(suma,resta,multiplicaicon,division): ")
num1 = float(input("Insertar Primer Numero: "))
num2 = float(input("Insertar Segundo Numero: "))

if cuenta == "suma" :
    resultado = num1 + num2
elif cuenta == "resta" :
    resultado = num1 + num2
elif cuenta == "multiplicacion" :
    resultado = num1 * num2
elif cuenta == "division" :
    if num2 != 0 :
        resultado = num1 / num2
    else :
        resultado = "No es posible dividir por cero"
else :
    print("No existe esa opcion")
    
print('El resultado es: ' + resultado)