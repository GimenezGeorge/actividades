def renderizar_cartas(mensaje, destinatario, remitente):
	for destinatario in destinatarios:
		carta_imprimir = modelo_elegido.replace("(destinatario)", destinatario)
		carta_imprimir = carta_imprimir.replace("(remitente)", remitente)
		print(carta_imprimir)

modelo_1 = "hola (destinatario), soy (remitente), chau (destinatario), firma: (remitente)"
modelo_2 = "bienvenido (destinatario), soy (remitente), chau (destinatario), firma: (remitente)"
modelo_3 = "holis (destinatario), soy (remitente), chau (destinatario), firma: (remitente)"
lista_modelos = [modelo_1, modelo_2, modelo_3]

sigue_cargando = True
while sigue_cargando:
	modelo_ingresar = input("Ingrese modelo: (desitinatario) para desitinatario, (remitente) para remitente")
	if modelo == "":
		sigue_cargando = False
	else:
		modelo_ingresar.append(modelo) #Roto

destinatarios = []

sigue_cargando = True
while sigue_cargando:
	persona = input("Ingrese nombre destinatario: (Deje vacío para corta la carga)")
	if persona == "":
		sigue_cargando = False
	else:
		destinatarios.append(persona)

remitente = input("Ingrese nombre remitente")

for indice, modelo in enumerate(lista_modelos):
	print(indice, end=".")
	print(modelo)

opcion = int(input("Seleccione una carta: "))
modelo_elegido = lista_modelos[opcion]

renderizar_cartas(modelo_elegido, destinatarios, remitente)