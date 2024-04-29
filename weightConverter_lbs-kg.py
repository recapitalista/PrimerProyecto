peso = int(input('Ingrese Peso: '))
tipoPeso = input('Kg o Lbs: ').lower()

if tipoPeso == 'kg' :
    conversion = peso * 0.45
    print(f'Tu peso en libras es {conversion}')
elif tipoPeso == 'lbs' :
    conversion = peso / 0.45
    print(f'Tu peso en kilogramos es {conversion}')
else :
    print('ERROR tipo de peso no es correcto')

