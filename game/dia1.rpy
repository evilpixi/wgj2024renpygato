label dia1:
  scene black with dissolve
  show text "DIA 1"
  pause

  scene habitacion base dia
  show humano sentado dia
  show flores dia
  show pajaro dia
  show papel dia
  show caja dia at Position(xpos=1580, ypos=680)
  show gato neutro at truecenter:
    zoom 0.2
  with dissolve
  
  # Sonido panza
  play sound ["stomach.mp3"] 

  g "Pppprrrrrrr! Pppppprrrrr! Oouh creo que la cena de ayer no me cayó nada bien. Tal vez podría masticar algunas hojitas.. Mmmmm ¡Humano odia que haga eso!"
  g "Ya sé! Si hago eso se va a enojar y va a llevar la planta a la terraza otra vez. En la terraza hay sol y aire..."
  g "Se va a acordar de lo lindo que es estar afuera. ¡Ya no va a estar sentado ni enojado!"
  g "Mmm aunque.. tal vez es mejor hacerlo salir afuera de verdad." 
  g "¿Y si arruino su caja de baño? Sé que prometí no volver a hacerlo pero... ¡es tan divertido!"
  g "Podría jugar un rato con esa serpiente de papel... ¡y a Humano no le quedaría otra que salir a comprar más!" 
  g "Chau silla, chau caja de luz odiosa. Pero.. ¿cuál es la mejor forma de hacer que Humano se levante?"

  # Cambio iluminación -> Tarde
  show habitacion base tarde
  show humano sentado tarde
  show caja tarde at Position(xpos=1580, ypos=680)
  show pajaro tarde
  show papel tarde
  show flores tarde
  show papel tarde

  with dissolve

  # Opciones Dia 1
  menu:
    "Masticar hojitas ñam ñam":
      $ aciertos += 1
      $ comio_planta = True
      jump plantas

    "Jugar con la serpiente de papel":
      $ aciertos += 0
      $ rompio_papel = True
      jump papel

# Opcion comer planta
label plantas:
  play sound ["nam.mp3", "meow_annoyed.mp3"]
  show gato girado with dissolve:
    xpos 620
    ypos 360
    zoom 0.2
    

  $ renpy.pause(1)
  show flores comidas tarde
  $ renpy.pause(3)
  g "Puajj estas hojas no estaban tan ricas como creí. ¿Hace cuánto no las riega?"
  g "No importa, todo sea para que se enoje y suba a la terraza. Puaaj puaaj, ¡Uaaacala!"
  $ renpy.pause(1)
 

  # Humano la mira
  show humano girado tarde
  g "Mientras termino de masticar estas hojas rancias, Humano parece escucharme y gira la cabeza...  Primero observa a la maltrecha plantita y después a mí."
  $ renpy.pause(1)

  h "Nunca creí que iba a decir esto Pat pero..."

  # Patricia lo mira, contenta
  show gato boca abierta:
    xpos 620
    ypos 360
    zoom 0.2
    xzoom -1
  h "...hiciste bien en morder esas hojas, ¡esta planta necesitaba una poda! Y yo últimamente no tengo tiempo ni ganas de nada..."
  $ renpy.pause(1)
  
  # Humano vuelve a mirar la caja de luz
  show humano sentado tarde
  g "¡Tanto mordisquear para nada! La caja de luz volvió a atrapar a Humano." 
  g "Cuando se sienta ahí, se olvida de todo. Nada de sol, nada de terraza. ¿Y ahora qué?" 


  # Cambio iluminación -> Noche
  show humano sentado noche
  show caja noche at Position(xpos=1580, ypos=680)
  show flores comidas noche
  show papel noche
  hide pajaro tarde
  show gato bolita:
    xpos 780
    ypos 620
    zoom 0.9
  show habitacion base noche with dissolve

  play sound ["meow_sad.mp3"]
  g "Cuando se sienta ahí, se olvida de todo. Nada de sol, nada de terraza. ¿Y ahora qué?"
  jump finDia1


# Opcion serpiente de papel
label papel:
  # Patricia se acerca al baño
  show gato girado:
    xpos 1800
    ypos 900
  play sound ["toilet_paper.mp3"]
  g "Meeeeeowwwwwiiii ¡me había olvidado lo divertido que era jugar con la serpiente de papel!"
  play sound ["meow_purr.mp3"]
  
  # Papel desenrollado aparece y Humano mira
  show papel roto tarde
  show humano girado tarde

  # Patricia toda contenta
  show gato boca abierta:
    xpos 1300
    ypos 800
    zoom 0.2
    xzoom -1
  
  g "¡Tengo que seguir haciéndolo todas mis vidas!"
  $ renpy.pause(1)
  
  # Se levanta el humano
  show humano de pie
  g "Mientras araño el papel y lo convierto en tiritas, Humano se acerca a mí."
  g "Me observa primero a mí y después a la gran piel de serpiente blanca desparramada en el piso de madera."
  g "Pero ¡ni siquiera le importa! Tiene un caja gigante llena de serpientes de papel guardadas..."
  $ renpy.pause(2)

  # Se vuelve a sentar el humano
  show humano sentado tarde
  g "Ahora que vuelve a sentarse frente a la caja de luz...." 
  g "No sé.. la diversión se apagó y una serpiente de tristeza se retuerce adentro mío."

  # Cambio iluminación -> Noche
  show humano sentado noche
  show caja noche at Position(xpos=1580, ypos=680)
  hide pajaro tarde
  show flores noche
  show papel roto noche
  show gato bolita:
    xpos 780
    ypos 620
    zoom 0.9
  show habitacion base noche with dissolve

  play sound ["meow_sad.mp3"]
  g "¿No vamos a salir a la plaza nunca más?"
  jump finDia1


# aqui se juntan ambas opciones y se va al día 2
label finDia1:
  scene black with dissolve

  jump dia2