#coding=UTF-8


'''
Ejercicio: 3, Tema: Toma de desiciones
Enunciado --> (3.) Mantener el programa anterior el cual detecta la no existencia de caramelos y genere una salida
acorde a ésta circunstancia.
Nombre del archivo 'td3.py'
Desarrollo del algoritmo en código Python
'''

caramelos = raw_input ("Ingrese la cantidad de caramelos que desea repartir: ")
caramelos = int(caramelos)
if caramelos == 0:
    print "No hay caramelos para repartir."
    raw_input("Oprima la tecla ENTER para finalizar.")
else:
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
