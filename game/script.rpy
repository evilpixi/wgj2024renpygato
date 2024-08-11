define g = Character("Patricia", color="#926a54")
define h = Character("Norberto", color="#28abe7")

# la cantidad de 
default aciertos = 0

image Patricia:
    "gato"
    zoom 0.2


# Aquí comienza el juego
label start:
    
    scene fondo_base_dia
    $ renpy.pause(3)
    

    show fondo_base_dia_con_humano
    with dissolve
    $ renpy.pause(2)
    
    show Patricia at truecenter
    with dissolve
    $ renpy.pause(3)

    # Aquí iría la introducción
    g "Desde que llegó esa caja de luz a la casa, todos los días parecen iguales..."
    g "¿Estará bien? No parece estar bien. Me gustaría que se diera vuelta y me acariciara como antes."
    g "Ahora casi ni se mueve..."
    g "Sólo se levanta para ir a su caja de agua.. o para buscar comida."
    $ renpy.pause(2)

    g "Esa caja de luz.. lo hipnotiza y le hace olvidar el tiempo."
    g "¿Qué hago para que se levante de la silla? Tengo que investigar... tal vez así Humano vuelva a sonreír."
    $ renpy.pause(2)

    jump dia1

    "este es un cambio de pixi :)"
    "pixi"
    "Pixi invita la cena ;)"
    "pan"
    "Una gata en una habitación con un humano muy ocupado..."

    play music "Sonder.mp3"

    
    show Gata at left
    with dissolve

    g "Qué humano más aburrido..."
    h "mmmh..."

    "Cómo llamarle la atención?"

    menu:
        "Pedir mimos":
            jump mimos

        "Empujar taza":
            jump taza

# opción A y Bad Ending
label mimos:
    play sound ["meow.mp3", "Purr.mp3"]

    show Gata at right
    with dissolve

    $ renpy.pause(3)

    h "salí de acá! Ahora no...!"

    scene photo_album
    with dissolve

    $ renpy.pause(5)
    return


# Opción B y Good Ending
label taza:
    hide Gata   
    h "No empujes la taza..."
    h "..."
    h "Te dije que no!"

    play sound "mug.mp3"

    $ renpy.pause(1)
    h "\*\!\%\§\!"

    scene room_bad_ending
    with dissolve

    $ renpy.pause(5)
    return
