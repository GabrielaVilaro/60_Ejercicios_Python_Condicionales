#coding=UTF-8


'''
Ejercicio: 62, Tema: Toma de desiciones
Enunciado --> (62.)Ingresar el nombre y el apellido de un alumno y sus evaluaciones que fueron N1, N2 y N3. Calcular el
promedio y emitir un mensaje que diga:”El alumno XXX obtuvo una calificación XXXX”, donde se
utilizará una constante que contenga la leyenda correpondiente, según el siguiente cuadro:
Promedio 0 < promedio < 4 Constante IN Calificación Insuficiente
4 <= promedio < 6 SF Suficiente
5 < promedio < 7 BI Bien
7 <= promedio <= 8 NT Notable
9 <= promedio = 10 SO Sobresaliente
Nombre del archivo 'td62.py'
Desarrollo del algoritmo en código Python
'''
nombre = raw_input("Ingrese el nombre del alumno: ")
apellido = raw_input ("Ingrese el apellido del alumno: ")
nya = nombre + apellido

n1 = raw_input("\nIngrese la primer calficación del alumno: ")
n1 = int(n1)
n2 = raw_input("\nIngrese la segunda calificación del alumno: ")
n2 = int(n2)
n3 = raw_input("\nIngrese la tercera calificación del alumno: ")
n3 = int(n3)

suma = n1 + n2 + n3

promedio = suma / 3

IN = "\nInsuficiente."
SF = "\nSuficiente."
BI = "\nBien."
NT = "\nNotable."
SO = "\nSobresaliente."

if promedio > 0 and promedio < 4:
	print "\nEl alumno ",nombre, apellido, "obtuvo una calificación: ", IN
else:
	if promedio >= 4 and promedio < 6:
		print "\nEl alumno ",nombre, apellido, "obtuvo una calificación: ", SF
	else:
		if promedio >= 5 and promedio < 7:
			print "\nEl alumno ",nombre, apellido, "obtuvo una calificación: ", BI
		else:
			if promedio >= 7 and promedio <= 8:
				print "\nEl alumno ",nombre, apellido, "obtuvo una calificación: ", NT
			else:
				if promedio >= 9 and promedio == 10:
					print "\nEl alumno ",nombre, apellido, "obtuvo una calificación: ", SO

raw_input("\nOprima la tecla ENTER para finalizar.")
