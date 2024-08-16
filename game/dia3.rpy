label dia3:
  hide Patricia onlayer top with dissolve
  scene black with dissolve
  show text "DIA 3"
  pause

  scene habitacion base dia 
  show humano sentado dia
  show caja dia at Position(xpos=1580, ypos=680)
  show pajaro dia
  show gato flip:
    xpos 870
    ypos 370
    zoom 0.2
  
  if comio_planta:
    show flores comidas dia behind gato
  else:
    show flores dia behind gato

  if rompio_papel:
    show papel roto dia behind gato
  else:
    show papel dia behind gato
    
  $ renpy.pause(2)
  
  show Patricia onlayer top
  g "Abro los ojos y bostezo. Otra vez todo es igual... no me sorprende."
  show Patricia triste onlayer top
  g "Humano sentado enfrente de la caja maldita, la comida sin gusto a nada y ese pájaro que todos los días se queda mirándome desde la ventana..."
  
  
  play sound ["hornero.mp3"]
  show Patricia onlayer top
  show gato parado:
    xpos 700
    ypos 450
    zoom 0.2
  g "¿por qué me mira, qué quiere?"
  show Patricia enojada onlayer top
  g "Ya fue, me cansé. Necesito que algo cambie, ¡lo necesito desesperadamente!"
  show Patricia onlayer top
  g "Si no hay nada que yo pueda hacer, tal vez.. tal vez el pájaro sea la respuesta."
  show Patricia onlayer top
  g "Me acerco despacio a la ventana, pero en el camino mi suave cola marroncita roza una de las cajas de cartón.."
  show Patricia contenta onlayer top
  g "¡qué sensación increíble! Se siente casi.. casi como una caricia."
  
  # Patricia se mueve
  show Patricia onlayer top
  g "¿Qué voy a hacer? ¿El pájaro realmente va a ayudarme a despertar a Humano?"
  g "¿Y si me rindiera? Humano no va a dejar su caja de luz..."
  g "¿Qué pasaría si eligiera quedarme entre las cajas... si eligiera la caricia del cartón?"
  
  # Cambio iluminación -> Tarde
  hide Patricia onlayer top with dissolve
  show habitacion base tarde with dissolve
  hide humano sentado dia
  show humano sentado tarde
  
  if comio_planta: 
    show flores comidas tarde behind gato
  else:
    show flores tarde behind gato

  if rompio_papel:
    show papel roto tarde
  else:
    show papel tarde

  show pajaro tarde

  # Opciones Dia 3
  menu:
    "Preguntarle la posta al pájaro":
      $ aciertos += 0
      jump ventana

    "Entregarse a la caricia del cartón":
      $ aciertos += 1
      jump caja

# Opcion pajaro
label ventana:
  show Patricia onlayer top
  g "Decido confiar en el pájaro y sigo avanzando hacia la ventana, esquivando las cajas.."
 
  # Patricia se mueve al lado del pájaro y lo mira
  show gato girado:
    xpos 550
    ypos 250
    zoom 0.2
    xzoom -1
  g "Mientras trepo por el acolchado, siento el calor del sol acariciándome el lomo. Rayos de luz atraviesan la ventana y me envuelven en una calidez antigua, lejana y permanente."
  g "Desde la ventana veo la plaza: árboles frondosos y fuentes de agua, una nena con trenzas sostiene un barrilete naranja."
  
  play sound ["meow_far.mp3"]
  show Patricia contenta onlayer top
  g "Saludo al pájaro - Meeeowwwlaa!- mientras el olor a verano despeina mis bigotes. Él se acerca y yo siento como si estuviera sosteniendo un secreto con el pico, sólo para mí."
  show Patricia pregunta onlayer top
  g "Cuando está a punto de abrir el pico, saludarme o tal vez soltar el secreto... escucho un grito de terror que me pone los pelos de punta...."

  # Humano la mira
  show humano girado tarde
  show Patricia asco onlayer top
  show Humano enojado onlayer top
  h "¡¿¡PATRICIA QUÉ HACES!?! ¡BAJATE DE AHÍ!"

  # Patricia se vuelve a la cama
  show gato neutro:
    xpos 700
    ypos 500
    zoom 0.2

  g "Humano al fin me mira... pero está asustado y nervioso."
  show Patricia triste onlayer top
  g "Quiero explicarle que estoy bien, quiero hablarle del secreto del pájaro, pero me agarra con las manos temblorosas y me aleja de la ventana."
  
  # Humano vuelve a mirar en frente
  hide Humano onlayer top
  hide Patricia onlayer top with dissolve
  hide pajaro tarde
  show humano sentado tarde 

  # Aparece reja ventana
  $ renpy.pause(2) 

  show red tarde behind flores

  $ renpy.pause(2)
  # Cambio iluminación -> Noche
  if comio_planta: 
    show flores comidas noche
  else:
    show flores noche

  if rompio_papel:
    show papel roto noche
  else:
    show papel noche
    
  show red noche
  show humano sentado noche
  show caja noche at Position(xpos=1580, ypos=680)
  show red noche behind flores
  show habitacion base noche with dissolve

  # Aparece reja ventana
  $ renpy.pause(2) 
  show red noche

  $ renpy.pause(2) 

  # Aparece habitacion gris
  show final malobis with dissolve
  play sound ["meow_begging.mp3"]
  g "Los días siguen siendo iguales.. Humano sentado en su escritorio, la comida sin sabor."
  g "Pero ahora la ventana tiene rejas y yo observo, desde mi pequeña jaula."
  g "Al pájaro, nunca más lo volví a ver. Y cuando intento recordar los ojos de Humano, sólo puedo pensar en una luz brillante y dolorosa, como la luz de la caja."
  jump final

