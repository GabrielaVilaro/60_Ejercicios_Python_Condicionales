#coding=UTF-8

""" UdemyBucles: Ejercicio N°11 - Escribe un programa que diga si un 
número introducido por teclado es o no primo. Un número primo es aquel 
que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente 
probar hasta la raíz cuadrada del número para ver si es divisible por 
algún otro número."""

es_primo = True

num = raw_input("Ingrese un número: ")
num = int(num)

for i in range(2, num):
        if num % i == 0:
            es_primo = False
if es_primo:
	print "Es primo."
else:
	print "No es primo."

raw_input("Oprima la tecla ENTER para finalizar el programa.")