label dia2:
  "DIA 2"
  
  "¿Hoy es hoy o todavía es ayer? Ya ni siquiera me doy cuenta, cada día es una eternidad infinita."
  "Humano ya no me mira... sigue atrapado por esa caja de luz, esa maldita luz..."

  "Ffffss Fffssss ¿de dónde viene ese aroma viscoso y delicioso?"
  "¡Creo que está abajo de la cama!"

  #aparece la cuca
  "Ñaaaaaaami, ¡ya puedo saborearlo!"
  "Aunque... pensándolo mejor. Podría cazarlo para Humano... y entonces me miraría a los ojos y diría con su alegre voz: \"¡Pat, esto es una masa! Sos increíble y genial\""


  "Aunque también podría sentarme sobre la caja de luz y aplastar al fin ese meteorito incandescente."
  "Me quedaría cerquita suyo, tan cerca y a oscuras..." 
  "Meeooooww si tan sólo pudiera mirarlo una vez más..."
  "¡lo que daría por mirarlo a los ojos una vez más!"
  "Me quedaría cerquita suyo, tan cerca y a oscuras..." 
  "Meeooooww si tan sólo pudiera mirarlo una vez más..."
  "¡lo que daría por mirarlo a los ojos una vez más!"

  menu:
    "Cazar una cena viscosa para Humano":
      $ aciertos += 1
      jump ofrenda

    "Aplastar la (odiosa) caja de luz":
      $ aciertos += 0
      jump teclado

label ofrenda:
  "¡Meeowwii! Zarpada presa atrapé."
  "Humaaaaaaaaaanoooooooo, ¡mirá lo que tengo para vos!"
  "..."
  "¿Pueden creerlo? Humano miró con asco mi regalo y lo tiró a esa bolsa en donde junta todas esas cosas que ya no le importan más."
  "Lo hizo mientras se tapaba la nariz. Ni siquiera se dio vuelta para agradecerme. Nada."

  "¡¡AAAAAGGGGR RRRRR!! De la bronca empiezo a rasguñar las patas de la cama, le clavo  las garras enfurecida."
  "Pero no sirve de nada... parece como si no existiera."
  "¿Existo? ¿o estoy empezando a desaparecer?"
  jump finDia2

label teclado:
  "El primer salto es fácil, lo conozco de memoria."
  "Cuando llego a las piernas de Humano, vuelvo a saltar y finalmente me acurruco sobre el escritorio, tapando con mi cuerpo la caja de luz."
  "La caja de luz es sorprendentemente cómoda.. ejem digo... ¡¡¡LA ODIO CON TODO EL MEEEEOOOOWWW!!!"
  "Ahora que estoy arriba, giro la cabeza buscando la mirada de Humano."

  "Por un ratito nuestras miradas se encuentran y al fin puedo ver..."
  "...el brillo de sus ojos negros y profundos, como la inmensidad del cielo estrellado. Mi refugio favorito."
  "Pero dura casi nada. Unas nubes grises y espesas atraviesan sus ojos, llevando su pensamientos lejos mío."
  "¿A dónde vas Humano? Estás acá... pero no estás."
  jump finDia2

label finDia2:
  "FIN DEL DIA 2"
  jump dia3