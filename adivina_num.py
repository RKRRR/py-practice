import random

num_ganador = random.randint(1, 5)
adivina = int(input ("introduce un num del 1 al 5: "))

if adivina == num_ganador:
    print("felicidades adivinaste el numero!")
else: print("lo siento no adivinaste el numero")