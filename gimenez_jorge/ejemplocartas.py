
def renderizar_cartas(mensaje, destinos, remitente):
    for destinario in destinos:
        carta_imprimir = modelo_elegido.replace("(dest)",destinario)
        carta_imprimir = carta_imprimir.replace("(remitente)",remitente)
        print(carta_imprimir)



modelo_1 = "bienvenido (dest), soy (remitente), chau (dest), firma: (remitente)"
modelo_2 = "hasta la vista (dest), soy (remitente), chau (dest), firma: (remitente)"
modelo_3 = "hola (dest), soy (remitente), chau (dest), firma: (remitente)"

lista_modelos = [modelo_1, modelo_2, modelo_3]


sigue_cargando = True
while sigue_cargando:
    modelo_ingresar = input("ingrese modelo: (dest) para destinatario (remitente) para remitente (vaxcio para cortar)")
    if modelo_ingresar == "":
        sigue_cargando = False
    else:
        lista_modelos.append(modelo_ingresar)



lista_destinatarios = []

sigue_cargando = True
while sigue_cargando:
    persona = input("ingrese nombre destinario: (deje vacio para cortar la carga)")
    if persona == "":
        sigue_cargando = False
    else:
        lista_destinatarios.append(persona)

remitente = input("ingrese nombre remitente: ")


for indice, modelo in enumerate(lista_modelos):
    print(indice, end="-")
    print(modelo)

opcion = int(input("seleccione una carta: "))
modelo_elegido = lista_modelos[opcion]


renderizar_cartas(modelo_elegido, lista_destinatarios, remitente)