# Opcion caja
label caja:
  show gato flip:
    xpos 1520
    ypos 490
    zoom 0.2

  show gato parado flip:
    xpos 700
    ypos 450
    zoom 0.2
  show Patricia onlayer top
  g "El pájaro puede esperar, pero ¡esa caja!"
  show gato parado flip:
    xpos 1050
    ypos 590
    zoom 0.2
  g "Es irresistible..."

  show gato parado flip:
    xpos 1400
    ypos 445
    zoom 0.2
  show Patricia contenta onlayer top
  g "Me froto contra ella, una y otra vez, aprovechando su filosas superficies."
  
  # Patricia se mete en la caja
  hide gato
  show caja gato tarde at Position(xpos=1581, ypos=690)
  g "Ahora ya me cansé de rascarme y me meto adentro."

  # Humano la mira
  show humano girado tarde
  show Patricia onlayer top
  g "Desde esta oscuridad de cartón... el mundo da menos miedo."
  
  # Humano se levanta y la mira
  show humano de pie at Position(xpos=1000)
  g "De repente, siento un calor conocido."
  show Patricia pregunta onlayer top
  g "Una voz me abraza, mientras me sostiene la ternura de una caricia que creí que nunca más iba a volver a sentir..."
  show Patricia contenta onlayer top
  g "¡Son sus manos! Firmes, cálidas y seguras."
  show Patricia onlayer top
  g "Mientras jugaba con las cajas, Humano me había estado observando..." 
  g "...se había levantado de la silla y alejado de su caja de luz..  ya sin luz."

  show Humano neutro onlayer top
  h "Creo que ya pasó demasiado tiempo, ¿no Pat?"

  show Patricia onlayer top
  g "Sonreía por primera vez en mucho tiempo.. sonreía y lloraba.." 
  show Patricia pregunta onlayer top
  g "¡qué Humano tan extraño! Pero no lo cambiaría por ningún pájaro, ninguna caja de cartón o de luz."
  show Patricia contenta onlayer top
  g "Era mi Humano y hoy al fin había vuelto."

  show Patricia pregunta onlayer top
  show Humano contento onlayer top
  h "Es hora de salir afuera Pat, ¿vamos a la plaza?"
  
  # SFX puerta, pasos, pajaritos
  hide Humano onlayer top
  hide Patricia onlayer top
  hide humano sentado tarde with dissolve
  hide caja gato tarde with dissolve
  play sound ["door.mp3", "footsteps.mp3"]
  
  # Aparece habitacion final bueno
  show final bueno with dissolve
  
  $ renpy.pause(4) 
  play sound ["Purr_short.mp3"] fadeout 1
  g "Ppppprprrrrrr Prrrprprrrrrrr, yo ronroneo." 

  play sound ["outside.mp3"] fadein 3
  
  g "Mientras tanto, la brisa del verano atraviesa mis bigotes."
  jump final

label final:
  hide caja_gato
  if aciertos >= 2:
    jump final_bueno
  else:
    jump final_malo