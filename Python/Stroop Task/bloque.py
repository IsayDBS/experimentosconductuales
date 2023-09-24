from psychopy import core, visual, gui
from psychopy.hardware import keyboard
import random
import csv

"""
Este código es un bloque de enesayos.
Mostramos palabras que es un color, pero son coloreadas de otro color, lo que queremos es que el usuario presione
la tecla referente al color y no a la plaabra.
Los datos que se guardaran en el archivo csv son el nombre del participante, su edad, la respuesta corecta, 
la respuesta proporcionada por el participante y el tiempo que le tomo darla
"""

#Creamos una Ventana de Dialogo haciendo uso de gui.Dlg
ventanaDeDialogo = gui.Dlg(title="Bloque de Tarea de Stroop")   #utilizaremos la variable ventanaDeDialogo, 
#haciendo uso de gui.Dlg, este, tiene un parámetro title que es el nombre que aparece en el tope de la ventana

ventanaDeDialogo.addText('Información del participante')        #Agrega texto en un renglón de la ventana, en este caso
#inmediatamente abajo del título

ventanaDeDialogo.addField('Nombre:')          #Agrega el texto 'Nombre', después del cual, tiene un cuadro donde puedes agregar
#texto, todo esto estará abajo del texto de información del participante.

ventanaDeDialogo.addField('Edad:')            #Agrega el texto 'Edad', después del cual, tiene un cuadro donde puedes agregar
#texto, pero en este caso, se espera un número, todo esto estará abajo del texto 'Nombre'

ok_data = ventanaDeDialogo.show() #Muestra dos opciones, OK o Cancel

if ventanaDeDialogo.OK:  #Pregunta si el participante le dio a OK
    print(ok_data)#Imprimimos en terminal la lista ok_data, que consiste del nombre y la edad
else:                    #Se dió a Cancel
    print('Usuario canceló')#Le dió a Cancel, imprime en terminal 'Usuario canceló' y cancelamos el ensayo
    #Final del programa
    core.quit()     #Cierra todo lo referente a psychopy


#Creamos un objeto keyboard
kb = keyboard.Keyboard()#Nos permite leer una entrada del teclado

#Lista con las palabras que se presentará durante el bloque de ensayos
listaDeColores = ["ROJO","VERDE","AMARILLO","AZUL"]
random.shuffle(listaDeColores)#Barajamos la lista colorList, dandonos una lista con un orden diferente al declarado

#Lista de los colores con las que las palabras se colorearan
#estan en inglés porque ese es el valor que recibe el parámetro color
coloresDePalabras = ["red","green","yellow","blue"]

#Ventana
ventana = visual.Window(monitor="testMonitor", fullscr=True)#Ventana que mostrará el bloque de ensayos

#Instrucciones presentadas en forma de texto en la ventana
instrucciones = visual.TextBox2(ventana, text="""Instrucciones: En este experimento aparecerán palabras, estas estarán en un color, tendrás que escribir el color de la palabra, siendo rojo = r, verde = g, azul = b y amarillo = y""")

#Dibujamos las instrucciones en el buffer
instrucciones.draw()

#Mostramos lo dibujado en el buffer
ventana.flip()

#Esperamos una respuesta que venga del teclado
c = kb.waitKeys()

if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
        ventana.close() #Cierra la ventana en la que se hizo el ensayo
        core.quit()     #Cierra todo lo referente a psychopy

#Utilizaremos esta lista para guardar las respuestas dadas por el participante
respuestas = []

#==========================
#Inicio de bloque de ensayo
#==========================
for i in listaDeColores:     #Hacemos un for a listaDeColores, siendo i un color dentro de la listaDeColores
    kb.clock.reset()           #Reiniciamos el reloj dentro de nuestro objeto teclado       
    colorPalabra = coloresDePalabras[random.randint(0,3)] #Elegimos al azar el color que tendrá la palabra
    #Creamos otro objeto TextBox2, el cual mostrará la palabra, con el color al azar en la línea anterior y centrada 
    messagePrueba = visual.TextBox2(ventana, text=i, color=colorPalabra, alignment='center')
    messagePrueba.draw()    #Dibujamos el mensaje en el buffer
    ventana.flip()              #Pasamos lo que tenemos en el buffer a la ventana
    c = kb.waitKeys()       #Esperamos la respuesta del teclado del participante
    if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
        ventana.close() #Cierra la ventana en la que se hizo el ensayo
        core.quit()     #Cierra todo lo referente a psychopy
    #Agregamos a la lista respuestas, una lista, con la respuesta correcta, la respuesta que dio el participante y el tiempo
    #Agregamos dos espacios en blanco, ya que estos corresponden a las columnas de nombre y edad, y solo necesitamos este dato 
    #una vez, que fue puesto en el segundo renglón
    respuestas.append(['','',colorPalabra, c[0].name, c[0].rt])

#==========================
#Final del bloque de ensayo
#==========================

#Volvemos a abrir nuestro archivo csv
with open('respuestas_bloque.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)#Nos ayuda a escribir sobre nuestro archivo csv

    writer.writerow(['nombre','edad','respuesta_correcta','respuesta','tiempo'])#Primer renglón, el cual tendrá nuestros 
        #nombres de las columnas que vamos a usar

    writer.writerow(ok_data)#Escribe en el segundo renglón, como ok_data solo tienen dos valores, nombre y edad, solo llena 
        #las dos primeras columnas, dejando las demas en blanco

    writer.writerows(respuestas)#Ya que guardamos todos los resultados en nuestra lista respuestas
    #utilizamos el método writerows() que nos permite escribir diferentes renglones pasandole una lista
    #de listas, donde cada lista será un renglón nuevo


#cierre programa
ventana.close()
core.quit()