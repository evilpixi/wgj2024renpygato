label dia2:
  hide Patricia onlayer top with dissolve
  scene black with dissolve
  show text "DIA 2"
  pause
  
  scene habitacion base dia
  
  show humano sentado dia
  show caja dia at Position(xpos=1580, ypos=680)
  show pajaro dia
  
  if comio_planta:
    show flores comidas dia
  else:
    show flores dia

  if rompio_papel:
    show papel roto dia
  else:
    show papel dia

  show gato neutro:
    xpos 620
    ypos 480
    zoom 0.2

  show Patricia onlayer top
  g "¿Hoy es hoy o todavía es ayer? Ya ni siquiera me doy cuenta, cada día es una eternidad infinita."
  g "Humano ya no me mira... sigue atrapado por esa caja de luz, esa maldita luz..."

  show Patricia triste onlayer top  
  g "Ffffss Fffssss ¿de dónde viene ese aroma viscoso y delicioso?"
  
  # Aparece la cuca
  show cucaracha behind gato
  show Patricia contenta onlayer top
  g "¡Mira lo que apareció en la cama!"  
  g "Ñaaaaaaami, ¡ya puedo saborearlo!"
  g "Aunque... pensándolo mejor. Podría cazarlo para Humano... y entonces me miraría a los ojos y diría con su alegre voz: \"¡Pat, esto es una masa! Sos increíble y genial\""
  show Patricia onlayer top
  g "Aunque también podría sentarme sobre la caja de luz y aplastar al fin ese meteorito incandescente."
  g "Me quedaría cerquita suyo, tan cerca y a oscuras..." 
  show Patricia triste onlayer top
  g "Meeooooww si tan sólo pudiera mirarlo una vez más..."

  # Cambio iluminación -> Tarde
  hide Patricia onlayer top with dissolve
  show habitacion base tarde with dissolve
  show humano sentado tarde
  show pajaro tarde behind humano
  show caja tarde at Position(xpos=1580, ypos=680)

  if comio_planta:
    show flores comidas tarde behind humano
  else:
    show flores tarde behind humano

  if rompio_papel:
    show papel roto tarde
  else:
    show papel tarde

  # Opciones Dia 2
  menu:
    "Cazar una cena viscosa para Humano":
      $ aciertos += 1
      $ ofrecio_cucaracha = True
      jump ofrenda

    "Aplastar la (odiosa) caja de luz":
      $ aciertos += 0
      $ aplasto_teclado = True
      jump teclado

# Opcion cuca
label ofrenda:
  # Patricia atrapa la cucaracha
  show gato mirada abajo flip:
    xpos 741
    ypos 451
    zoom 0.2
  show cucaracha behind gato

  show Patricia contenta onlayer top
  g "¡Meeowwii! Zarpada presa atrapé."
  show gato boca abierta behind humano:
    xpos 779
    ypos 451
    zoom 0.2
  show cucaracha behind gato
  play sound ["meow.mp3"]
  g "Humaaaaaaaaaanoooooooo, ¡mirá lo que tengo para vos!"

  pause 0.5
  
  # Humano la mira
  show humano girado tarde
  g "..."
  
  # Humano se levanta, gata contenta

  show humano nariz:
    xpos 600
    ypos 1200
    zoom 1.2

  show Patricia enojada onlayer top
  g "¿Pueden creerlo? Humano miró con asco mi regalo y lo tiró a esa bolsa en donde junta todas esas cosas que ya no le importan más."
 
  # Humano vuelve a sentarse, cuca aparece en la basura
  hide humano nariz
  show humano sentado tarde
  show cucaracha behind gato at Position(xpos=1400)

  # Patricia de espalda mirando la basura
  show gato espalda dia:
    xpos 1260
    ypos 630
    zoom 0.7

  g "Lo hizo mientras se tapaba la nariz. Ni siquiera se dio vuelta para agradecerme. Nada."
  g "¡MEEAAAOOWW! Quisiera rasguñar esa caja, clavarle las garras hasta apagarla... Pero Humano nunca me dejaría."
  play sound ["meow_begging.mp3"]
  show Patricia triste onlayer top
  g "Meeow.. me siento tan triste."
  g "Hay algo adentro mío que se está apagando.. ¡si tan sólo me abrazara una vez más!"

  # Cambio iluminación -> Noche
  if comio_planta:
    show flores comidas noche
  else:
    show flores noche

  if rompio_papel:
    show papel roto noche
  else:
    show papel noche
  
  show humano sentado noche
  show caja noche at Position(xpos=1580, ypos=680)
  hide pajaro tarde
  hide cucaracha
  show gato bolita:
    xpos 660
    ypos 560
    zoom 0.9
  show habitacion base noche with dissolve

  g "¿Existo? ¿o estoy empezando a desaparecer?"
  jump finDia2

# Opcion teclado
label teclado:
  show Patricia onlayer top
  g "El primer salto es fácil, lo conozco de memoria."
  show gato flip:
    xpos 490
    ypos 250
    zoom 0.2
  hide cucaracha with dissolve
  
  g "Cuando llego a las piernas de Humano, vuelvo a saltar y finalmente me acurruco sobre el escritorio, tapando con mi cuerpo la caja de luz."
  # Aparece Patricia sobre teclado
  hide gato neutro
  show teclado gato with dissolve

  g "La caja de luz es sorprendentemente cómoda.. ejem digo... ¡¡¡LA ODIO CON TODO EL MEEEEOOOOWWW!!!"
  g "Ahora que estoy arriba, giro la cabeza buscando la mirada de Humano."
  g "Por un ratito nuestras miradas se encuentran y al fin puedo ver..."
  show Patricia contenta onlayer top
  g "Sus profundos ojos negros, como la inmensidad del cielo estrellado. Mi refugio favorito."
  show Patricia triste onlayer top
  g "Pero no dura nada. Unas nubes grises y espesas atraviesan su mirada, llevando sus pensamientos lejos mío."
  
  # Cambio iluminación -> Noche
  if comio_planta:
    show flores comidas noche
  else:
    show flores noche

  if rompio_papel:
    show papel roto noche
  else:
    show papel noche
  
  hide pajaro tarde
  hide teclado gato
  show humano sentado noche
  show caja noche at Position(xpos=1580, ypos=680)
  show gato bolita:
    xpos 660
    ypos 560
    zoom 0.9
  show habitacion base noche with dissolve



  play sound ["meow_begging.mp3"]
  g "¿A dónde vas Humano? Estás acá... pero no estás."
  jump finDia2

label finDia2:
  scene black with dissolve
  
  jump dia3