#coding=UTF-8


'''
Ejercicio: 27, Tema: Toma de desiciones
Enunciado --> (27.) Ingresar un calificación numérica e informar el concepto según la siguiente tabla:
27.1. Nota = 0.00 a 3.99 Informar INSUFICIENTE
27.2. Nota = 4.00 a 6.99 Informar REGULAR
27.3. Nota = 7.00 a 8.99 Informar BUENO
27.4. Nota = 9.00 a 10.00 Informar MUY BUENO
Nombre del archivo 'td27.py'
Desarrollo del algoritmo en código Python
'''
print "\nRecibe una nota numérica e informa el concepto."
nota = raw_input("\nIngresar una nota numérica: ")
nota = float(nota)

if nota == 0.00 or nota <= 3.99:
    print "\nINSUFICIENTE"
else:
    if nota == 4.00 or nota <= 6.99:
        print "\nREGULAR."
    else:
        if nota == 7.00 or nota <= 8.99:
            print "\nBUENO."
        else:
            if nota == 9.0 or nota <= 10.00:
                print "\nMUY BUENO."
                
raw_input("\nOprima la tecla ENTER para finalizar.")
