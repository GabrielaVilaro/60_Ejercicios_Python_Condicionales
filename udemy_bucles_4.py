#coding=UTF-8

""" UdemyBucles: Ejercicio N°4 - Realizar un algoritmo que pida números 
(se pedirá por teclado la cantidad de números a introducir). El programa 
debe informar de cuantos números introducidos son mayores que 0, menores 
que 0 e iguales a 0.""" 

num = raw_input("Ingrese la cantidad de números a introducir: ")
num = int(num)
amounts = 0
am_ceros = 0 #cantidad de ceros
am_negative = 0
am_positives = 0

while amounts < num:
	numbers = raw_input("Ingrese un número: ")
	numbers = int(numbers)
	amounts = amounts + 1
	if numbers < 0:
		am_negative = am_negative + 1
	if numbers > 0:
		am_positives = am_positives + 1
	if numbers == 0:		
		am_ceros = am_ceros + 1

print "La cantidad de negativos ingresados es de: ", am_negative
print "La cantidad de positivos ingresados es de: ", am_positives
print "La cantidad de ceros ingresados es de: ", am_ceros

raw_input("Oprima ENTER para finalizar el programa.")



