#coding=UTF-8

#Ejercicio de objetos Python, del curso de "Pildoras Informáticas."

class vehiculos(): #herencia

	 def __init__(self, marca, modelo):

		 self.marca = marca
		 self.modelo = modelo
		 self.enMarcha = False
		 self.acelera = False
		 self.frena = False

	 def arrancar (self):

		 self.enMarcha = True

	 def acelerar (self):

		 self.acelera = True

	 def frenar (self):

		 self.frena = True

	 def estado (self):
		print "Marca: " , self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
		self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena #\n salto de línea

class moto(vehiculos):#hacemos que moto herede todas las propiedades anteriores de vehiculos.
	pass 

miMoto = moto("Honda", "CBR") #le pasamos los parametros de vehiculos (el constructor de objetos)

miMoto.estado() #hereda las características

raw_input("Oprima ENTER para finalizar.")