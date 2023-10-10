from psychopy.hardware import keyboard
from psychopy import visual, core, gui
import csv, os, random


ventanaDeDialogo = gui.Dlg(title="Experimento de Tarea Estimación Temporal")

ventanaDeDialogo.addText('Información del participante')

ventanaDeDialogo.addField('Nombre:')

ventanaDeDialogo.addField('Edad:')

ok_data = ventanaDeDialogo.show()

if ventanaDeDialogo.OK: 
    print(ok_data)
else: 
    print('Usuario canceló')
    core.quit()

ventana = visual.Window(monitor="Monitor" ,fullscr=True, color='white')

kb = keyboard.Keyboard()

directory = os.getcwd()

instrucciones = visual.TextBox2(ventana, text="""A continuación se presentará una imagen seguida en alguna parte de la pantalla, después del cual, aparecerá un texto mencionando si fue presentado una larga duración o corta. Para cada opción, presion S para corta duración y L para larga duración. Presione la barra espaciadora para comenzar.""", color='black')

mensajeS = visual.TextBox2(ventana, text='El estimulo anterior fue de duración corta presiona S', color= 'black')

mensajeL = visual.TextBox2(ventana, text='El estímulo anterior fue de duración larga presiona L', color='black')

mensajeAtencion = visual.TextBox2(ventana, text='Atención', color='black', alignment="center", bold=True, size=[24,24])

pantallaTamanio = ventana.windowedSize

pantallaRoja = visual.Rect(ventana, width = pantallaTamanio[0], height = pantallaTamanio[1], color='darkred')

imagenAzul = visual.ImageStim(ventana, image=directory + '/img/blue.png',size=[0.5,0.5])

instrucciones.draw()

ventana.flip()

c = kb.waitKeys(keyList=['space','escape'])

if c[0].name == 'escape':
    ventana.close() 
    core.quit()

ventana.flip()

tiempos = [.4, 1.6]

posiciones=[[0,0],[0.75,0.75],[0.75,-0.75],[-0.75,0.75],[-0.75,-0.75]]

respuestas = []

for j in range(4):

    for i in range(5):
        random.shuffle(posiciones)

        random.shuffle(tiempos)

        pantallaRoja.draw()

        mensajeAtencion.draw()

        ventana.flip()

        core.wait(1)

        imagenAzul.pos=posiciones[0]

        imagenAzul.draw()

        ventana.flip()

        core.wait(tiempos[0])

        ventana.flip()

        kb.clock.reset()

        c = kb.waitKeys(keyList=['s','l','escape'])
        if c[0].name == 's':
            if tiempos[0] == .4:
                respuestas.append(['','','s','s',c[0].rt])            
            else:
                respuestas.append(['','','l','s',c[0].rt])
        elif c[0].name == 'escape':
            ventana.close()
            core.quit()
        else:
            if tiempos[0] == .4:
                respuestas.append(['','','s','l',c[0].rt])
            else:
                respuestas.append(['','','l','l',c[0].rt])

with open('respuesta_experimento.csv','w',encoding='UTF8',newline='') as f:
    
    writer = csv.writer(f)

    writer.writerow(['nombre','edad','teclaAPresionar','teclaPresionada','tiempo'])

    writer.writerow(ok_data)

    writer.writerows(respuestas)



ventana.close()
core.quit() 