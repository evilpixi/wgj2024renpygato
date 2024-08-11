# Personajes
define g = Character("Patricia", color="#926a54")
define h = Character("Humano", color="#28abe7")

# Habitacion
image habitacion humano = "bg/fondo_base_dia_con_humano.png"
image habitacion base dia = "bg/fondo_base_dia.png"
image habitacion base noche = "bg/fondo_base_noche.png"

# Objetos
image caja dia = "bg/objetos/caja_dia.png"
image caja noche ="bg/objetos/caja_noche.png"
image flor dia = "bg/objetos/flores_dia.png"
image flor noche = "bg/objetos/flores_noche.png"
image pajaro = "bg/objetos/pajaro.png"
image papel = "bg/objetos/papel.png"
image celular = "bg/objetos/celular.png"

# Sucesos
image caja gato = "bg/sucesos/cajaa_gato.png"
image celular roto = "bg/sucesos/celular.png"
image cucaracha = "bg/sucesos/cucaracha.png"
image flor rota dia = "bg/sucesos/flor_dia.png"
image flor rota noche = "bg/sucesos/flor_noche.png"
image papel roto = "bg/sucesos/papel.png"
image teclado gato = "bg/sucesos/teclado_gato.png"



# la cantidad de 
default aciertos = 0

image Patricia:
    "gato"
    zoom 0.2


# Aquí comienza el juego
label start:
    jump intro