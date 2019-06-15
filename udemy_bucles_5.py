#coding=UTF-8

""" UdemyBucles: Ejercicio N°4 - Algoritmo que pida caracteres e imprima 
‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina 
cuando se introduce un espacio."""

string = raw_input("Ingrese un caracter: ")

for i in string:
	if string.upper() == "A"or string.upper() == "E"or string.upper() == "I"or string.upper() == "O" or string.upper() == "U":
		print "VOCAL."
 	else:
 		print "NO VOCAL."
 	if string == " ":
		break

raw_input("Oprima ENTER para finalizar el programa.")



 	