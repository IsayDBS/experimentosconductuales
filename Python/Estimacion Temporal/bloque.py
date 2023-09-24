from psychopy.hardware import keyboard
from psychopy import visual, core, gui
import csv, os, random
"""
Este código es un bloque de ensayos
Este código es un ensayo, se muestra una imagen en la pantalla, el punto del ensayo es que el usuario decida si la imagen
estuvo un tiempo corto (400ms) o largo (1600ms). En este ensayo, se presentará el estímulo, seguido de un texto informando si el
el estímulo fue largo o corto.
Se guardará la información referente al nombre del participante, la edad del participante, la tecla que debería presionar 
el participante, la tecla que presiono, si acerto o no y el tiempo que le tomo presionarla
"""

#Creamos una Ventana de Dialogo haciendo uso de gui.Dlg
ventanaDeDialogo = gui.Dlg(title="Bloque de Tarea Estimación Temporal")   #utilizaremos la variable ventanaDeDialogo, 
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

ventana = visual.Window(monitor="Monitor" ,fullscr=True, color='white')

kb = keyboard.Keyboard()

directory = os.getcwd()

#Para legilibilidad, escribiremos todos los mensaje que utilizaremos a lo largo del programa

instrucciones = visual.TextBox2(ventana, text="""A continuación se presentará una imagen seguida en alguna parte de la pantalla, después del cual, aparecerá un texto mencionando si fue presentado una larga duración o corta. Para cada opción, presion S para corta duración y L para larga duración. Presione la barra espaciadora para comenzar.""", color='black')
mensajeS = visual.TextBox2(ventana, text='El estimulo anterior fue de duración corta presiona S', color= 'black')
mensajeL = visual.TextBox2(ventana, text='El estímulo anterior fue de duración larga presiona L', color='black')

mensajeAtencion = visual.TextBox2(ventana, text='Atención', color='black', alignment="center", bold=True, size=[24,24])

#Rectángulo rojo
pantallaTamanio = ventana.windowedSize
pantallaRoja = visual.Rect(ventana, width = pantallaTamanio[0], height = pantallaTamanio[1], color='darkred')

#Imagen usada durante el programa
imagenAzul = visual.ImageStim(ventana, image=directory + '/img/blue.png',size=[0.2,0.2])

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

#Usaremos una lista para sacar los tiempos que aparecerá la imagen en la pantalla
tiempos = [.4, 1.6]

#Usaremos esta lista para mostrar las diferentes posiciones en las que puede aparecer la imagen en la pantalla
posiciones=[[0,0],[0.75,0.75],[0.75,-0.75],[-0.75,0.75],[-0.75,-0.75]]

#Lista respuestas, donde guardaremos los datos referentes a cada ensayo 
respuestas = []

#Se haran 5 ensayos, donde la imagen aparecera en una posición al azar en un tiempo al azar
for i in range(5):
    #Se barajea las posiciones para que podamos hacer azar
    random.shuffle(posiciones)

    #Se barajea los tiempos, para que sean al azar
    random.shuffle(tiempos)

    #Se dibuja la pantalla roja sobre el buffer
    pantallaRoja.draw()

    #Se imprime el emnsaje atención sobre el rectángulo rojo 
    mensajeAtencion.draw()

    #Se pasa el buffer a la ventana, se vacía el buffer
    ventana.flip()

    #El programa espera un segundo
    core.wait(1)

    #Le damos la posición a la imagen, eligiendo el primer elemento de la lista
    #a la cual le hicimos un shuffle (barajear)
    imagenAzul.pos=posiciones[0]

    #Dibujamos la imagen en el buffer
    imagenAzul.draw()

    #Pasamos el buffer a la ventana, se vacía el buffer
    ventana.flip()

    #Elegimos el primer elemento de la lista tiempos, a la cual
    #le hicimos un shuffle (barajear)
    core.wait(tiempos[0])

    #Como no hay nada en el buffer, la pantalla se limpia
    ventana.flip()

    #Se reinicia el reloj interno de la clase teclado
    kb.clock.reset()

    #Esperamos la respuesta del participante
    #ya sea s, l o escape
    c = kb.waitKeys(keyList=['s','l','escape'])
    if c[0].name == 's': #El usuario eligió un tiempo corto, es decir 's'
        if tiempos[0] == .4: #La imagen aparecio por un tiempo corto
            #Se agrega la lista a respuestas, los dos primeros elementos
            #correspondientes al nombre y la edad,
            #el tercer elemento es de la tecla que debió presionar
            #el cuarto elemento es de la tecla que presiono el participante
            #el quinto elemento es del tiempo que tardo en presionar
            respuestas.append(['','','s','s',c[0].rt])            
        else: #La imagen aparecio por un tiempo largo (1.6)
            respuestas.append(['','','l','s',c[0].rt])
    elif c[0].name == 'escape':#Se presiono la tecla escape
        #Final del programa
        ventana.close() #Cierra la ventana en la que se hizo el ensayo
        core.quit()     #Cierra todo lo referente a psychopy
    else:#El usuario eligió un tiempo largo, es decir 'L'
        if tiempos[0] == .4:#La imagen aparecio por un tiempo corto
            #Se agrega la lista a respuestas, los dos primeros elementos
            #correspondientes al nombre y la edad,
            #el tercer elemento es de la tecla que debió presionar
            #el cuarto elemento es de la tecla que presiono el participante
            #el quinto elemento es del tiempo que tardo en presionar
            respuestas.append(['','','s','l',c[0].rt])
        else:#La imagen aparecio por un tiempo largo
            respuestas.append(['','','l','l',c[0].rt])


#======================
#Aquí termina el bloque
#======================

#Guardamos información relevante de nuestro experimento en un archivo csv
#La siguiente línea solo nos dice como se va a llamar el archivo que gaurdará la información
#la 'w' que vamos a escribir en este
#encoding es para el tipo de caracteres que guardaremos
#newline solo nos dice como separar los renglones (no será necesario por ahora)
with open('respuesta_bloques.csv','w',encoding='UTF8',newline='') as f:
    #writer nos ayudará a escribir en el archivo csv
    writer = csv.writer(f)

    #el método writerow() escribirá en un renglón, en este caso, en el primer renglón del archivo csv
    #con los elementos de la lista en una columna diferente en el mismo renglón
    writer.writerow(['nombre','edad','teclaAPresionar','teclaPresionada','tiempo'])

    #escribimos en el siguiente renglón toda la información pertinente a las columnas en el sigueinte renglón
    #utilizando la lista ok_data
    writer.writerow(ok_data)

    #Ya que guardamos todos los resultados en nuestra lista respuestas
    #utilizamos el método writerows() que nos permite escribir diferentes renglones pasandole una lista
    #de listas, donde cada lista será un renglón nuevo
    writer.writerows(respuestas)


#Final del programa
ventana.close() #Cierra la ventana en la que se hizo el ensayo
core.quit()     #Cierra todo lo referente a psychopy