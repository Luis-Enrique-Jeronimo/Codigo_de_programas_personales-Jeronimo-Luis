import operaciones

def menu(): #Se muestra el menú y se solicita el valor de las variables y son los parámetros de cada función.
    op = int(input("Selecciona la opción que deseas. \n1.Suma \n2.Resta \n3.Multiplicación \n4.División\n Ingresa el número:  "))
    

    if(op==1):
        n1 = float(input("Ingresa el primer número: "))
        n2 = float(input("Ingresa el segúndo número: "))
        operaciones.suma(n1,n2)
    elif(op==2):
        n1 = float(input("Ingresa el primer número: "))
        n2 = float(input("Ingresa el segúndo número: "))
        operaciones.resta(n1,n2)
    elif(op==3):
        n1 = float(input("Ingresa el primer número: "))
        n2 = float(input("Ingresa el segúndo número: "))
        operaciones.multi(n1,n2)
    elif(op==4):
        n1 = float(input("Ingresa el primer número: "))
        n2 = float(input("Ingresa el segúndo número: "))
        operaciones.div(n1,n2)
    else:
        print("\t\tERROR.!! INGRESE UN VALOR DENTRO DEL RANGO.!!")
        menu()
