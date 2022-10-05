print("Test para saber si tienes depresion \n")

puntuacion = 0

asks = input("elige la respuesta que mas te represente \n"
             "A - me encanta mi vida\n"
             "B - me siento conforme con mi vida\n"
             "C - odio mi vida\n"
             "RESPUESTA: ")

if asks == "A":
    puntuacion += 5
elif asks == "B":
    puntuacion += 10
elif asks == "C":
    puntuacion += 15
else:
    print("selecciona una respuesta valida A B o C")
    exit()


print("\n siguiente ronda de preguntas")


asks = input("elige la respuesta que mas te represente \n"
             "A - me siento con mucha energia todo el dia\n"
             "B - aveces me siento un poco cansado\n"
             "C - no puedo ni levantarme de la cama\n"
             "RESPUESTA: ")

if asks == "A":
    puntuacion += 5
elif asks == "B":
    puntuacion += 10
elif asks == "C":
    puntuacion += 15
else:
    print("selecciona una respuesta valida A B o C")



print("\n ultima ronda de preguntas")


asks = input("elige la respuesta que mas te represente \n"
             "A - tengo muchos amigos y familiares que me quieren\n"
             "B - aveces me siento un poco solo, aunque tengo gente que me quiere\n"
             "C - no le importo a nadie, estoy muy sol@\n"
             "RESPUESTA: ")


if asks == "A":
    puntuacion += 5
elif asks == "B":
    puntuacion += 10
elif asks == "C":
    puntuacion += 15
else:
    print("selecciona una respuesta valida G H o J")



if puntuacion <= 15:
    print("felicidades no tienes depresion, estas en un muy buen momento de tu vida")
elif puntuacion  <= 30:
    print("estas un poco triste, tienes que mejorar algunos aspectos de tu vida")
elif puntuacion <=45:
    print("parece que te encuentras bastante mal, te recomiendo que vayas a un psicologo")

























