from psychopy import core, visual, gui
from psychopy.hardware import keyboard
import random
import csv

ventanaDeDialogo = gui.Dlg(title="Bloque de Tarea de Stroop")

ventanaDeDialogo.addText('Información del participante')     

ventanaDeDialogo.addField('Nombre:')

ventanaDeDialogo.addField('Edad:')

ok_data = ventanaDeDialogo.show()

if ventanaDeDialogo.OK:
    print(ok_data)
else:                   
    print('Usuario canceló')
    core.quit()

kb = keyboard.Keyboard()

ventana = visual.Window(monitor="testMonitor", fullscr=True)

instrucciones = visual.TextBox2(ventana, text="""Instrucciones: En este experimento aparecerán palabras, estas estarán en un color, tendrás que escribir el color de la palabra, siendo rojo = r, verde = g, azul = b y amarillo = y""")

instrucciones.draw()

ventana.flip()

c = kb.waitKeys()

if c[0].name == 'escape':
        ventana.close() 
        core.quit()     

respuestas = []

listaDeColores = ["ROJO","VERDE","AMARILLO","AZUL"]

coloresDePalabras = ["red","green","yellow","blue"]

random.shuffle(listaDeColores)

for i in listaDeColores:
    kb.clock.reset() 
    colorPalabra = coloresDePalabras[random.randint(0,3)]

    messagePrueba = visual.TextBox2(ventana, text=i, color=colorPalabra, alignment='center')
    messagePrueba.draw()
    ventana.flip()
    c = kb.waitKeys()
    if c[0].name == 'escape':
        ventana.close() 
        core.quit()
    respuestas.append(['','',colorPalabra, c[0].name, c[0].rt])

ventana.flip()

mensaje1 = visual.TextBox2(ventana, text="Termina primera fase del experimento, presiona cualquier tecla para continuar")

mensaje1.draw()

ventana.flip()

c = kb.waitKeys()

if c[0].name == 'escape':
    ventana.close()
    core.quit()

ventana.flip()

for i in range(3):

    random.shuffle(listaDeColores)

    for i in listaDeColores:
        kb.clock.reset() 
        colorPalabra = coloresDePalabras[random.randint(0,3)]

        messagePrueba = visual.TextBox2(ventana, text=i, color=colorPalabra, alignment='center')
        messagePrueba.draw()
        ventana.flip()
        c = kb.waitKeys()
        if c[0].name == 'escape':
            ventana.close() 
            core.quit()
        respuestas.append(['','',colorPalabra, c[0].name, c[0].rt])

despedida = visual.TextBox2(ventana, text='Aquí termina el experimento, gracias por participar.' , color='black')

despedida.draw()

ventana.flip()

core.wait(5)

ventana.flip()

with open('respuestas_experimento.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['nombre','edad','respuesta_correcta','respuesta','tiempo'])

    writer.writerow(ok_data)

    writer.writerows(respuestas)

ventana.close()
core.quit()