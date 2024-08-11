label dia3:
  "DIA 3"

  scene habitacion base dia 
  show humano sentado dia
  show caja dia

  $ renpy.pause(2)
  show pajaro dia with dissolve
  $ renpy.pause(2)
  
  # agregar sonido hornero: play sound ["pajaro.mp3"] 
  play sound ["stomach.mp3"] 


  g "Abro los ojos y bostezo. Otra vez todo es igual... no me sorprende."
  g "Humano sentado enfrente de la caja maldita, la comida sin gusto a nada y ese pájaro que todos los días se queda mirándome desde la ventana..."
  g "¿por qué me mira, qué quiere?"
  g "Ya fue, me cansé. Necesito que algo cambie, ¡lo necesito desesperadamente!"
  g "Si no hay nada que yo pueda hacer, tal vez.. tal vez el pájaro sea la respuesta."
  g "Me acerco despacio a la ventana, pero en el camino mi suave cola marroncita roza una de las cajas de cartón.."
  g "¡qué sensación increíble! Se siente casi.. casi como una caricia."
  g "¿Qué voy a hacer? ¿El pájaro realmente va a ayudarme a despertar a Humano?"
  g "¿Y si me rindiera? Humano no va a dejar su caja de luz..."
  g "¿Qué pasaría si eligiera quedarme entre las cajas... si eligiera la caricia del cartón?"
  
  # Cambio iluminación -> Tarde
  show habitacion base tarde with dissolve
  hide humano sentado dia
  show humano sentado tarde
  hide pajaro dia
  show pajaro tarde
  menu:
    "Preguntarle la posta al pájaro":
      $ aciertos += 0
      jump ventana

    "Entregarse a la caricia del cartón":
      $ aciertos += 1
      jump caja

label ventana:
  g "Decido confiar en el pájaro y sigo avanzando hacia la ventana, esquivando las cajas.."
  g "Mientras trepo por el acolchado, siento el calor del sol acariciándome el lomo. Rayos de luz atraviesan la ventana y me envuelven en una calidez antigua, lejana y permanente."
  g "Desde la ventana veo la plaza: árboles frondosos y fuentes de agua, una nena con trenzas sostiene un barrilete naranja."
  
  play sound ["meow_far.mp3"]
  g "Saludo al pájaro - Meeeowwwlaa!- mientras el olor a verano despeina mis bigotes. Él se acerca y yo siento como si estuviera sosteniendo un secreto con el pico, sólo para mí."
  g "Cuando está a punto de abrir el pico, saludarme o tal vez soltar el secreto... escucho un grito de terror que me pone los pelos de punta...."

  h "¡¿¡PATRICIA QUÉ HACES!?! ¡BAJATE DE AHÍ!"

  g "Humano al fin me mira... pero está asustado y nervioso."
  g "Quiero explicarle que estoy bien, quiero hablarle del secreto del pájaro, pero me agarra con las manos temblorosas y cierra la ventana con un golpe seco."
  
  play sound ["window.mp3"]

  # Aparece reja ventana

  # Cambio iluminación -> Noche
  show habitacion base noche with dissolve
  hide humano sentado tarde
  show humano sentado noche
  hide caja dia
  show caja noche
  hide pajaro tarde
  play sound ["meow_begging.mp3"]
  g "Los días siguen siendo iguales.. Humano sentado en su escritorio, la comida sin sabor."
  g "Pero ahora la ventana tiene rejas y yo observo, desde mi pequeña jaula."
  g "Al pájaro, nunca más lo volví a ver. Y cuando intento recordar los ojos de Humano, sólo puedo pensar en una luz brillante y dolorosa, como la luz de la caja."
  jump final

label caja:
  g "El pájaro puede esperar, pero ¡esas cajas! Son irresistibles..."

  g "Me froto contra ellas, una y otra vez, aprovechando sus filosas superficies."
  g "Ahora ya me cansé de rascarme y me meto adentro."
  
  show caja_gato
  g "Desde esta oscuridad de cartón... el mundo da menos miedo."

  hide habitacion humano
  show fondo_base 
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

  hide humano sentado tarde with dissolve
  hide Patricia with dissolve

  # Agregar un "blur" de la escena

  play sound ["Purr.mp3"]

  # SFX puerta
  # SFX pasos
  # SFX pájaros y árboles
  g "Ppppprprrrrrr Prrrprprrrrrrr, yo ronroneo. Mientras tanto, la brisa del verano atraviesa mis bigotes."
  jump final

label final:
  hide caja_gato
  if aciertos >= 2:
    jump final_bueno
  else:
    jump final_malo