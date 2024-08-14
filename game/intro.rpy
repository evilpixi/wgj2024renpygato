label intro:
    scene black
    pause 0.2

    play music musica_fondo
    show habitacion base dia
    show humano sentado dia
    show flores dia
    show papel dia
    show caja dia at Position(xpos=1550, ypos=680)

    with dissolve

    $ renpy.pause(2)
    
    # Patricia en la cama, mira hacia el humano
    show gato flip:
        xpos 650
        ypos 500
        zoom 0.2
    with dissolve
    $ renpy.pause(1)


    # Introducción
    show Patricia onlayer top
    g "Desde que llegó esa caja de luz a la casa, todos los días parecen iguales..."
    play sound ["meow_attention.mp3"]
    g "¿Estará bien? No parece estar bien. Me gustaría que se diera vuelta y me acariciara como antes."
    g "Ahora casi ni se mueve..."
    g "Sólo se levanta para ir a su caja de agua.. o para buscar comida."
    $ renpy.pause(2)

    show Patricia triste onlayer top
    g "Esa caja de luz.. lo hipnotiza y le hace olvidar el tiempo."
    show Patricia onlayer top
    g "¿Qué hago para que se levante de la silla? Tengo que investigar... tal vez así Humano vuelva a sonreír."
    $ renpy.pause(0)

    jump dia1