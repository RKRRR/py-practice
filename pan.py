titulo = ("Hola, bienbvenido al Test sobre Panes")
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Que haces cuando ves un pan? \n"
                 "A- no me gusta el pan \n"
                  "B- me como la mitad \n"
                   "C- Me la reviento entera \n")
if opcion =="A":
    puntuacion += 0
elif opcion == "B":
    puntuacion +=  5
elif opcion == "C":
    puntuacion += 10

else:
    print("las opciones posibles son A, B y C")
    exit()


print(puntuacion)

opcion = input("pregunta 2: ¿Que tipo de pan de pan te gusta mas?\n"
               "A- Pan integral \n"
               "B- Baguete \n"
               "C- Chapata \n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion +=  5
elif opcion == "C":
    puntuacion += 10

else:
    print("las opciones posibles son A, B y C")

print(puntuacion)




opcion = input("Pregunta 3:¿Donde comprarias el pan?\n"
               "A- En una gasolinera\n"
               "B- En el supermercado\n"
               "C- En una panaderia\n")
if opcion =="A":
    puntuacion += 0
elif opcion == "B":
    puntuacion +=  5
elif opcion == "C":
    puntuacion += 10

else:
    print("las opciones posibles son A, B y C")

print(puntuacion)


if puntuacion >= 25:
    print("Resultado: ¡Eres un experto panadero!")

elif puntuacion >= 15:
    print("Te gusta el pan")

else:
    print("perico")