#coding=UTF-8


'''
Ejercicio: 50, Tema: Toma de desiciones
Enunciado --> (50.)Leer el tamaño de cada uno de los tres lados de un triángulo e informar qué tipo de triángulo es:
escaleno, isósceles o equilátero.
Nombre del archivo 'td50.py'
Desarrollo del algoritmo en código Python
'''

lado_a = raw_input("\nIngrese el tamaño del primer lado: ")
lado_a = int(lado_a)
lado_b = raw_input("\nIngrese el tamaño del segundo lado: ")
lado_b = int(lado_b)
lado_c = raw_input("\nIngrese el tamaño del tercer lado: ")
lado_c = int(lado_c)

if lado_a == lado_b and lado_a == lado_c:
    print "\nEl triángulo es EQUILATERO."
if lado_a == lado_b and lado_a != lado_c or lado_a == lado_c and lado_a != lado_b or lado_b == lado_c and lado_b != lado_a:
    print "\nEl triángulo es ISÓSCELES."
if lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
    print "\nEl triángulo es ESCALENO."

raw_input ("\nOprima la tecla ENTER para finalizar.")