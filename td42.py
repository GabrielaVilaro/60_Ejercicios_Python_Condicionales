#coding=UTF-8


'''
Ejercicio: 42, Tema: Toma de desiciones
Enunciado --> (42.) Ingresar las edades y la estatura de tres alumnos de un curso de primer año de la Tecnicatura Superior
en Instalación y Mantenimiento de Sistemas de Cómputo. Se pide:
42.1. Informar la edad promedio.
42.2. Informar la estatura promedio.
42.3. Informar las edades de los alumnos mayores de 20 años que miden menos de 1.60mts.
Nombre del archivo 'td42.py'
Desarrollo del algoritmo en código Python
'''
alumno1Edad = raw_input ("\nIngrese la edad del primer alumno: ")
alumno1Edad = int(alumno1Edad)
alumno1Altura = raw_input("\nIngrese la estatura del primer alumno (En cm): ")
alumno1Altura = int(alumno1Altura)
alumno2Edad = raw_input("\nIngrese la edad del segundo alumno: ")
alumno2Edad = int(alumno2Edad)
alumno2Altura = raw_input("\nIngrese la estatura del segundo alumno (En cm): ")
alumno2Altura = int(alumno2Altura)
alumno3Edad = raw_input("\nIngrese la edad del tercer alumno: ")
alumno3Edad = int(alumno3Edad)
alumno3Altura = raw_input("\nIngrese la estatura del tercer alumno (En cm): ")
alumno3Altura = int(alumno3Altura)

print "\nLa edad promedio de los alumnos es de: ", (alumno1Edad + alumno2Edad + alumno3Edad) / 3, "Años"
print "\nLa estatura promedio de los alumnos es de: " , (alumno1Altura + alumno2Altura + alumno3Altura) / 3, "cm"

if alumno1Edad > 20 and alumno1Altura < 160:
	print "\nLa edad del primer alumno es de: ", alumno1Edad
else:
	if alumno2Edad > 20 and alumno2Altura < 160:
		print "\nLa edad del segundo alumno es de: ", alumno2Edad
	else:
		if alumno3Edad > 20 and alumno3Altura < 160:
			print "\nLa edad del tercer alumno es de: ", alumno3Edad

raw_input ("\nOprima la tecla ENTER para finalizar.")