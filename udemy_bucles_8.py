#coding=UTF-8

""" UdemyBucles: Ejercicio N°8 - Escribe un programa que pida el limite 
inferior y superior de un intervalo. Si el límite inferior es mayor que 
el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
•	La suma de los números que están dentro del intervalo 
(intervalo abierto).
•	Cuantos números están fuera del intervalo.
•	He informa si hemos introducido algún número igual a los límites 
del intervalo."""

add_in_intervalo = 0
cont_out_intervalo = 0
igual_lim = False
while True:
 	lim_inf = raw_input("Ingrese el límite inferior del intervalo: ")
 	lim_inf = int(lim_inf)
 	lim_sup = raw_input("Ingrese el límite superior del intervalo: ")
 	lim_sup = int(lim_sup)

 	if lim_inf > lim_sup:
 		print "Error, el límite inferior no puede ser mayor al superior."
 	if lim_inf <= lim_sup:
 		break
num = raw_input("Ingrese el número 0 (cero) para salir.")
num = int(num)

while num != 0:
 	if num > lim_inf and num < lim_sup:
 		add_in_intervalo = add_in_intervalo + num
 	else:
 		cont_out_intervalo = cont_out_intervalo + 1
num = raw_input("Ingrese el número 0 (cero) para salir. ")
num = int(num)

print "La suma dentro del intervalo es: ", add_in_intervalo
print "La cantidad de números afuera del intervalo es: ", cont_out_intervalo
if igual_lim:
	"Se ha ingresado algún valor igual a los límites del intervalo."
else:
	print "No se ha introducido ningún número igual a los límites del intervalo."

raw_input("Oprima ENTER para finalizar el programa.")

