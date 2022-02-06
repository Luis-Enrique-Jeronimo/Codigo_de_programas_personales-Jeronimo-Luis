def MayMen():
    print("Introducira dos números para la comparación: \n")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))

    if num1 > num2:
        print("{} es mayor que {}".format(num1,num2))
    else:
        print("{} es mayor que {}".format(num2,num1))

MayMen()