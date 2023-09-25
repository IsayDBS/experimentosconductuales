from psychopy.hardware import keyboard
from psychopy import visual, core, gui
import csv, os, random

"""
Este código es un ensayo. En este ensayo, aparecerá una L sobre uno de los cuadros, el participante decidirá si hubo una
L en el sentido correcto, la imagen aparecerá por 350 ms.
"""
#=========
#Funciones
#=========

def dibujaCajas(imagenes):
    for i in imagenes:
        i.draw()

#Funcion utilizada para convertir una lista de objetos imagenes a lista de strings que describen dichas imagenes
#es decir, tenemos [imagenL0, imagenL1, imagenL2, imagenL3], queremos ["L incorrecta","L incorrecta", "L incorrecta","L correcta"]
#ya que imagenL3 es la que tiene la imagen con la L en orientación correcta
def listaImagenes(lista, iteraciones):
    #Estructura de datos diccionario donde la llave será un objeto imagen, y el valor será si la L tiene orientación correcta
    #o no
    diccionarioAux = {imagenL0 : "L incorrecta", imagenL1: "L incorrecta", imagenL2: "L incorrecta", imagenL3: "L correcta"}
    #Lista que utilizaremos para devolver la lista si las L's son correctas
    listaAux = []
    #Iteramos sobre las listas
    for i in range(iteraciones):
        #Revisamos el valor de i que es un objeto imagen en el diccionario, y agregamos su valor a la lista
        listaAux.append(diccionarioAux[lista[i]])
    #Regresamos la lista
    return listaAux

#===============
#Final funciones
#===============

#Creamos una Ventana de Dialogo haciendo uso de gui.Dlg
ventanaDeDialogo = gui.Dlg(title="Bloque de Tarea de Parpadeo Atencional")   #utilizaremos la variable ventanaDeDialogo, 
#haciendo uso de gui.Dlg, este, tiene un parámetro title que es el nombre que aparece en el tope de la ventana

ventanaDeDialogo.addText('Información del participante')        #Agrega texto en un renglón de la ventana, en este caso
#inmediatamente abajo del título

ventanaDeDialogo.addField('Nombre:')          #Agrega el texto 'Nombre', después del cual, tiene un cuadro donde puedes agregar
#texto, todo esto estará abajo del texto de información del participante.

ventanaDeDialogo.addField('Edad:')            #Agrega el texto 'Edad', después del cual, tiene un cuadro donde puedes agregar
#texto, pero en este caso, se espera un número, todo esto estará abajo del texto 'Nombre'

ok_data = ventanaDeDialogo.show() #Muestra dos opciones, OK o Cancel

if ventanaDeDialogo.OK:  #Pregunta si el participante le dio a OK
    print(ok_data)       #Le dio OK, da una lista, que guarda los valores de addField(), en este caso
                         #la lista será [nombre del participante, edad del participante]
else:                    #Se dió a Cancel
    print('Usuario canceló')#Le dió a Cancel, imprime en terminal 'Usuario canceló' y cancelamos el ensayo
    #Final del programa
    core.quit()     #Cierra todo lo referente a psychopy

#======================
#Aquí empieza el bloque
#======================
#Objeto teclado, el cual utilizaremos para leer la entrada por teclado del participante
kb = keyboard.Keyboard()

#Objeto ventana que mostrará la tarea de parpadeo atencional
ventana = visual.Window(fullscr=True, color='black')

#Objeto mensaje que muestra las instrucciones del ensayo
instrucciones = visual.TextBox2(ventana, text="""Se mostrarán varias imagenes de la letra L, el objetivo es decir si se vió la imagen L con la orientación correcta, es decir, la del abecedario, presionaras la tecla G, en caso contrario, presiona la H. Presiona cualquier tecla para iniciar""", color='white')

#Dibuja las instrucciones en el buffer
instrucciones.draw()

#Muestra el buffer en la ventana, el buffer se vacía
ventana.flip()

#Esperamos la respuesta del participante
c = kb.waitKeys()

#Se limpia la ventana ya que no había nada en el buffer
ventana.flip()

#Nos da la dirección en la que se encuentra este archivo en la computadora
directory = os.getcwd()

#=================================
#Imagenes usadas durante el ensayo
#=================================

#Objeto imagen que presenta una letra L (revisar multimedia para ver imagen)
imagenL0 = visual.ImageStim(ventana, image=directory + '/multimedia/n1.png', size=[0.2,0.2])

