#coding=UTF-8

""" UdemyBucles: Ejercicio N°3 - Algoritmo que pida números hasta 
que se introduzca un cero. Debe imprimir la suma y la media de todos 
los números introducidos."""

num = raw_input("Ingrese 0 para salir: ")
num = int(num)

add = 0
i = 0

while num != 0:
	add = add + num
	i = i + 1
	num = raw_input("Ingrese 0 para salir: ")
	num = int(num)

print "La suma de los números ingresados es: ", add
print "La media de los números ingresados es: ", add / i

