label dia3:
  scene black with dissolve
  show text "DIA 3"
  pause

  scene habitacion base dia 
  show humano sentado dia
  show caja dia at Position(xpos=1580, ypos=680)
  show pajaro dia
  show gato neutro:
    xpos 1520
    ypos 490
    zoom 0.2
    xzoom -1
  
  
  if comio_planta:
    show flores comidas dia
  else:
    show flores dia

  if rompio_papel:
    show papel roto dia
  else:
    show papel dia
    
  $ renpy.pause(2)
  

  g "Abro los ojos y bostezo. Otra vez todo es igual... no me sorprende."
  g "Humano sentado enfrente de la caja maldita, la comida sin gusto a nada y ese pájaro que todos los días se queda mirándome desde la ventana..."
  
  
  play sound ["hornero.mp3"]
  g "¿por qué me mira, qué quiere?"
  g "Ya fue, me cansé. Necesito que algo cambie, ¡lo necesito desesperadamente!"
  g "Si no hay nada que yo pueda hacer, tal vez.. tal vez el pájaro sea la respuesta."
  g "Me acerco despacio a la ventana, pero en el camino mi suave cola marroncita roza una de las cajas de cartón.."
  g "¡qué sensación increíble! Se siente casi.. casi como una caricia."
  
  # Patricia se mueve AUN DEFINIR A DONDE CON LA NARRATIVA
  g "¿Qué voy a hacer? ¿El pájaro realmente va a ayudarme a despertar a Humano?"
  g "¿Y si me rindiera? Humano no va a dejar su caja de luz..."
  g "¿Qué pasaría si eligiera quedarme entre las cajas... si eligiera la caricia del cartón?"
  
  # Cambio iluminación -> Tarde
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
  g "Saludo al pájaro - Meeeowwwlaa!- mientras el olor a verano despeina mis bigotes. Él se acerca y yo siento como si estuviera sosteniendo un secreto con el pico, sólo para mí."
  g "Cuando está a punto de abrir el pico, saludarme o tal vez soltar el secreto... escucho un grito de terror que me pone los pelos de punta...."

  # Humano la mira
  show humano girado tarde

  h "¡¿¡PATRICIA QUÉ HACES!?! ¡BAJATE DE AHÍ!"

  # Patricia se vuelve a la cama
  show gato neutro:
    xpos 700
    ypos 500
    zoom 0.2

  g "Humano al fin me mira... pero está asustado y nervioso."
  g "Quiero explicarle que estoy bien, quiero hablarle del secreto del pájaro, pero me agarra con las manos temblorosas y me aleja de la ventana."
  
  # Humano vuelve a mirar en frente
  hide pajaro tarde
  show humano sentado tarde 


  # Aparece reja ventana
  $ renpy.pause(2) 

  show red tarde behind flores


  # QUITE EL SONIDO DE LA REJA: play sound ["window.mp3"] -> acomodar narrativa?

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
  g "El pájaro puede esperar, pero ¡esa caja! Es irresistible..."
  g "Me froto contra ella, una y otra vez, aprovechando su filosas superficies."
  
  # Patricia se mete en la caja
  hide gato
  show caja gato tarde at Position(xpos=1581, ypos=690)
  g "Ahora ya me cansé de rascarme y me meto adentro."

  # Humano la mira
  show humano girado tarde
  g "Desde esta oscuridad de cartón... el mundo da menos miedo."
  
  # Humano se levanta y la mira
  show humano de pie at Position(xpos=1000)
  g "De repente, siento un calor conocido."
  g "Una voz me abraza, mientras me sostiene la ternura de una caricia que creí que nunca más iba a volver a sentir..."
  g "¡Son sus manos! Firmes, cálidas y seguras."
  g "Mientras jugaba con las cajas, Humano me había estado observando..." 
  g "...se había levantado de la silla y alejado de su caja de luz..  ya sin luz."

  h "Creo que ya pasó demasiado tiempo, ¿no Pat?"

  g "Sonreía por primera vez en mucho tiempo.. sonreía y lloraba.." 
  g "¡qué Humano tan extraño! Pero no lo cambiaría por ningún pájaro, ninguna caja de cartón o de luz."
  g "Era mi Humano y hoy al fin había vuelto."

  h "Es hora de salir afuera Pat, ¿vamos a la plaza?"
  
  # SFX puerta, pasos, pajaritos
  hide humano sentado tarde with dissolve
  hide caja gato tarde with dissolve
  play sound ["door.mp3", "footsteps.mp3"]
  
  # Aparece habitacion final bueno
  show final bueno with dissolve
  
  $ renpy.pause(4) 
  play sound ["Purr_short.mp3"]
  g "Ppppprprrrrrr Prrrprprrrrrrr, yo ronroneo." 

  
  play sound ["outside.mp3"]

  
  
  g "Mientras tanto, la brisa del verano atraviesa mis bigotes."
  jump final

label final:
  hide caja_gato
  if aciertos >= 2:
    jump final_bueno
  else:
    jump final_malo