from psychopy.hardware import keyboard
from psychopy import visual, core, gui
import csv, os

"""
Este código es un ensayo. En este ensayo, aparecerá una L sobre uno de los cuadros, el participante decidirá si hubo una
L en el sentido correcto, la imagen aparecerá por 350 ms. Aparecerá una checkmark verde si acertó y un equis roja en caso
de que no haya acertado
"""
#=========
#Funciones
#=========

#Funcion utilizada para dibujar cajas
#Recibe una lista como parámetro con objetos imagenes que a cada uno le aplicará un draw()
def dibujaCajas(imagenes):
    for i in imagenes:
        i.draw()

#===============
#Final funciones
#===============

#Creamos una Ventana de Dialogo haciendo uso de gui.Dlg
ventanaDeDialogo = gui.Dlg(title="Ensayo de Tarea de Parpadeo Atencional")   #utilizaremos la variable ventanaDeDialogo, 
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
#Aquí empieza el ensayo
#======================
#Objeto teclado, el cual utilizaremos para leer la entrada por teclado del participante
kb = keyboard.Keyboard()

#Objeto ventana que mostrará la tarea de parpadeo atencional
ventana = visual.Window(size=(800,600), fullscr=False, color='black')

#Objeto mensaje que muestra las instrucciones del ensayo
instrucciones = visual.TextBox2(ventana, text="""Se mostrarán varias imagenes de la letra L, el objetivo es decir si se vió la imagen L con la orientación correcta, es decir, la del abecedario, presionaras la tecla G, en caso contrario, presiona la H. Presiona cualquier tecla para iniciar""", color='white')

#Dibuja las instrucciones en el buffer
instrucciones.draw()

#Muestra el buffer en la ventana, el buffer se vacía
ventana.flip()

#Esperamos la respuesta del participante
c = kb.waitKeys()

if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
    ventana.close() #Cierra la ventana en la que se hizo el ensayo
    core.quit()     #Cierra todo lo referente a psychopy

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
#imagenL1 = visual.ImageStim(ventana, image=directory + '/multimedia/n2.png', size=[0.2,0.2])

#Objeto imagen que presenta una letra L (revisar multimedia para ver imagen)
#imagenL2 = visual.ImageStim(ventana, image=directory + '/multimedia/n3.png', size=[0.2,0.2])

#Objeto imagen que presenta una letra L (revisar multimedia para ver imagen)
#Esta imagen es la L con la orientación correcta
#imagenL3 = visual.ImageStim(ventana, image=directory + '/multimedia/t1.png', size=[0.2,0.2])

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

#Llamamos la función dibujaCajas, que dibujas los cuadros en el buffer 
dibujaCajas(cajas)

#Le damos la posición del cuadro de arriba una imagen
imagenL0.pos = [0, 0.75]

#Dibujamos la imagen en el buffer, al estar en la misma posición que otra imagen, esta se sobrepone
imagenL0.draw()

#Pasamos el buffer a la ventana
ventana.flip()

#Esperamos 350 ms antes de borrar las imagenes
core.wait(.35)

#Dibujamos los cuadros en el buffer
dibujaCajas(cajas)

#Pasamos el buffer a la ventana, el buffer se vacía
#como dibujamos los cuadros en el buffer, aparecerán vacíos en pantalla
ventana.flip()

#Esperamos la respuesta del participante
c = kb.waitKeys(keyList=['escape','g','h'])

if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
    ventana.close() #Cierra la ventana en la que se hizo el ensayo
    core.quit()     #Cierra todo lo referente a psychopy
elif c[0].name == 'g':#Se presiono la tecla 'g'
    ok_data.append(False)  #En este ensayo en particular, al no tener la L en orientación correcta, es False
    ok_data.append('g')#Se agrega la tecla que el participante presionó
    imagenIncorrecto.draw() #En este caso particular, al no estar la L, y presionar la g de que si estaba, dibujamos en el buffer la equis
else: #Se presiono 'h'
    ok_data.append(False)  #En este ensayo en particular, al no tener la L en orientación correcta, es False
    ok_data.append('h')#Se agrega la tecla que el participante presionó
    imagenCorrecto.draw() #En este caso particular, al no estar la L y presionar la h de que no estaba la L, dibujamos el checkmark 

#Pasa lo que tenemos en el buffer a la ventana, se vacía el buffer
ventana.flip()

#Esperamos 2 segundos antes de borrar la ventana
core.wait(2)

#Limpiamos la ventana
ventana.flip()

#======================
#Aquí termina el ensayo
#======================

#Guardamos información relevante de nuestro experimento en un archivo csv
#La siguiente línea solo nos dice como se va a llamar el archivo que gaurdará la información
#la 'w' que vamos a escribir en este
#encoding es para el tipo de caracteres que guardaremos
#newline solo nos dice como separar los renglones (no será necesario por ahora)
with open('respuesta_ensayo.csv','w',encoding='UTF8',newline='') as f:
    #writer nos ayudará a escribir en el archivo csv
    writer = csv.writer(f)

    #el método writerow() escribirá en un renglón, en este caso, en el primer renglón del archivo csv
    #con los elementos de la lista en una columna diferente en el mismo renglón
    writer.writerow(['nombre','edad','seEncuentraL','teclaPresionada'])

    #escribimos en el siguiente renglón toda la información pertinente a las columnas en el sigueinte renglón
    #utilizando la lista ok_data
    writer.writerow(ok_data)


#Final del programa
ventana.close() #Cierra la ventana en la que se hizo el ensayo
core.quit()     #Cierra todo lo referente a psychopy