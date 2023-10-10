from psychopy import visual, sound, core, gui
from psychopy.hardware import keyboard
import os, csv, random

"""
Este código es un bloque de ensayos. Se pone el sonido seguido de una imagen 5 veces, con un máximo de 3 segundos para presionar la tecla G.
Los datos que se guardaran en el archivo csv son el nombre del participante, su edad, si aparecio la imagen
la tecla presionada y el tiempo que le tomo darla
"""
#Creamos una Ventana de Dialogo haciendo uso de gui.Dlg
ventanaDeDialogo = gui.Dlg(title="Bloque de Tarea de Pavlov")   #utilizaremos la variable ventanaDeDialogo, 
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
#Ventana
ventana = visual.Window(monitor="informacion", fullscr=True, color='white')#Se crea una ventana donde se presentará el ensayo
#el parámetro monitor, es para darle un identificador a nuestra ventana,  con un nombre representativo basta
#fullscr es un parámetro que nos indica si queremos que la ventana abarque toda nuestra pantalla, como le ponemos True, ocupará toda la pantalla
#color nos dará el color de la ventana, en este caso, blanco

#Creamos un objeto keyboard, con el cual leeremos lo que presione el usuario en el teclado
kb = keyboard.Keyboard()

#Instrucciones presentadas en forma de texto en la ventana, con un parámetro llamado color, que cambiará las letras a color negro
instrucciones = visual.TextBox2(ventana, text="""Instrucciones: En este experimento oiras una campana seguido por una imagen de un circulo azul, cuando veas la imagen, presiona la tecla G, solo cuando veas la imagen.""", color='black')

#Dibuja las isntrucciones en el buffer
instrucciones.draw()

#Pasa el buffer a la ventana, y vacía el buffer
ventana.flip()

#Esperamos la respuesta del participante
c = kb.waitKeys()

if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
    ventana.close() #Cierra la ventana en la que se hizo el ensayo
    core.quit()     #Cierra todo lo referente a psychopy

#Pasa el buffer a la ventana, dejando vacío el buffer
ventana.flip()

#Nos da la dirección en la que se encuentra este archivo en la computadora
directory = os.getcwd()

#Creamos un objeto sound, el cual tendra el sonido de la camapna, que se encuentra en la carpeta multimedia
sonido = sound.Sound(directory + '/multimedia/bell-ring-01.wav')

#Creamos un objeto ImageStim, que recibe tres parámetros, el primero una ventana, el segundo, que es image, que es
#la dirección a la imagen, que esta dentro de la carpeta multimedia, y el tamanio de la imagen, que es un valor entre
#0 y 1
imagen = visual.ImageStim(ventana, image=directory + '/multimedia/blue.png', size=[0.8,0.8])

#Lista de listas que tendrá las respuestas dadas por el participante y que después se pasará al archivo csv
respuestas = []

#Repertiremos el ensayo 5 veces, se presenta sonido seguido por la imagen
for i in range(5):

    #Reiniciamos el reloj interno dentro del teclado
    kb.clock.reset()

    #Reproducimos el sonido con el método play()

    #Esperamos que se reproduzca por completo el sonido, utiizamos core.wait() que espera un tiempo determinado
    #utilizamos getDuration() para saber la duración de dicho sonido

    #Después de reproducido el sonido, es necesario detenerlo, por lo que usamos el método stop()

    #Dibujamos la imagen en el buffer
    imagen.draw()

    #Pasamos el buffer a la ventana, dejando el buffer vacío
    ventana.flip()

    #Esperamos la respuesta del teclado del participante por lo máximo de 3 segundos
    c = kb.waitKeys(maxWait = 3)

    if c == None:#En este caso, el participante no presiono nada en los 3 segundos maximos que se le dio, y regresa un objeto None
        respuestas.append(['','',True,'',3])#Agregamos una lista a la lista respuestas, siendo los primeros 2 elementos '', porque
        #son las columnas nombre y edad, el tercer elemento es si aparecio la imagen, en este caso, siempre aparecera
        #la cuarta posicion será '', porque el usuario no presiono ninguna tecla
        #y en la quinta posición, 3, ya que el usuario no presiono ninguna tecla, le tomó 3 segundos
    elif c[0].name == 'escape':#Si la tecla presionada por el participante es esc
        #Final del programa
        ventana.close() #Cierra la ventana en la que se hizo el ensayo
        core.quit()     #Cierra todo lo referente a psychopy
    else:#Si se presiono alguna tecla
        respuestas.append(['','',True,c[0].name,c[0].rt])#Agregamos una lista a la lista respuestas, siendo los primeros 2 elementos '', porque
        #son las columnas nombre y edad, el tercer elemento es si aparecio la imagen, en este caso, siempre aparecera
        #la cuarta posicion será la tecla presionada por el usuario
        #y en la quinta posición el tiempo que le tomo presionar la tecla

    #Como nuestro buffer no tiene nada dibujado, limpia la pantalla, no presentando nada
    ventana.flip()

