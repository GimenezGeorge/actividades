# Función que reciba como parametros dos números (a y b), y
# devuelva una tupla con todos los números primos que se encuentra entre
# a y b (incluyendo a y b si son primos).
#  Por defecto a=0, y b=100

def generar_primos(a, b):
	
	numero = 0

	yield numero

	while True:
		temp = numero
		while True:
			temp += 1
			contador = 1
			contador_divisores = 0

			while contador <= temp:
				if temp % contador == 0:
					contador_divisores += 1
				
				if contador_divisores > 2:
					break
				
				contador += 1
			
			if contador_divisores == 2:
				yield temp

# No se como darle la orden de que cuente solo entre 0 y 100.
g = generar_primos(0, 100)
primos = [next(g) for _ in range(26)]
print(primos)

