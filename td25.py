#coding=UTF-8


'''
Ejercicio: 25, Tema: Toma de desiciones
Enunciado --> (25.) Ingresar dos valores numéricos que representan las coordenadas cartesianas de un punto en el plano
X,Y. Se desea determinar en que cuadrante se halla el punto.
Nombre del archivo 'td25.py'
Desarrollo del algoritmo en código Python
'''
print "\nSe ingresan las coordenadas cartesianas y se obtiene en que cuadrante está el punto."
x = raw_input("\nIngrese el primer punto X: ")
x = int(x)
y = raw_input("\nIngrese el segundo punto Y: ")
y = int(y)

if x >= 0 and y >= 0:
	print "\nEl punto ingresado se encuentra en el primer cuadrante."
else:
	if x < 0 and y >= 0:
		print "\nEl punto ingresado se encuentra en el segundo cuadrante."
	else:
		if x < 0 and y < 0:
			print "\nEl punto ingresado se encuentra en el tercer cuadrante."
		else:
			if x >= 0 and y < 0:
				print "\nEl punto ingresado se encuentra en el cuarto cuadrante."
raw_input ("\nOprima la tecla ENTER para finalizar.")
