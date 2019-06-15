#coding=UTF-8

""" UdemyBucles: Ejercicio N°7 - Realizar una algoritmo que muestre la 
tabla de multiplicar de un número introducido por teclado."""

num = raw_input("Ingrese un número: ")
num = int(num)

for i in range(1, 11):
	producto = num * i
	print num, "x", i, "=", producto
print "Esta fue la tabla de multiplicar del número elegido."
raw_input("Oprima ENTER para finalizar.")

