#coding=UTF-8

""" UdemyBucles: Ejercicio N°16 - Una empresa les paga a sus empleados 
con base en las horas trabajadas en la semana. Realice un algoritmo para
 determinar el sueldo semanal de N trabajadores y, además, calcule 
 cuánto pagó la empresa por los N empleados."""

obreros = raw_input("Ingrese la cantidad de trabajadores: ")
obreros = int(obreros)

hs_semana = raw_input("Ingrese las horas semanales de trabajo: ")
hs_semana = int(hs_semana)

pago_total_semanal = 0

for i in range(0, obreros):
	obreros = i + 1
	pago_total_semanal = obreros * hs_semana

print "El sueldo semanal por cada empleado es: ", pago_total_semanal


