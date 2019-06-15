#coding=UTF-8

""" UdemyBucles: Ejercicio N°20 - Mostrar en pantalla los N primero números
primos. Se pide por teclado la cantidad de números primos que queremos 
mostrar.."""

cantidad_primos = raw_input("Ingrese la cantidad de números primos que desea generar: ")
cantidad_primos = int(cantidad_primos)

while cantidad_primos > 0:
		num = raw_input("Ingrese un número: ")
		num = int(num)
		cantidad_primos = cantidad_primos + 1
		if num % i == 0:
            print "Es primo."
        else:
        	print "No es primo."
	
raw_input("Oprima la tecla ENTER para finalizar el programa.")