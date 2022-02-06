import Inicial  #Funcion que contiene las opciones de la calculadora.
import sys

letras = ('S','s','SI','si','Si') #Diccionario para verificación de las letras que introducira el usuario


Inicial.menu()
op = str(input("-----------¿Desea realizar otra operación?-----------\n :_"))

#Si lo introducido en la variable es igual al contenido de la lista entonces se vuelve a iniciar el programa.
for op in letras:
    if (op == letras):
        Inicial.menu()

    elif(op != letras):
        sys.exit()

