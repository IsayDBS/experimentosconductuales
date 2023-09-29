from psychopy import core, visual, gui  #Importamos core, visual y gui que utilizaremos durante el ensayo
from psychopy.hardware import keyboard  #Importamos keyboard, el cual lo utilizamos para poder usar nuestro teclado en el ensayo
import csv  #Utilizado para escribir un archivo csv dentro del cual guadará la información del ensayo

"""
Este código es un ensayo, se presenta una palabra coloreada con un color, el objetivo del participante es presionar una tecla
perteneciente al color.
Los datos que guardaremos en nuestro archivo csv son 'nombre_participante', 'edad_participante', 'respuesta_correcta', 'respuesta' y 'tiempo'
"""

#Creamos una Ventana de Dialogo haciendo uso de gui.Dlg
ventanaDeDialogo = gui.Dlg(title="Ensayo de Tarea de Stroop")   #utilizaremos la variable ventanaDeDialogo, 
#haciendo uso de gui.Dlg, este, tiene un parámetro title que es el nombre que aparece en el tope de la ventana

ventanaDeDialogo.addText('Información del participante')        #Agrega texto en un renglón de la ventana, en este caso
#inmediatamente abajo del título

ventanaDeDialogo.addField('Nombre:')          #Agrega el texto 'Nombre', después del cual, tiene un cuadro donde puedes agregar
#texto, todo esto estará abajo del texto de información del participante.

#ventanaDeDialogo.addField('Edad:')

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
instrucciones = visual.TextBox2(ventana, text="""Instrucciones: En este ensayo aparecerá una palabra de un color, esta estará coloreada de un color, tendrás que presionar una tecla con el color de la palabra, siendo rojo = r, verde = g, azul = b, amarillo = y.\n Presiona cualquier tecla para seguir al ensayo""")
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

#Palabra a mostrar en pantalla
palabra = visual.TextBox2(ventana, text="ROJO", color="yellow", alignment="center")
#el primer parámetro recibe la ventana donde se pondrá el texto
#text será el texto que se mostrará
#el parámetro color recibe un color en minisculas en inglés, en este caso yellow = amarillo
#el parámetro alignment recibe una posición en la cual aparecerá en la ventana, en este caso, la queremos en el centro
#por lo que usaremos center

#Dibujamos en el buffer la palabra
palabra.draw()

#Dibujamos en la ventana
ventana.flip()

#Reiniciamos el reloj interno del teclado
kb.clock.reset()#nuestro objeto teclado (kb) consta de un reloj interno, para tener precisión en nuestro resultado
#reiniciamos el reloj antes de pedir al usuario su respuesta

#Esperar respuesta del teclado
c = kb.waitKeys()

if c[0].name == 'escape':#Si la tecla presionada por el participante es esc
    #Final del programa
    ventana.close() #Cierra la ventana en la que se hizo el ensayo
    core.quit()     #Cierra todo lo referente a psychopy

#Como no tenemos nada en nuestro buffer, no muestra nada en la ventana, es una forma de limpiar la ventana
ventana.flip()

ok_data.append("yellow") #agregamos a la lista ok_data "yellow" que es la respuesta correcta

ok_data.append(c[0].name) #agregamos la tecla que el usuario presionó durante el ensayo

ok_data.append(c[0].rt) #agregamos el tiempo que le tomo al usuario responder



#================
#Final del ensayo
#================

#Guardamos información relevante de nuestro experimento en un archivo csv
#La siguiente línea solo nos dice como se va a llamar el archivo que gaurdará la información
#la 'w' que vamos a escribir en este
#encoding es para el tipo de caracteres que guardaremos
#newline solo nos dice como separar los renglones (no será necesario por ahora)
with open('respuestas_ensayo.csv','w',encoding='UTF8',newline='') as f:
    #writer nos ayudará a escribir en el archivo csv
    writer = csv.writer(f)

    #writer.writerow(['nombre_participante','edad_participante','respuesta_correcta','respuesta','tiempo'])

    #escribimos en el siguiente renglón toda la información pertinente a las columnas en el sigueinte renglón
    #utilizando la lista ok_data
    writer.writerow(ok_data)

#Final del programa
ventana.close() #Cierra la ventana en la que se hizo el ensayo
core.quit()     #Cierra todo lo referente a psychopy