#coding=UTF-8


'''
Ejercicio: 19, Tema: Toma de desiciones
Enunciado --> (19.) De una exposición de libros se conocen las cantidades de libros de autores argentinos,
latinoamericanos, europeos y asiáticos que hay. Se pide hacer un programa que informe:
19.1. La cantidad total de libros que hay en la exposición.
19.2. Que porcentaje del total le corresponde a cada una de las cantidades ingresadas.
19.3. Cual es el nivel de la exposición, considerando que puede ser: MALO, BUENO, MUY BUENO,
EXCELENTE o SOBRESALIENTE si la cantidad de obras expuestas es menor que 5000, 10000,
20000, 30000 o 40000 respectivamente.
Nombre del archivo 'td19.py'
Desarrollo del algoritmo en código Python
'''
def porcentaje(parte, todo):
    return parte * 100 / todo


argentinos = 4500
latinos = 6780
euro = 12000
asiaticos = 3800
total = argentinos + latinos + euro + asiaticos

print "\nLa cantidad total de libros que hay en la exposición es de: ", total
print "\nEl porcentaje de libros de autores Argentinos es: ","%", porcentaje (argentinos, total)
print "\nEl porcentaje de libros de autores Latinoamericanos es: " ,"%", porcentaje (latinos, total)
print "\nEl porcentaje de libros de autores Europeos es: ","%", porcentaje (euro, total)
print "\nEl porcentaje de libros de autores Asiáticos es: " ,"%", porcentaje (asiaticos, total)

if total < 5000:
	print "\nEl nivel de la exposición es MALO."
else:
	if total < 10000:
		print "\nEl nivel de la exposición es BUENO"
	else:
		if total < 20000:
			print "\nEl nivel de la exposición es MUY BUENO"
		else:
			if total < 30000:
				print "\nEl nivel de la exposición es EXCELENTE"
			else:
				if total < 40000:
					print "\nEl nivel de la exposición es SOBRESALIENTE"


raw_input("\nOprima la tecla ENTER para finalizar.")