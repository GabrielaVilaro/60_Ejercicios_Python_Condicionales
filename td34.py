#coding=UTF-8


'''
Ejercicio: 34, Tema: Toma de desiciones
Enunciado --> (34.)Ingresar las medidas de los lados de un triángulo. Informar si es escaleno, isósceles o equilátero.
Nombre del archivo 'td34.py'
Desarrollo del algoritmo en código Python
'''

print "\nIngrese las medidas de los lados de un triángulo para saber si es escaleno, isósceles o equilátero"
lado1 = raw_input("\nIngrese el primer lado: ")
lado1 = int(lado1)
lado2 = raw_input("\nIngrese el segundo lado: ")
lado2 = int(lado2)
lado3 = raw_input("\nIngrese el tercer lado: ")
lado3 = int(lado3)

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
 	print "\nNO es un triángulo."
else:
	if lado1 == lado2 == lado3:
		print "\nEl triángulo es equilátero."
	else:
		if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
			print "\nEl triángulo es isósceles."
		else:
			if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
				print "\nEl triángulo es escaleno"

raw_input("\nprima la tecla ENTER para finalizar.")