#Presentaremos 5 ensayos, solo que esta vez, pueden ir intercaladas las apariciones de las imagenes
#Pero siempre se oira la campana
for i in range(5):
    #Reiniciamos el reloj interno dentro del teclado
    kb.clock.reset()

    #Reproducimos el sonido con el método play()
    

    #Esperamos que se reproduzca por completo el sonido, utiizamos core.wait() que espera un tiempo determinado
    #utilizamos getDuration() para saber la duración de dicho sonido
    

    #Después de reproducido el sonido, es necesario detenerlo, por lo que usamos el método stop()
    

    #Haremos uso de la función random para que sea 50% y 50% de posibilidad de que aparezca la imagen
    if random.randint(0,1) == 1: #Si la funcion random.randint(0,1) que elige un numero entero entre el rango 0 y 1, es 1
        #Se imprime la imagen
        #Dibujamos la imagen en el buffer
        imagen.draw()

        #Pasamos el buffer a la ventana, dejando el buffer vacío
        ventana.flip()

        #Esperamos la respuesta del teclado del participante por lo máximo de 3 segundos
        c = kb.waitKeys(maxWait = 3)

        if c == None:#En este caso, el participante no presiono nada en los 3 segundos maximos que se le dio, y regresa un objeto None
            respuestas.append(['','',True,'',3])#Agregamos una lista a la lista respuestas, siendo los primeros 2 elementos '', porque
            #son las columnas nombre y edad, el tercer elemento es si aparecio la imagen, en este caso, siempre aparecera
            #la cuarta posicion será '', porque el usuario no presiono ninguna tecla
            #y en la quinta posición, 3, ya que el usuario no presiono ninguna tecla, le tomó 3 segundos
        elif c[0].name == 'escape':#Si la tecla presionada por el participante es esc
            #Final del programa
            ventana.close() #Cierra la ventana en la que se hizo el ensayo
            core.quit()     #Cierra todo lo referente a psychopy
        else:#Si se presiono alguna tecla
            respuestas.append(['','',True,c[0].name,c[0].rt])#Agregamos una lista a la lista respuestas, siendo los primeros 2 elementos '', porque
            #son las columnas nombre y edad, el tercer elemento es si aparecio la imagen, en este caso, siempre aparecera
            #la cuarta posicion será la tecla presionada por el usuario
            #y en la quinta posición el tiempo que le tomo presionar la tecla
    else:#La funcion random.randint(0,1) == 0
        #No se imprime la imagen

        #Esperamos la respuesta del teclado del participante por lo máximo de 3 segundos
        c = kb.waitKeys(maxWait = 3)

        if c == None:#En este caso, el participante no presiono nada en los 3 segundos maximos que se le dio, y regresa un objeto None
            respuestas.append(['','',False,'',3])#Agregamos una lista a la lista respuestas, siendo los primeros 2 elementos '', porque
            #son las columnas nombre y edad, el tercer elemento es si aparecio la imagen, en este caso, no aparecio la imagen(False)
            #la cuarta posicion será '', porque el usuario no presiono ninguna tecla
            #y en la quinta posición, 3, ya que el usuario no presiono ninguna tecla, le tomó 3 segundos
        elif c[0].name == 'escape':#Si la tecla presionada por el participante es esc
            #Final del programa
            ventana.close() #Cierra la ventana en la que se hizo el ensayo
            core.quit()     #Cierra todo lo referente a psychopy
        else:#Si se presiono alguna tecla
            respuestas.append(['','',False,c[0].name,c[0].rt])#Agregamos una lista a la lista respuestas, siendo los primeros 2 elementos '', porque
            #son las columnas nombre y edad, el tercer elemento es si aparecio la imagen, en este caso, no aparecio imagen(False)
            #la cuarta posicion será la tecla presionada por el usuario
            #y en la quinta posición el tiempo que le tomo presionar la tecla

    #Como nuestro buffer no tiene nada dibujado, limpia la pantalla, no presentando nada
    ventana.flip()

#================
#Final del bloque
#================

#Guardamos información relevante de nuestro experimento en un archivo csv
#La siguiente línea solo nos dice como se va a llamar el archivo que gaurdará la información
#la 'w' que vamos a escribir en este
#encoding es para el tipo de caracteres que guardaremos
#newline solo nos dice como separar los renglones (no será necesario por ahora)
with open('respuestas_bloque.csv','w',encoding='UTF8',newline='') as f:
    #writer nos ayudará a escribir en el archivo csv
    writer = csv.writer(f)

    #el método writerow() escribirá en un renglón, en este caso, en el primer renglón del archivo csv
    #con los elementos de la lista en una columna diferente en el mismo renglón
    writer.writerow(['nombre','edad','se mostro imagen','tecla presionada','tiempo'])

    #Escribimos en el segundo renglón los datos de nombre y edad del participante
    writer.writerow(ok_data)

    #Ya que guardamos todos los resultados en nuestra lista respuestas
    #utilizamos el método writerows() que nos permite escribir diferentes renglones pasandole una lista
    #de listas, donde cada lista será un renglón nuevo
    writer.writerows(respuestas)

#cierre programa
ventana.close()
core.quit()