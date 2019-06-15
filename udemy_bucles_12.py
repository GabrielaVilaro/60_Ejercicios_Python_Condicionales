#coding=UTF-8

""" UdemyBucles: Ejercicio N°12 - Realizar un algoritmo para determinar 
cuánto ahorrará una persona en un año, si al final de cada mes deposita 
cantidades variables de dinero; además, se quiere saber cuánto lleva 
ahorrado cada mes."""

saving = 0

for i in range (1, 13): #months
	monto = raw_input("Ingrese la cantidad de ahorrado este mes: ")
	monto = float(monto)
	saving = saving + monto
print "La cantidad ahorrada por mes es: ", saving

raw_input("Oprima Enter para finalizar.")


