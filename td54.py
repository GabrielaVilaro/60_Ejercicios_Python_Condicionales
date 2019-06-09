
#coding=UTF-8


'''
Ejercicio: 54, Tema: Toma de desiciones
Enunciado --> (54.)De un empleado se conocen: su nombre, categoría a la que pertenece (T= Técnico, A= Administrativo
u O= Operario) y la cantidad de horas trabajadas. Sabiendo que el valor del sueldo por hora según
categoría es: Técnico $ 20,00; Administrativo $ 15; y Operario $ 10,00. Definiendo sueldo neto como la
cantidad de horas trabajadas por el valor correspondiente, y sabiendo que se hacen descuentos del 3%
por Obra Social y 11% por Jubilación. Informar: nombre, sueldo neto, monto de las deducciones y sueldo
a cobrar
Nombre del archivo 'td54.py'
Desarrollo del algoritmo en código Python
'''
def porcentaje(parte, todo):
	return parte / todo * 100

nombre = raw_input("\nIngrese el nombre del empleado: ")
categoria = raw_input("\nIngrese la categoría a la cual pertenece el empleado: ")
cant_horas = raw_input("\nIngrese la cantidad de horas trabajadas: ")
cant_horas = float(cant_horas)

if categoria == "T":
	sueldo_neto = 20 * cant_horas
else:
	if categoria == "A":
		sueldo_neto = 15 * cant_horas
	else:
		if categoria == "O":
			sueldo_neto = cant_horas * 10
		else:
			if categoria != "O" and categoria != "T" and categoria != "A":
				print "\nLa categoría ingresada es inexistente."

obra_soc = porcentaje(3, sueldo_neto)
jubilacion = porcentaje(11, sueldo_neto)

print "\nEl nombre del empleado es: ", nombre
print "\nEl sueldo neto del empleado es: ", sueldo_neto
print "\nEl descuento por Obra Social es de: ", obra_soc
print "\nEl descuento por Jubilación es de: ", jubilacion
print "\nEl sueldo total a cobrar es de: ", sueldo_neto - obra_soc - jubilacion

raw_input("\nOprima la tecla ENTER para finalizar.")

