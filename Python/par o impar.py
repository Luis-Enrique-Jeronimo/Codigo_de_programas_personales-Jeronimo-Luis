#Par o impar con paradigma de programación funcional.
#Crear la funcion donde estará todo el código de impresion en pantalla, guardar los números en una lista.


def fun_list():

    print("Ingresa 3 números y la maquina te dira si es par o impar.")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    num3 = int(input("Tercer número: "))

    list = (num1,num2,num3)

    for i in list:
        if i % 2 == 0:
            print("{} Es número Par".format(i))
        else:
            print("{} Es número Impar".format(i))


fun_list()
