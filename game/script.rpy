# Personajes
define g = Character("Patricia", color="#926a54")
define h = Character("Humano", color="#28abe7")

# Habitacion
image habitacion humano = "bg/fondo_base_dia_con_humano.png"
image habitacion base dia = "bg/fondo_dia.png"
image habitacion base tarde = "bg/fondo_tarde.png"
image habitacion base noche = "bg/fondo_noche.png"

# Humano narrativa
image humano neutro cerrada = "character/humano/humano_neutro_boca_cerrada.png"
image humano neutro abierta = "character/humano/humano_neutro_boca_abierta.png"
image humano molesto cerrada = "character/humano/humano_molesto_boca_cerrada.png"
image humano molesto abierta = "character/humano/humano_molesto_boca_abierta.png"


# Humano escena
image humano sentado dia = "character/humano/humano_sentado_dia.png"
image humano sentado tarde = "character/humano/humano_sentado_tarde.png"
image humano sentado noche = "character/humano/humano_sentado_noche.png"
image humano girado dia = "character/humano/humano_sentado_girado_dia.png"
image humano girado tarde = "character/humano/humano_sentado_girado_tarde.png"
image humano girado noche = "character/humano/humano_sentado_girado_noche.png"
image humano de pie = "character/humano/humano_de_pie.png"

# Musica
define musica_fondo = "audio/music/bgmusic.wav"
define musica_final_bueno = "audio/music/goodend_music.wav"
define musica_final_malo = "audio/music/badend_music.wav"

# Objetos
image caja dia = "bg/objetos/caja_dia.png"
image caja noche ="bg/objetos/caja_noche.png"
image flores dia = "bg/objetos/flores_dia.png"
image flores tarde = "bg/objetos/flores_tarde.png"
image flores noche = "bg/objetos/flores_noche.png"
image pajaro dia = "bg/objetos/pajaro_dia.png"
image pajaro tarde = "bg/objetos/pajaro_tarde.png"
image red tarde = "bg/objetos/red_tarde.png"
image red noche = "bg/objetos/red_noche.png"
image papel = "bg/objetos/papel.png"
image celular = "bg/objetos/celular.png"

# Sucesos
image caja gato = "bg/sucesos/cajaa_gato.png"
image celular roto = "bg/sucesos/celular.png"
image cucaracha = "bg/sucesos/cucaracha.png"
image flores comidas dia = "bg/objetos/flores_comidas_dia.png"
image flores comidas tarde = "bg/objetos/flores_comidas_tarde.png"
image flores comidas noche = "bg/suceobjetossos/flores_comidas_noche.png"
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