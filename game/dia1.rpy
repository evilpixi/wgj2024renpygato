label dia1:
  "dia 1"
  "texto intro del día 1"

  # aqui habría que poner la intro de las decisiones

  menu:
    "Comer plantas":
      $ aciertos += 1
      jump plantas

    "Opción Buena":
      $ aciertos += 0
      jump papel


label plantas:
  "el humano te da unos mimos y te saca de la habitación."
  jump finDia1


label papel:
  "empujas la taza y el humano te mira."
  jump finDia1


# aqui se juntan ambas opciones y se va al día 2
label finDia1:
  "fin del dia 1"
  jump dia2