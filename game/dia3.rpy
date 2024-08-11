label dia3:
  show text "DIA 3"
  pause

  scene habitacion base dia with dissolve

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

  g "Los días siguen siendo iguales.. Humano sentado en su escritorio, la comida no tiene sabor."
  g "Pero ahora la ventana tiene rejas y yo observo, desde mi pequeña jaula."
  g "Al pájaro, nunca más lo volví a ver. Y cuando intento recordar los ojos de Humano, sólo puedo pensar en una luz brillante y dolorosa, como la luz de la caja."
  jump final

label caja:
  g "El pájaro puede esperar, pero ¡esas cajas! Son irresistibles..."

  g "Me froto contra ellas, una y otra vez, aprovechando sus filosas superficies."
  g "Ahora ya me cansé rascarme y me meto adentro de ellas."
  g "Desde esta oscuridad de cartón... el mundo da menos miedo."

  g "De repente, siento un calor conocido."
  g "Una voz me abraza, mientras me sostiene la ternura de una caricia que creí que nunca más iba a volver a sentir..."
  g "¡Son sus manos! Firmes, cálidas y seguras."
  g "Mientras jugaba con las cajas, Humano me estaba observando.."
  g "Se había levantado de la silla y se había alejado de su caja de luz.. que ya no tenía ninguna luz."

  h "Creo que ya pasó demasiado tiempo, ¿no Pat?"

  g "Sonreía por primera vez en mucho tiempo.. sonreía y lloraba.." 
  g "¡qué Humano tan extraño! Pero no lo cambiaría por ningún pájaro, ninguna caja de cartón o de luz."
  g "Era mi Humano y hoy al fin había vuelto."

  h "Es hora de salir afuera Pat, ¿vamos a la plaza?"

  play sound ["Purr.mp3"]
  g "Ppppprprrrrrr Prrrprprrrrrrr, yo ronroneo. Mientras tanto, la brisa del verano atraviesa mis bigotes."
  jump final

label final:
  scene black with dissolve
  show text "FIN"
  pause

  "Gracias por jugar."
  return