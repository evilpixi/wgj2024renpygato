label dia3:
  "dia 3"
  "texto intro del día 3"

  menu:
    "Ver pájaro en la ventana":
      $ aciertos += 1
      jump ventana

    "Meterse a la caja":
      $ aciertos += 0
      jump caja

label ventana:
  "te comes al pajaro en la ventana y el humano se rie."
  jump final

label caja:
  "te metes en la caja y el humano te saca de la habitación."
  jump final

label final:
  if aciertos >= 2:
    jump final_bueno
  else:
    jump final_malo