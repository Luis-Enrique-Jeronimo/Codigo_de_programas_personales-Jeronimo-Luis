import Inicial  #Funcion que contiene las opciones de la calculadora.

def pregunta(): #Imprime el menú y pregunta si deseas realizar otra operación.
    
    Inicial.menu()
    
    letras = ('S','s','SI','si','Si') #Diccionario para verificación de las letras que introducira el usuario

    opc = str(input("-----------¿Desea realizar otra operación?-----------\n\t : "))
    
    if (opc in letras):
            Inicial.menu()
            pregunta()
    else:
        print("Adios.!!")

pregunta()
