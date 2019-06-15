#coding=UTF-8

""" UdemyBucles: Ejercicio N°17 - Una empresa les paga a sus empleados 
con base en las horas trabajadas en la semana. Para esto, se registran 
los días que trabajó y las horas de cada día. Realice un algoritmo para 
determinar el sueldo semanal de N trabajadores y además calcule cuánto 
pagó la empresa por los N empleados."""

obreros = raw_input("Ingrese la cantidad de trabajadores: ")
obreros = int(obreros)

sueldo_hs = raw_input("Ingrese el sueldo por hora: ");
sueldo_hs = int(sueldo_hs)

horas_acumuladas = 0

for obreros in range(1, obreros + 1):
	horas_por_obrero = 0
	dias = raw_input("Ingrese los días trabajados: ")
	dias = int(dias)
	for dia in range(1, dias + 1):
		horas = raw_input("Ingrese la cantidad de horas: ")
		horas = int(horas)
		horas_por_obrero = horas_por_obrero + horas
		print "El trabajador tiene de sueldo: ", obreros, horas_por_obrero * sueldo_hs
		horas_acumuladas = horas_acumuladas * horas_por_obrero
		print "El pago a los trabajadores es: ", obreros, horas_acumuladas * sueldo_hs

		raw_input("Oprima ENTER para finalizar el programa.")


