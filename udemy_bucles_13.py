#coding=UTF-8

""" UdemyBucles: Ejercicio N°13- Una empresa tiene el registro de las 
horas que trabaja diariamente un empleado durante la semana (seis días) y 
requiere determinar el total de éstas, así como el sueldo que recibirá 
por las horas trabajadas."""

hs_trabajo = 0

sueldo_hora = raw_input("Ingrese el sueldo por hora del empleado: ")
sueldo_hora = float(sueldo_hora)

for dia in range(1, 7):
	horas = raw_input("¿Cuántas horas trabajó el empleado?: ")
	horas = int(horas)
	hs_trabajo = hs_trabajo + horas
print "Horas de trabajo: ", hs_trabajo
print "El sueldo es de: ", sueldo_hora * hs_trabajo

raw_input("Oprima ENTER para finalizar el programa.")
