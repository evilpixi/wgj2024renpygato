label dia1:
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

  # aqui habría que poner la intro de las decisiones

  menu:
    "Comer plantas":
      $ aciertos += 1
      jump plantas

    "Jugar con el papel higiénico":
      $ aciertos += 0
      jump papel


label plantas:
  g "Puajj estas hojas no estaban tan ricas como creí. ¿Hace cuánto no las riega?"
  g "No importa, todo sea para que se enoje y suba a la terraza. Puaaj puaaj, ¡Uaaacala!"
  $ renpy.pause(1)
  
  "Mientras mastico esas hojas rancias, humano se acerca a mí. Se agacha y me observa primero a mí y después a la maltrecha plantita."
  $ renpy.pause(1)

  h "Nunca creí que iba a decir esto Pat pero..."
  h "...hiciste bien en morder esas hojas, ¡esta planta necesitaba una poda! Y yo últimamente no tengo tiempo ni ganas de nada..."
  $ renpy.pause(1)
  
  g "¡Tanto mordisquear para nada! Humano volvió a sentarse y admirar la caja de luz.." 
  g "Cuando se sienta ahí, se olvida de todo. Nada de sol, nada de terraza. ¿Y ahora qué?"
  jump finDia1


label papel:
  g "Meeeeeowwwwwiiii ¡me había olvidado lo divertido que era jugar con la serpiente de papel!"
  g "¡Tengo que seguir haciéndolo todas mis vidas!"
  $ renpy.pause(1)
  
  "Mientras araño el papel y lo convierto en tiritas, Humano se acerca a mí." 
  "Se agacha y me observa primero a mí y después a la gran piel de serpiente blanca desparramada en el piso de madera."
  $ renpy.pause(2)

  "¡Ni siquiera le importa! Ni siquiera se enojó conmigo."
  "Y lo peor es que no va a salir afuera, tiene un caja gigante llena de serpientes de papel..."
  "Sí fue divertido.. pero ahora mientras lo veo volver a sentarse frente a la caja de luz...." 
  "No sé.. algo adentro mío se revuelve, como si la serpiente viviera adentro mío y se retorciera de tristeza."
  "¿No vamos a salir a la plaza nunca más? ¿Qué voy a hacer?"
  jump finDia1


# aqui se juntan ambas opciones y se va al día 2
label finDia1:
  "fin del dia 1"
  jump dia2