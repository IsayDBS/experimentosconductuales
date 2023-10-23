from psychopy.hardware import keyboard
from psychopy import visual, core, gui
import csv, os, random

"""
Este código es un ensayo, se muestra una imagen en la pantalla, el punto del ensayo es que el usuario decida si la imagen
estuvo un tiempo corto (400ms) o largo (1600ms). En este ensayo, se presentará el estímulo, seguido de un texto informando si el
el estímulo fue largo o corto.
Se guardará la información referente al nombre del participante, la edad del participante, la tecla que debería presionar 
el participante, la tecla que presiono, si acerto o no y el tiempo que le tomo presionarla
"""

#Creamos una Ventana de Dialogo haciendo uso de gui.Dlg
ventanaDeDialogo = gui.Dlg(title="Ensayo de Tarea de Estimcación Temporal")   #utilizaremos la variable ventanaDeDialogo, 
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
#Ventana
ventana = visual.Window([800,800], monitor="informacion", fullscr=False, color="white")#Se crea una ventana donde se presentará el ensayo
#El primer parámetro es una lista, que representa el tamaño de la ventana, es un numero entero, en este, el primero es el ancho, el segundo es lo alto
#el parámetro monitor, es para darle un identificador a nuestra ventana,  con un nombre representativo basta
#fullscr es un parámetro que nos indica si queremos que la ventana abarque toda nuestra pantalla, como le ponemos False, no ocupará toda la pantalla

#Objeto teclado que nos sirve para recibir las teclas presionada por el participante
kb = keyboard.Keyboard()

#Nos da la dirección en la que se encuentra este archivo en la computadora
directory = os.getcwd()

#Mensaje a imprimir en pantalla
instrucciones = visual.TextBox2(ventana, text="""A continuación se presentará una imagen seguida en alguna parte de la pantalla, después del cual, aparecerá un texto mencionando si fue presentado una larga duración o corta. Para cada opción, presion S para corta duración y L para larga duración. Presione la barra espaciadora para comenzar.""", color='black')

#Mnesaje a imprimir en pantalla
mensaje = visual.TextBox2(ventana, text='El estimulo anterior fue de duración corta presiona S', color= 'black')

#Muestra una cruz negra en el centro de la pantalla
fixation = visual.TextBox2(ventana, text='+', color='black', alignment='center')

#Creamos un objeto ImageStim, que recibe dos parámetros, el primero una ventana, el segundo, que es image, que es
#la dirección a la imagen, que esta dentro de la carpeta img, el parámetro size en una lista, nos dice el ancho y el largo
imagenAzul = visual.ImageStim(ventana, image=directory + '/img/blue.png',size=[0.5,0.5])

#Dibujamos en el buffer las instrucciones
instrucciones.draw()

#Pasamos lo que hayamos hecho en el buffer a la ventana, el buffer se vacía
ventana.flip()

#Esperamos la respuesta por teclado del participante, en este caso, recibe un parámetro
#llamado keyList, que es una lista que nos dice que teclas va a tomar en cuenta, ignorando los demás
#En este caso, la barra espaciadora y escape son las únicas teclas que tomará en cuenta
c = kb.waitKeys(keyList=['space','escape'])

if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
    ventana.close() #Cierra la ventana en la que se hizo el ensayo
    core.quit()     #Cierra todo lo referente a psychopy

#Limpiamos la ventana, ya que no había nada en el buffer
ventana.flip()

#Dibujamos la cruz en el buffer
fixation.draw()

#Pasamos lo del buffer sobre la ventana, se vacía el buffer
ventana.flip()

#Esperamos 1 segundo, el programa no permite ninguna acción
core.wait(1)

#El atributo pos de las imagenes es una lista de dos elementos, el primero nos da una dirección sobre x
#el segundo sobre y
#Imagina un plano cartesiano sobre tu pantalla, donde los extremos valen 1 o -1.

#                 [0,1]
#                   |
#                   |       [0.75,0.75] Aprox
#                   |
#[-1,0]------------------------------[1,0]
#                   |
#                   |
#                   |
#                 [0,-1]
imagenAzul.pos = [0.75, 0.75]

#Dibujamos la imagen sobre el buffer
imagenAzul.draw()

#Pasamos el buffer a la ventana, se vacía el buffer
ventana.flip()

#El programa espera 400 ms 
core.wait(.4)

#Dibujamos el mensaje sobre el buffer
mensaje.draw()

#Pasamos el buffer a la ventana, se vacía el buffer
ventana.flip()

#Reiniciamos el reloj interno del teclado
kb.clock.reset()

#Esperamos el valor introducido por el participante, solo permitiendo escape y 's'
c = kb.waitKeys(keyList=['s','escape'])

if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
    ventana.close() #Cierra la ventana en la que se hizo el ensayo
    core.quit()     #Cierra todo lo referente a psychopy
elif c[0].name == 's': #Si la tecla es s
    ok_data.append('s')#Agregamos a la lista ok_data la letra s, que es la tecla que debió presionar
    ok_data.append('s')#Agregamos a la lista ok_data la letra s, que es la teca presionada
    ok_data.append(c[0].rt)#Se agrega el valor de tiempo que le tomo presionar dicha tecla
 

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
    writer.writerow(['nombre','edad','teclaAPresionar','teclaPresionada','tiempo'])

    #escribimos en el siguiente renglón toda la información pertinente a las columnas en el sigueinte renglón
    #utilizando la lista ok_data
    writer.writerow(ok_data)


#Final del programa
ventana.close() #Cierra la ventana en la que se hizo el ensayo
core.quit()     #Cierra todo lo referente a psychopy