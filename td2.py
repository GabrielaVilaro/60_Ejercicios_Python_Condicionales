#coding=UTF-8


'''
Ejercicio: 2, Tema: Toma de desiciones
Enunciado --> (2.) Mantener el programa anterior de manera tal que se pueda saber si todos los niños recibieron la
misma cantidad de caramelos. Siendo los niños y los caramelos valores no constantes por cada ingreso.
Nombre del archivo 'td2.py'
Desarrollo del algoritmo en código Python
'''

caramelos = raw_input ("Ingrese la cantidad de caramelos que desea repartir: ")
caramelos =int(caramelos)
chicos = raw_input ("Ingrese la cantidad de chicos a los que se les repartirán los caramelos: ")
chicos = int(chicos)
reparto = caramelos / chicos
equidad = caramelos % chicos
print "\nDe los", caramelos, "caramelos, le corresponde a cada uno de los", chicos, "niños", reparto, "unidades."
raw_input("\n\nOprima la tecla ENTER para continuar.")
if equidad == 0:
    print "\nEl reparto de caramelos fue EQUITATIVO."
else:
    print "\nEl reparto de caramelos NO fue EQUITATIVO."
raw_input("\t\n\nOprima la tecla ENTER para terminar.")
