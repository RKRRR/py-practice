print ("Conversor de dinero")
dinero = (input("introduzca a que quiere convertir su dinero\n"
                "A - dolar a ars\n"
                "B - euro a dolar \n"))

if dinero == "A":
    print("conversor de dolar a ars\n")
    d = float(input("introduzca la cantida que quiere  convertir de dolares  a euros: "))
    print((d)*float(0.0067) )
