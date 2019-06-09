#coding=UTF-8


'''
Ejercicio: 40, Tema: Toma de desiciones
Enunciado --> (40.)Ingresar la cantidad de horas trabajadas por un empleado, la categoría en que se desempeña, y un
número de empleado, se debe calcular y luego informar:
40.1. Sueldo del empleado.
40.2. El número del empleado y su sueldo si éste supera a los $ 1500.
Valor por hora es de: categorías 1, 2 y 3, pesos 20, 25 y 33 respectivamente.
Nombre del archivo 'td40.py'
Desarrollo del algoritmo en código Python
'''
n_empleado = raw_input("\nIngrese el número del empleado: ")
n_empleado = int(n_empleado)
hs_trabajadas = raw_input("\nIngrese la cantidad de horas trabajadas por el empleado: ")
hs_trabajadas = int(hs_trabajadas)
categoria = raw_input("\nIngresar la categoría del empleado (del 1 al 3): ")
categoria = int(categoria)

if categoria == 1:
	sueldo = 20 * hs_trabajadas
	print "\nEl sueldo del empleado", n_empleado, "es de:$", sueldo
	if sueldo > 1500:
		print "El suelo del empleado supera los $1500."
else:
	if categoria == 2:
		sueldo = 25 * hs_trabajadas
		print "\nEl sueldo del empleado ", n_empleado, "es de: $", sueldo
		if sueldo > 1500:
			print "\nEl sueldo del empleado supera los $1500."
	else:
		if categoria == 3:
			sueldo = 33 * hs_trabajadas
			print "\nEl sueldo del empleado ", n_empleado, "es de: $", sueldo
		else:
			if categoria > 4:
				print "\nLa categoria ingresada NO existe."

raw_input("\nOprima la tecla ENTER para finalizar.")