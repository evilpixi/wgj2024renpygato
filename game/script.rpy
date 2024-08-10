define g = Character("Gata", color="#089ea8")
define h = Character("Humano", color="#e8a43f")

image Gata:
    "gata"
    zoom 0.1

# The game starts here.

label start:
    
    scene room
    with dissolve

    "este es un cambio de pixi :)"
    "pixi"
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
