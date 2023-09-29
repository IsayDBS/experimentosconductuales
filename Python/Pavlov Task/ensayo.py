from psychopy import core, visual, gui, sound #Importamos core, visual, sound y gui que utilizaremos durante el ensayo
from psychopy.hardware import keyboard  #Importamos keyboard, el cual lo utilizamos para poder usar nuestro teclado en el ensayo
import os, csv  #Utilizado para escribir un archivo csv dentro del cual guadará la información del ensayo

"""
Este código es un ensayo, se presentará un sonido de una campana, seguido por un estímulo visual, se debe de presionar la tecla
mencionada en las instrucciones lo más rápido posible, antes de 3 segundos.
Los datos que guardaremos en nuestro archivo csv son 'nombre_participante', 'edad_participante', 'respuesta_correcta', 'respuesta' y 'tiempo'
"""

#Creamos una Ventana de Dialogo haciendo uso de gui.Dlg
ventanaDeDialogo = gui.Dlg(title="Ensayo de Tarea de Pavlov")   #utilizaremos la variable ventanaDeDialogo, 
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
ventana = visual.Window([800,800], monitor="informacion", fullscr=False)#Se crea una ventana donde se presentará el ensayo
#El primer parámetro es una lista, que representa el tamaño de la ventana, es un numero entero, en este, el primero es el ancho, el segundo es lo alto
#el parámetro monitor, es para darle un identificador a nuestra ventana,  con un nombre representativo basta
#fullscr es un parámetro que nos indica si queremos que la ventana abarque toda nuestra pantalla, como le ponemos False, no ocupará toda la pantalla

#Objeto keyboard
kb = keyboard.Keyboard() #Se crea un objeto teclado usando keyboard.Keyboard, llamado kb, con el cual lee las entradas a través del teclado

#Mensaje a imprimir en pantalla
instrucciones = visual.TextBox2(ventana, text="""Instrucciones: En este ensayo, sonará una campana, seguido por una imagen, el objetivo es presionar lo más rápido la tecla G. Presiona cualquier tecla para continuar.""")
#Se crea un objeto de mensaje de texto usando visual.TextBox2, llamado
#instrucciones, como primer parámetro recibe la ventana en la cual se aplicará, y el texto, en este caso son las instrucciones
#del ensayo

#Dibujar el texto en buffer
instrucciones.draw()#Este método NO IMPRIME directamente a pantalla, más bien, dibuja en una pantalla
#que aun no presentas, para mostrar todo lo que vayas dibujando en este buffer, utilizamos el 
#método flip() de la ventana que creamos

#Muestra el buffer 
ventana.flip()#Este método de la ventana, muestra el buffer, es decir, todo los métodos draw() que hemos 
#usado a lo largo del programa, se mostrarán después de utilizar este método, y el buffer se limpiará
# por lo que nuestro buffer esta limpio a partir de este punto

#Espera una respuesta del teclado
c = kb.waitKeys()#La variable c es una lista, esta lista contiene un solo elemento, que es un objeto con 2 atributos
#llamados name para la tecla que se presiono y rt, que es el tiempo que le tomo presionar dicha tecla

if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
    ventana.close() #Cierra la ventana en la que se hizo el ensayo
    core.quit()     #Cierra todo lo referente a psychopy

#Como nuestro buffer no tiene un draw, se limpia la pantalla
ventana.flip()


#Nos da la dirección en la que se encuentra este archivo en la computadora
#Un ejemplo es entrar a la biblioteca de tu computadora, elegir este archivo
#darle click derecho y ver la información del archivo, encontrarás la ubicación
#actual del archivo, eso es lo que nos devuelve os.getcwd(), esto nos servirá para poder 
#usar archivos multimedia
directory = os.getcwd()

#Creamos un objeto sound, el cual tendra el sonido de la camapna, que se encuentra en la carpeta multimedia
sonido = sound.Sound(directory + '/multimedia/bell-ring-01.wav')#concatenamos la dirección que tenemos en la
#variable directory con la dirección dentro de la carpeta multimedia

#Creamos un objeto ImageStim, que recibe tres parámetros, el primero una ventana, el segundo, que es image, que es
#la dirección a la imagen, que esta dentro de la carpeta multimedia, y el tamanio de la imagen, que es un valor entre
#0 y 1
imagen = visual.ImageStim(ventana, image=directory + '/multimedia/blue.png', size=[0.8,0.8])


sonido.play()

core.wait(sonido.getDuration())

sonido.stop()

#Se dibuja la imagen en el buffer
imagen.draw()

#Se dibuja lo que tenemos en el buffer en la ventana
#El buffer se vacía y se queda en blanco
ventana.flip()

#Se reinicia el reloj interno del teclado
kb.clock.reset()

#Esperamos la respuesta del teclado del participante por lo máximo de 3 segundos
c = kb.waitKeys(maxWait = 3)

if c == None:#En este caso, el participante no presiono nada en los 3 segundos maximos que se le dio, y regresa un objeto None
    ok_data.append(True)#Se mostro la imagen
    ok_data.append('')#Como no presiono ninguna tecla, le pasaremos a la respuesta el valor ''
    ok_data.append(3)#Como pasaron los 3 segundos, le tomo 3 segundos para responder, agregamos esto a nuestra lista que pasaremos a csv
elif c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
    ventana.close() #Cierra la ventana en la que se hizo el ensayo
    core.quit()     #Cierra todo lo referente a psychopy
else:#Si se presiono alguna tecla
    ok_data.append(True) #Si se mostro la imagen
    ok_data.append(c[0].name) #Guardamos la tecla que presiono
    ok_data.append(c[0].rt)   #Guardamos el tiempo que le tomo responder


#================
#Final del ensayo
#================

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
    writer.writerow(['nombre_participante','edad_participante','se_mostro_imagen','tecla_presionada','tiempo'])

    #writer.writerow(ok_data)

#Final del programa
ventana.close() #Cierra la ventana en la que se hizo el ensayo
core.quit()     #Cierra todo lo referente a psychopy