#Objeto imagen que presenta una letra L (revisar multimedia para ver imagen)
imagenL1 = visual.ImageStim(ventana, image=directory + '/multimedia/n2.png', size=[0.2,0.2])

#Objeto imagen que presenta una letra L (revisar multimedia para ver imagen)
imagenL2 = visual.ImageStim(ventana, image=directory + '/multimedia/n3.png', size=[0.2,0.2])

#Objeto imagen que presenta una letra L (revisar multimedia para ver imagen)
#Esta imagen es la L con la orientación correcta
imagenL3 = visual.ImageStim(ventana, image=directory + '/multimedia/t1.png', size=[0.2,0.2])

#Objeto imagen que es un cuadrado con contorno blanco (revisar multimedia para ver imagen)
#Con posicion en la parte de la derecha de la ventana
imagenCaja0 = visual.ImageStim(ventana, image=directory + '/multimedia/box.png', size =[0.4,0.4], pos=[0.75, 0])

#Objeto imagen que es un cuadrado con contorno blanco (revisar multimedia para ver imagen)
#Con posicion en la parte de la izquierda de la ventana
imagenCaja1 = visual.ImageStim(ventana, image=directory + '/multimedia/box.png', size =[0.4,0.4], pos=[-0.75, 0])

#Objeto imagen que es un cuadrado con contorno blanco (revisar multimedia para ver imagen)
#Con posicion en la parte de abajo de la ventana
imagenCaja2 = visual.ImageStim(ventana, image=directory + '/multimedia/box.png', size =[0.4,0.4], pos=[0, -0.75])

#Objeto imagen que es un cuadrado con contorno blanco (revisar multimedia para ver imagen)
#Con posicion en la parte de arriba de la ventana
imagenCaja3 = visual.ImageStim(ventana, image=directory + '/multimedia/box.png', size =[0.4,0.4], pos=[0, 0.75])

#Objeto imagen que es un checkmark verde(revisar multimedia para ver imagen)
imagenCorrecto = visual.ImageStim(ventana, image=directory + '/multimedia/correct.png', size=[0.2,0.2])

#Objeto imagen que es un equis roja(revisar multimedia para ver imagen)
imagenIncorrecto = visual.ImageStim(ventana, image=directory + '/multimedia/error.png', size=[0.2,0.2])

#===================================
#Terminan la declaración de imagenes
#=================================== 

#Lista con todos los cuadrados
cajas = [imagenCaja0, imagenCaja1, imagenCaja2, imagenCaja3]

#Lista con las letras L's 
letras = [imagenL0, imagenL1, imagenL2, imagenL3]

#Posiciones usadas para presentar las L's
posiciones = [[-0.75,0],[0.75,0],[0,-0.75],[0,0.75]]

#Variable que nos dice si la letra L apareció en la ventana
seEncuentra = False

#Variable que nos dice que tecla se presiono
teclaPresionada = False

#Lista que guarda las respuestas dada por el participante
respuestas = []

#!!!!!!!!!!!!!!!!!!!
#!Inicio de código !
#!delicado, manejar!
#!con precaución   !
#!!!!!!!!!!!!!!!!!!!

