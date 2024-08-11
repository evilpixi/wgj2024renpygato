label dia1:
  scene black with dissolve
  show text "DIA 1"
  pause

  scene habitacion base dia
  show Patricia at truecenter
  show humano sentado dia
  show flores dia
  show papel dia
  show caja dia

  with dissolve
  
  play sound ["stomach.mp3"] 
  show Patricia at left

  g "Pppprrrrrrr! Pppppprrrrr! Oouh creo que la cena de ayer no me cayó nada bien. Tal vez podría masticar algunas hojitas.. Mmmmm ¡Humano odia que haga eso!"
  $ renpy.pause(1)

  g "Ya sé! Si hago eso se va a enojar y va a llevar la planta a la terraza otra vez. En la terraza hay sol y aire..."
  g "Se va a acordar de lo lindo que es estar afuera. ¡Ya no va a estar sentado ni enojado!"
  $ renpy.pause(1)

  g "Mmm aunque.. tal vez es mejor hacerlo salir afuera de verdad." 
  g "¿Y si arruino su caja de baño? Sé que prometí no volver a hacerlo pero... ¡es tan divertido!"
  $ renpy.pause(1)

  g "Podría jugar un rato con esa serpiente de papel... ¡y a Humano no le quedaría otra que salir a comprar más!" 
  g "Chau silla, chau caja de luz odiosa. Pero.. ¿cuál es la mejor forma de hacer que Humano se levante?"

  # Cambio iluminación -> Tarde
  show habitacion base tarde
  show humano sentado tarde
  show pajaro tarde
  show papel tarde
  show flores tarde
  hide papel dia
  show papel tarde

  with dissolve

  menu:
    "Masticar hojitas ñam ñam":
      $ aciertos += 1
      $ comio_planta = True
      jump plantas

    "Jugar con la serpiente de papel":
      $ aciertos += 0
      $ rompio_papel = True
      jump papel

label plantas:
  play sound ["meow_annoyed.mp3"]
  g "Puajj estas hojas no estaban tan ricas como creí. ¿Hace cuánto no las riega?"
  g "No importa, todo sea para que se enoje y suba a la terraza. Puaaj puaaj, ¡Uaaacala!"
  $ renpy.pause(1)
  

  # Planta rota
  show flores comidas tarde 

  # Humano la mira
  hide humano sentado tarde 
  show humano girado tarde
  g "Mientras mastico esas hojas rancias, humano se acerca a mí. Me observa primero a mí y después a la maltrecha plantita."
  $ renpy.pause(1)

  h "Nunca creí que iba a decir esto Pat pero..."
  h "...hiciste bien en morder esas hojas, ¡esta planta necesitaba una poda! Y yo últimamente no tengo tiempo ni ganas de nada..."
  $ renpy.pause(1)
  
  g "¡Tanto mordisquear para nada! Humano volvió a sentarse y admirar la caja de luz.." 


  # Cambio iluminación -> Noche
  show habitacion base noche with dissolve
  hide humano girado tarde
  show humano sentado noche
  show caja noche
  hide pajaro tarde with dissolve
  show flores comidas noche
  show papel noche

  play sound ["meow_sad.mp3"]
  g "Cuando se sienta ahí, se olvida de todo. Nada de sol, nada de terraza. ¿Y ahora qué?"
  jump finDia1


label papel:
  play sound ["meow_purr.mp3", "toilet_paper.mp3"]
  g "Meeeeeowwwwwiiii ¡me había olvidado lo divertido que era jugar con la serpiente de papel!"
  hide papel tarde
  show papel roto tarde
  g "¡Tengo que seguir haciéndolo todas mis vidas!"
  $ renpy.pause(1)
  
  hide humano girado tarde
  show humano de pie
  g "Mientras araño el papel y lo convierto en tiritas, Humano se acerca a mí."
  g "Me observa primero a mí y después a la gran piel de serpiente blanca desparramada en el piso de madera."
  g "Pero ¡ni siquiera le importa! Tiene un caja gigante llena de serpientes de papel guardadas..."
  $ renpy.pause(2)

  g "Ahora que vuelve a sentarse frente a la caja de luz...." 
  g "No sé.. la diversión se apagó y una serpiente de tristeza se retuerce adentro mío."

  # Cambio iluminación -> Noche
  show habitacion base noche with dissolve
  hide humano de pie
  show humano sentado noche
  show caja noche
  hide pajaro tarde with dissolve
  show flores noche
  show papel roto noche
  
  play sound ["meow_sad.mp3"]
  g "¿No vamos a salir a la plaza nunca más?"
  jump finDia1


# aqui se juntan ambas opciones y se va al día 2
label finDia1:
  scene black with dissolve

  jump dia2