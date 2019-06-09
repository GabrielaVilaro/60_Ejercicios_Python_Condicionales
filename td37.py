#coding=UTF-8


'''
Ejercicio: 37, Tema: Toma de desiciones
Enunciado --> (37.)Realizar un programa que permita ingresar tres datos, (que son valores de distancias entre
localidades). Informar la mayor distancia ingresada.
Nombre del archivo 'td37.py'
Desarrollo del algoritmo en código Python
'''

dato1 = raw_input("\nIngrese la primer distancia: ")
dato1 = int(dato1)
dato2 = raw_input("\nIngrese la segunda distancia: ")
dato2 = int(dato2)
dato3 = raw_input("\nIngrese la tercer distancia: ")
dato3 = int(dato3)

if dato1 > dato2 and dato1 > dato3:
	print "\nLa mayor distancia ingresada es la primera", dato1
else:
	if dato2 > dato1 and dato2 > dato3:
		print "\nLa mayor distancia ingresada es la segunda", dato2 
	else:
		if dato3 > dato2 and dato3 > dato1:
			print "\nLa mayor distancia ingresada es la tercera", dato3

raw_input("\nOprima la tecla ENTER para finalizar.")