#Repetimos el ensayo 5 veces
for i in range(5):
    
    dibujaCajas(cajas)

    #Pasamos el buffer a la ventana, se vacía el buffer
    ventana.flip()

    #letrasEnCajas es una lista, que dada la lista letras, devolverá una lista de 4 eleemntos con
    #cualquier elemento dentro de letras, hasta se puede repetir
    #Es decir, letras tiene las imagenes de las L's
    #letrasEnCajas puede tener imagenL0 como todos sus elementos, así como es posible
    #que sea imagenL1 repetido dos veces, despupes imagenL0 e imagenL3
    #letrasEnCajas = [imagenL1, imagenL1, imagenL0, imagenL3]
    letrasEnCajas = random.choices(letras, k=4)

    #Barajea la lista posiciones
    random.shuffle(posiciones)

    #Numero de L's que van a aparecer, siendo 
    # 0 va a aparecer 1, 1 van a aparecer 2, 2 van a aparecer 3 y 3 van a aparecer los 4
    apariciones = random.randint(0,3)

    
    dibujaCajas(cajas) 

    #Como no sabemos que L's hay en letrasEnCajas, iteramos sobre la lista segun la cantidad 
    # de la variable apariciones + 1.
    for j in range(apariciones + 1):
        #A cada imagen en letrasEnCajas, le damos una posición, es decir, van a ir dentro de un
        #cuadrado
        letrasEnCajas[j].pos = posiciones[j]
        #Revisamos si dicha imagen es la L con orientación correcta
        if letrasEnCajas[j] == imagenL3:
            #Si es así, la variable seEncuentra se vuelve True
            seEncuentra = True
        #Terminamos dibujando la imagen en el buffer
        letrasEnCajas[j].draw()

    #Pasamos el buffer a la ventana, el buffer se vacía
    ventana.flip()

    #Esperamos 350 ms con los cuadros llenos
    core.wait(.35)

    
    dibujaCajas(cajas)

    #Pasamos el buffer a la ventana, el buffer se vacía
    ventana.flip()

    #Esperamos la tecla presionada por el participante
    c = kb.waitKeys(keyList=['g','h'])

    
    #El participante presionó la tecla g y la L con orientación correcta esta
    if c[0].name == 'g' and seEncuentra == True:
        #Al estar la L y presionando la tecla correcta, se dibuja el checkmark
        imagenCorrecto.draw()
        #Guardamos la tecla que el participante presionó
        teclaPresionada = 'g'
        #Pasamos el buffer a la ventana
        ventana.flip()
        #Esperamos 1 segundo
        core.wait(1)
    #El participante presionó la tecla g y la L con orientación correcta no esta
    elif c[0].name == 'g' and seEncuentra == False:
        #Al no estar la L y presionando la tecla incorrecta, se dibuja la equis
        imagenIncorrecto.draw()
        #Guardamos la tecla que el participante presionó
        teclaPresionada = 'g'
        #Pasamos el buffer a la ventana
        ventana.flip()
        #Esperamos 1 segundo
        core.wait(1)
    #El participante presionó la tecla h y la L con orientación correcta no esta
    elif c[0].name == 'h' and seEncuentra == False:
        #Al no estar la L y presionando la tecla correcta, se dibuja el checkmark
        imagenCorrecto.draw()
        #Guardamos la tecla que el participante presionó
        teclaPresionada = 'h'
        #Pasamos el buffer a la ventana
        ventana.flip()
        #Esperamos 1 segundo
        core.wait(1)
    #El participante presionó la tecla h y la L con orientación correcta esta
    elif c[0].name == 'h' and seEncuentra == True:
        #Aqui va codigo
        print("Aqui va tu codigo ;)")
    #Agregamos las respuestas del participante al a la lista respuestas
    respuestas.append(['','',listaImagenes(letrasEnCajas,apariciones+1),seEncuentra, teclaPresionada])
    #Volvemos la variale seEncuentra a False para usarla de nuevo el siguiente ensayo
    seEncuentra = False

#!!!!!!!!!!!!!!!!!!!
#!Final de código  !
#!delicado, manejar!
#!con precaución   !
#!!!!!!!!!!!!!!!!!!!

#======================
#Aquí termina el bloque
#======================

#Guardamos información relevante de nuestro experimento en un archivo csv
#La siguiente línea solo nos dice como se va a llamar el archivo que gaurdará la información
#la 'w' que vamos a escribir en este
#encoding es para el tipo de caracteres que guardaremos
#newline solo nos dice como separar los renglones (no será necesario por ahora)
with open('respuesta_bloque.csv','w',encoding='UTF8',newline='') as f:
    #writer nos ayudará a escribir en el archivo csv
    writer = csv.writer(f)

    #el método writerow() escribirá en un renglón, en este caso, en el primer renglón del archivo csv
    #con los elementos de la lista en una columna diferente en el mismo renglón
    writer.writerow(['nombre','edad','listaDeLs','seEncuentraL','teclaPresionada'])

    #escribimos en el siguiente renglón toda la información pertinente al nombre y edad
    #utilizando la lista ok_data
    writer.writerow(ok_data)

    #escribimos en el siguiente renglón toda la información pertinente a las columnas en el sigueinte renglón
    #utilizando la lista ok_data
    writer.writerows(respuestas)


#Final del programa
ventana.close() #Cierra la ventana en la que se hizo el ensayo
core.quit()     #Cierra todo lo referente a psychopy