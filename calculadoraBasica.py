cuenta = input("Elegir tipo de operacion(suma,resta,multiplicaicon,division): ")
num1 = input("Insertar Primer Numero: ")
num2 = input("Insertar Segundo Numero: ")

if cuenta == "suma" :
    print(int(num1) + int(num2))
elif cuenta == "resta" :
    print(int(num1) - int(num2))
elif cuenta == "multiplicacion" :
    print(int(num1) * int(num2))
elif cuenta == "division" :
    print(int(num1) / int(num2))
else :
    print("No existe esa opcion")