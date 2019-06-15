#coding=UTF-8


"""UdemyBucles: Ejercicio N°2 - Crea una aplicación que permita adivinar un número. 
La aplicación genera un número aleatorio del 1 al 100. 
A continuación va pidiendo números y va respondiendo si el número a 
adivinar es mayor o menor que el introducido,a demás de los intentos 
que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número 
(además te dice en cuantos intentos lo has acertado), 
si se llega al limite de intentos te muestra el número que había generado."""

import random
print "Este programa generará un número del 1 al 100 al azar, usted deberá adivinar que número es."
raw_input("\n¡Presione ENTER para comenzar el juego!")
num = random.randint(1, 100)
print "\n¡El número ya ha sido generado!"
num_input = raw_input("\nIngrese un número del 1 al 100: ")
num_input = int(num_input)

attemps = 0 #intentos
while num != num_input:
	num_input = raw_input("\n¡Incorrecto! Vuelva a interarlo: ")
	num_input = int(num_input)
	if num_input < num:
		print "\nEl número que ingresó es MENOR al número generado aleatoriamente."
	else:
		if num_input > num:
			print "\nEl número que ingresó es MAYOR al número generado aleatoriamente."
		else:
			if num_input == num:
				print "\n¡FELICIDADES! ¡Has acertado el número!"
	add = num_input + attemps #suma
	attemps = attemps + 1
	if attemps > 9:
		print "\n¡Lo siento! Usted se ha quedado sin intentos :( "
		print "\nEl número generado fue: ", num
		break

print "\nFueron" , attemps, "intentos."
raw_input("\nPresione ENTER para finalizar el programa.")