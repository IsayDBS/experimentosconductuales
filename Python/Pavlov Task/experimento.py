from psychopy import visual, sound, core, gui
from psychopy.hardware import keyboard
import os, csv, random

ventanaDeDialogo = gui.Dlg(title="Experimento de Tarea de Pavlov")

ventanaDeDialogo.addText('Información del participante')

ventanaDeDialogo.addField('Nombre:')

ventanaDeDialogo.addField('Edad:')

ok_data = ventanaDeDialogo.show()

if ventanaDeDialogo.OK:  
    print(ok_data)       
else:                    
    print('Usuario canceló')
    core.quit()     

ventana = visual.Window(monitor="informacion", fullscr=True, color='white')

kb = keyboard.Keyboard()


instrucciones = visual.TextBox2(ventana, text="""Instrucciones: En este experimento oiras una campana seguido por una imagen de un circulo azul, cuando veas la imagen, presiona la tecla G, solo cuando veas la imagen.""", color='black')

instrucciones.draw()

ventana.flip()

c = kb.waitKeys()

if c[0].name == 'escape':
    ventana.close() 
    core.quit()     

ventana.flip()

directory = os.getcwd()

sonido = sound.Sound(directory + '/multimedia/bell-ring-01.wav')

imagen = visual.ImageStim(ventana, image=directory + '/multimedia/blue.png', size=[0.8,0.8])

respuestas = []

for i in range(5):

    kb.clock.reset()

    sonido.play()

    core.wait(sonido.getDuration())

    sonido.stop()

    imagen.draw()

    ventana.flip()

    c = kb.waitKeys(maxWait = 3)

    if c == None:
        respuestas.append(['','',True,'',3])
    elif c[0].name == 'escape':
        ventana.close() 
        core.quit()     
    else:
        respuestas.append(['','',True,c[0].name,c[0].rt])

    ventana.flip()

for j in range(3):

    for i in range(5):
        
        kb.clock.reset()

        sonido.play()

        core.wait(sonido.getDuration())

        sonido.stop()

        if random.randint(0,1) == 1:

            imagen.draw()

            ventana.flip()

            c = kb.waitKeys(maxWait = 3)

            if c == None:
                respuestas.append(['','',True,'',3])
            elif c[0].name == 'escape':
                ventana.close() 
                core.quit()     
            else:
                respuestas.append(['','',True,c[0].name,c[0].rt])
        else:
            
            c = kb.waitKeys(maxWait = 3)

            if c == None:
                respuestas.append(['','',False,'',3])
            elif c[0].name == 'escape':
                ventana.close()
                core.quit()    
            else:
                respuestas.append(['','',False,c[0].name,c[0].rt])

        ventana.flip()


despedida = visual.TextBox2(ventana, text='Aquí termina el experimento, gracias por participar.' , color='black')

despedida.draw()

ventana.flip()

core.wait(5)

ventana.flip()

with open('respuestas_experimento.csv','w',encoding='UTF8',newline='') as f:
    
    writer = csv.writer(f)

    writer.writerow(['nombre','edad','se mostro imagen','tecla presionada','tiempo'])

    writer.writerow(ok_data)

    writer.writerows(respuestas)

ventana.close()
core.quit()