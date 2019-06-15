#coding=UTF-8


#personajes en python

class Personaje():

	def __init__(self, nombre, salud, color):
		self.nombre = nombre
		self.salud = salud
		self.color = color

	def nombra(self):
		print "El nombre de su personaje es: ", self.nombre

	def vida(self):
		print "Su personaje", self.nombre, "cuenta con ", self.salud, "de salud."

	def colors(self):
		print "Su personaje", self.nombre, "es de color ", self.color

	def camina(self):
		self.mueve = True

	def caminar(self):
		if self.mueve:
			return "El personaje camina."
		else:
			return "El personaje no camina."


elfo = Personaje("Elfo", 100, "Verde")

elfo.nombra()

elfo.vida()

elfo.colors()

elfo.camina()

print elfo.caminar()

gnomo = Personaje("Gnomo", 85, "Azul")

gnomo.nombra()

gnomo.vida()

gnomo.colors()

raw_input("Oprima la tecla ENTER para finalizar el programa.")

