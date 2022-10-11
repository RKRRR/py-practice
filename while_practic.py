from  random import randint
pikachu = 10
squirtle = 10


while pikachu > 0 and squirtle > 0:
    print("turno de pikachu")
    ataque_pikachu = randint(1,2)

    if ataque_pikachu == 1:
        #trueno
        print("pikachu ataca a squirtle con trueno")
        squirtle -= 3
    else:
        print("pikachu ataca con rafaga electrica")
        squirtle -= 5

    print("la vida de pikachu es: {}, la vida de squirtle es: {}".format(pikachu, squirtle))

    print("turno de squirtle")

    ataque = input("tu turno con que quieres atacar a pikachu? \n"
                   "1 - Pistola de agua \n"
                   "2 - Tsunami ")

    if ataque == 1:
        print("atacas con pistola de agua")
        pikachu -= 3
    elif ataque == 2:
        print("atacas con Tsunami")
        pikachu -= 5

    print("la vida de pikachu es: {}, la vida de squirtle es: {}".format(pikachu, squirtle))







