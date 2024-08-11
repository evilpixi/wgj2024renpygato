label intro:
    scene habitacion base dia
    $ renpy.pause(3)
    

    show habitacion humano
    with dissolve
    $ renpy.pause(2)
    
    show Patricia at truecenter
    with dissolve
    $ renpy.pause(3)

    # Aquí iría la introducción
    g "Desde que llegó esa caja de luz a la casa, todos los días parecen iguales..."
    
    play sound ["meow_attention.mp3"]
    g "¿Estará bien? No parece estar bien. Me gustaría que se diera vuelta y me acariciara como antes."
    g "Ahora casi ni se mueve..."
    g "Sólo se levanta para ir a su caja de agua.. o para buscar comida."
    $ renpy.pause(2)

    g "Esa caja de luz.. lo hipnotiza y le hace olvidar el tiempo."
    g "¿Qué hago para que se levante de la silla? Tengo que investigar... tal vez así Humano vuelva a sonreír."
    $ renpy.pause(2)

    jump dia1