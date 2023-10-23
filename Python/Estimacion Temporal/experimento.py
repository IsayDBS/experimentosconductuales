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

fixation = visual.TextBox2(ventana, text='+', color='black', alignment='center')

imagenAzul = visual.ImageStim(ventana, image=directory + '/img/blue.png',size=[0.5,0.5])

instrucciones.draw()

ventana.flip()

c = kb.waitKeys(keyList=['space','escape'])

if c[0].name == 'escape':
    ventana.close() 
    core.quit()

ventana.flip()

tiempos = [.4, .4, 1.6, 1.6]

posiciones=[[0,0],[0.75,0.75],[0.75,-0.75],[-0.75,0.75],[-0.75,-0.75]]

tiempos = [.4, 1.6, .4, 1.6]

random.shuffle(tiempos)

for k in tiempos:

    random.shuffle(posiciones)

    fixation.draw()

    ventana.flip()

    core.wait(.3)

    imagenAzul.pos = posiciones[0]

    imagenAzul.draw()

    ventana.flip()

    core.wait(k)

    ventana.flip()

    if k == 0.4:

        mensajeS.draw()

        ventana.flip()

        c = kb.waitKeys(keyList=['escape','s'])

        if c[0].name == 'escape':
            
            ventana.close()
            
            core.quit()
        
        else:
            
            ventana.flip()
    else:

        mensajeL.draw()

        ventana.flip()

        c = kb.waitKeys(keyList=['escape','l'])

        if c[0].name == 'escape':
            
            ventana.close()
            
            core.quit()
        
        else:
            
            ventana.flip()

mensaje1 = visual.TextBox2(ventana, text="Termina la primera parte del experimento, presiona cualquier tecla para continuar con la segunda fase", color='black')

mensaje1.draw()

ventana.flip()

c = kb.waitKeys()

if c[0].name == 'escape':
    ventana.close()
    core.quit()

tiempos = [.4, .6, .8, 1, 1.2, 1.4, 1.6]

respuestas = []

for j in range(2):

    random.shuffle(tiempos)

    for i in tiempos:
        random.shuffle(posiciones)

        fixation.draw()

        ventana.flip()

        core.wait(.3)

        imagenAzul.pos=posiciones[0]

        imagenAzul.draw()

        ventana.flip()

        core.wait(i)

        ventana.flip()

        kb.clock.reset()

        c = kb.waitKeys(keyList=['s','l','escape'], maxWait= 5)

        if c == None:
            if i < 1:
                respuestas.append(['','','s','-',5])
            elif i == 1:
                respuestas.append(['','','m','-',5])
            else:
                respuestas.append(['','','l','-',5])
        elif c[0].name == 'escape':
            ventana.close()
            core.quit()
        else:
            if i < 1:
                respuestas.append(['','','s',c[0].name,c[0].rt])
            elif i == 1:
                respuestas.append(['','','m',c[0].name,c[0].rt])
            else:
                respuestas.append(['','','l',c[0].name,c[0].rt])

despedida = visual.TextBox2(ventana, text='Aquí termina el experimento, gracias por participar.' , color='black')

despedida.draw()

ventana.flip()

core.wait(5)

ventana.flip()

with open('respuesta_experimento.csv','w',encoding='UTF8',newline='') as f:
    
    writer = csv.writer(f)

    writer.writerow(['nombre','edad','teclaAPresionar','teclaPresionada','tiempoDeTeclaPresionada'])

    writer.writerow(ok_data)

    writer.writerows(respuestas)



ventana.close()
core.quit() 