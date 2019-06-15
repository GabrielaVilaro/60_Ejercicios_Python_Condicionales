#coding=UTF-8

#Udemy curso de Python, ejercicio de ejemplo

class Moto():
	"""Atributos, el init es el constructor inicializador"""
	def __init__(self, marca):
		print "Objeto creado."
		self.marca = marca
	"""Métodos"""
	def acelerador(self):
		print "La moto", self.marca, "está acelerando."
	def frenar(self):
		print "La moto", self.marca, "está frenando."

"""Instanciar"""

moto_1 = Moto("CBR")

moto_1.acelerador() #llamar a los métodos
moto_1.frenar() #llamar a los métodos

moto_2 = Moto("Honda") #reutilizo el código
moto_2.frenar() #reutilizo el código

raw_input("Oprima ENTER para finalizar el programa.")