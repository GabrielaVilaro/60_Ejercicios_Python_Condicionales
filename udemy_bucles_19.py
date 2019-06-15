#coding=UTF-8

""" UdemyBucles: Ejercicio N°19 - Realizar un ejemplo de menú, donde 
podemos escoger las distintas opciones hasta que seleccionamos la opción 
de “Salir”."""

while True:
	print "\n1- Electricidad."
	print "\n2- Pinturería."
	print "\n3- Sanitarios."
	print "\n4- Herramientas."
	print "\n5- Salir."

	opcion = raw_input("\nElija la opción que requiera: ")
	opcion = int(opcion)

	if opcion == 1:
		print "\nElectricidad: Cables, Fichas macho/hembra, Puntos y tomas."
	if opcion == 2:
		print "\nPinturería: Pinturas, Esmaltes sintéticos, Latex, Pinceles."
	if opcion == 3:
		print "\nSanitarios: Caños, Accesorios de baño, Siliconas."
	if opcion == 4:
		print "\nHerramientas: Pinzas, Martillos, Hachas, Destornilladores."
	if opcion == 5:
		break
raw_input("\nOprima ENTER para finalizar el programa.")