# Personajes
define g = Character("Patricia", color="#926a54")
define h = Character("Humano", color="#28abe7")

# Habitacion
image habitacion humano = "bg/fondo_base_dia_con_humano.png"
image habitacion base dia = "bg/fondo_dia_v2.png"
image habitacion base tarde = "bg/fondo_tarde_v2.png"
image habitacion base noche = "bg/fondo_noche_v2.png"
image final bueno = "bg/fondo_final_bueno_v2.png"
image final malo =  "bg/fondo_final_malo_v2.png"
image final malobis = "bg/fondo_final_malo_v2bis.png"

# Objetos
image caja dia = "bg/objetos/caja_dia.png"
image caja tarde = "bg/objetos/caja_tarde.png"
image caja noche = "bg/objetos/caja_noche.png"
image flores dia = "bg/objetos/flores_dia.png"
image flores tarde = "bg/objetos/flores_tarde.png"
image flores noche = "bg/objetos/flores_noche.png"
image pajaro dia = "bg/objetos/pajaro_dia.png"
image pajaro tarde = "bg/objetos/pajaro_tarde.png"
image red tarde = "bg/objetos/red_tarde.png"
image red noche = "bg/objetos/red_noche.png"
image papel dia = "bg/objetos/papel_dia.png"
image papel tarde = "bg/objetos/papel_tarde.png"
image papel noche = "bg/objetos/papel_noche.png"
image celular = "bg/objetos/celular.png"

# Sucesos
image caja gato dia = "bg/objetos/caja_gato_dia.png"
image caja gato tarde = "bg/objetos/caja_gato_tarde.png"
image caja gato noche = "bg/objetos/caja_gato_noche.png"
image cucaracha = "bg/objetos/cucaracha.png"
image flores comidas dia = "bg/objetos/flores_comidas_dia.png"
image flores comidas tarde = "bg/objetos/flores_comidas_tarde.png"
image flores comidas noche = "bg/objetos/flores_comidas_noche.png"
image papel roto dia = "bg/objetos/papel_roto_dia.png"
image papel roto tarde = "bg/objetos/papel_roto_tarde.png"
image papel roto noche = "bg/objetos/papel_roto_noche.png"
image teclado gato = "bg/objetos/teclado_gato.png"
image red tarde = "bg/objetos/red_tarde.png"
image red noche = "bg/objetos/red_noche.png"

# Gato escena
image gato neutro = "character/gato/gato_neutro.png"
image gato espalda dia = "character/gato/gato_espalda_dia.png"
image gato espalda noche = "character/gato/gato_espalda_noche.png"
image gato girado = "character/gato/gato_girado.png"
image gato flip = "character/gato/gato_neutro_flip.png"
image gato mirada abajo = "character/gato/gato_mirada_abajo.png"
image gato boca abierta = "character/gato/gato_abierta.png"
image gato bolita = "character/gato/gato_bolita.png"

# Gato narrativa
image patricia = "character/narrativa/gato/patricia_normal.png"
image patricia asco = "character/narrativa/gato/patricia_asco.png"
image patricia pregunta = "character/narrativa/gato/patricia_pregunta.png"
image patricia triste = "character/narrativa/gato/patricia_triste.png"
image patricia enojada = "character/narrativa/gato/patricia_enojada.png"

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
image humano nariz = "character/humano/humano_nariz_tarde.png"

# Musica
define musica_fondo = "audio/music/bgmusic.wav"
define musica_final_bueno = "audio/music/goodend_music.wav"
define musica_final_malo_bis = "audio/music/badend_music.wav"



# variables
default aciertos = 0

default comio_planta = False
default rompio_papel = False
default ofrecio_cucaracha = False
default aplasto_teclado = False
default pregunto_pajaro = False
default jugo_caja = False

image Patricia:
    "gato_normal"
    zoom 0.2


# Aquí comienza el juego
label start:
    jump intro