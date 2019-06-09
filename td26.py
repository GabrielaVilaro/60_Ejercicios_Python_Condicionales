#coding=UTF-8


'''
Ejercicio: 26, Tema: Toma de desiciones
Enunciado --> (26.) Se ingresan 4 calificaciones de un alumno, informar el promedio de las 3 mejores.
Nombre del archivo 'td26.py'
Desarrollo del algoritmo en código Python
'''


print "\nImprime el promedio de las 3 mejores notas de un alumno."
c1 = raw_input("\nIngrese la primer calificación: ")
c1 = int(c1)
c2 = raw_input("\nIngrese la segunda calificación: ")
c2 = int(c2)
c3 = raw_input("\nIngrese la tercera calificación: ")
c3 = int(c3)
c4 = raw_input("\nIngrese la cuarta calificación: ")
c4 = int(c4)

if c1 < c2 and c1 < c3 and c1 < c4:
	menor = c1
else:
	if c2 < c1 and c2 < c3 and c2 < c4:
		menor = c2
	else:
		if c3 < c1 and c3 < c2 and c3 < c4:
			menor = c3
		else:
			if c4 < c1 and c4 < c2 and c4 < c3:
				menor = c4
promedio = c1 + c2 + c3 + c4 - menor

print "El promedio de las 3 mejores notas es de: ", promedio / 3

raw_input("\nOprime la tecla ENTER para finalizar.")


	

