class Persona:
	def __init__(self, nombre, apellido):
		nombre = self.nombre
		apellido = self.apellido

	def set_nombre(self, nombre):
		nombre = input("Ingrese su nombre: ")

	def set_apellido(self, apellido):
		apellido = input("Ingrese su apellido: ")

	def get_nombre(self, nombre):
		return nombre

	def get_apellido(self, apellido):
		return apellido