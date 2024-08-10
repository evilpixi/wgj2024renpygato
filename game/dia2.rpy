label dia2:
  "dia 2"
  "texto intro del día 2"

  menu:
    "Hacer ofrenda":
      $ aciertos += 1
      jump ofrenda

    "Sentarse en teclado":
      $ aciertos += 0
      jump teclado

label ofrenda:
  "le das una ofrenda al humano y te saca de la habitación."
  jump finDia2

label teclado:
  "Te subes al teclado y el humano te mira raro y se va. Eso fue muy hetero"
  jump finDia2

label finDia2:
  "fin del dia 2"
  jump dia3