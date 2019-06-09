#coding=UTF-8


'''
Ejercicio: 55, Tema: Toma de desiciones
Enunciado --> (55.)Escribir un algoritmo que lea el peso, en libras, de un objeto y que éste calcule y emita su peso en
gramos y/o kilogramos según corresponda; teniendo en cuenta que 1 libra es igual a 453 gramos.
Nombre del archivo 'td55.py'
Desarrollo del algoritmo en código Python
'''

peso_libras = raw_input("\nIngrese el peso en libras de un objeto: ")
peso_libras = float(peso_libras)

gramos = peso_libras * 453
kilos = peso_libras * 0.453

print "\nEl peso ingresado en libras es de: ", peso_libras
print "\nEl peso ingresado en gramos es de: ", gramos
print "\nEl peso ingresado en kilogramos es de: ", kilos

raw_input("\nOprima la tecla ENTER para finalizar.")
