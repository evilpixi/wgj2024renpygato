label dia2:
  show text "DIA 2"
  pause
  
  scene habitacion base dia with dissolve
  show Patricia at truecenter
  show humano sentado dia
  show caja dia

  $ renpy.pause(2)
  show pajaro dia with dissolve
  $ renpy.pause(2)
  
  # agregar sonido hornero: play sound ["pajaro.mp3"] 
  
  g "¿Hoy es hoy o todavía es ayer? Ya ni siquiera me doy cuenta, cada día es una eternidad infinita."
  g "Humano ya no me mira... sigue atrapado por esa caja de luz, esa maldita luz..."

  g "Ffffss Fffssss ¿de dónde viene ese aroma viscoso y delicioso?"
  g "¡Creo que está arriba de la cama!"

  #aparece la cuca
  g "Ñaaaaaaami, ¡ya puedo saborearlo!"
  g "Aunque... pensándolo mejor. Podría cazarlo para Humano... y entonces me miraría a los ojos y diría con su alegre voz: \"¡Pat, esto es una masa! Sos increíble y genial\""

  g "Aunque también podría sentarme sobre la caja de luz y aplastar al fin ese meteorito incandescente."
  g "Me quedaría cerquita suyo, tan cerca y a oscuras..." 
  g "Meeooooww si tan sólo pudiera mirarlo una vez más..."
  g "¡lo que daría por mirarlo a los ojos una vez más!"
  g "Me quedaría cerquita suyo, tan cerca y a oscuras..." 

  # Cambio iluminación -> Tarde
  show habitacion base tarde with dissolve
  hide humano sentado dia
  show humano sentado tarde
  hide pajaro dia
  show pajaro tarde

  menu:
    "Cazar una cena viscosa para Humano":
      $ aciertos += 1
      jump ofrenda

    "Aplastar la (odiosa) caja de luz":
      $ aciertos += 0
      jump teclado

label ofrenda:
  g "¡Meeowwii! Zarpada presa atrapé."

  play sound ["meow.mp3"]
  g "Humaaaaaaaaaanoooooooo, ¡mirá lo que tengo para vos!"
  g "..."
  g "¿Pueden creerlo? Humano miró con asco mi regalo y lo tiró a esa bolsa en donde junta todas esas cosas que ya no le importan más."
  g "Lo hizo mientras se tapaba la nariz. Ni siquiera se dio vuelta para agradecerme. Nada."

  g "¡¡AAAAAGGGGR RRRRR!! De la bronca empiezo a rasguñar las patas de la cama, le clavo  las garras enfurecida."
  g "Pero no sirve de nada... parece como si no existiera."

  # Cambio iluminación -> Noche
  show habitacion base noche with dissolve
  hide humano sentado tarde
  show humano sentado noche
  hide caja dia
  show caja noche
  hide pajaro tarde
  play sound ["meow_begging.mp3"]
  g "¿Existo? ¿o estoy empezando a desaparecer?"
  jump finDia2

label teclado:
  g "El primer salto es fácil, lo conozco de memoria."
  g "Cuando llego a las piernas de Humano, vuelvo a saltar y finalmente me acurruco sobre el escritorio, tapando con mi cuerpo la caja de luz."
  g "La caja de luz es sorprendentemente cómoda.. ejem digo... ¡¡¡LA ODIO CON TODO EL MEEEEOOOOWWW!!!"
  g "Ahora que estoy arriba, giro la cabeza buscando la mirada de Humano."

  g "Por un ratito nuestras miradas se encuentran y al fin puedo ver..."
  g "Sus profundos ojos negros, como la inmensidad del cielo estrellado. Mi refugio favorito."
  g "Pero no dura nada. Unas nubes grises y espesas atraviesan sus mirada, llevando sus pensamientos lejos mío."
  
  # Cambio iluminación -> Noche
  show habitacion base noche with dissolve
  hide humano sentado tarde
  show humano sentado noche
  play sound ["meow_begging.mp3"]
  g "¿A dónde vas Humano? Estás acá... pero no estás."
  jump finDia2

label finDia2:
  scene black with dissolve
  
  jump dia3