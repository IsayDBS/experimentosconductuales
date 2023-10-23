from psychopy.hardware import keyboard
from psychopy import visual, core, gui
import csv, os, random

def dibujaCajas(imagenes):
    for i in imagenes:
        i.draw()

def listaImagenes(lista, iteraciones, diccionarioAux):
    listaAux = []
    for i in range(iteraciones):
        listaAux.append(diccionarioAux[lista[i]])
    return listaAux

ventanaDeDialogo = gui.Dlg(title="Experimento de Tarea de Parpadeo Atencional")

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

ventana = visual.Window(fullscr=True, color='black')

instrucciones = visual.TextBox2(ventana, text="""Se mostrarán varias imagenes de la letra L, el objetivo es decir si se vió la imagen L con la orientación correcta, es decir, la del abecedario, presionaras la tecla G, en caso contrario, presiona la H. Presiona cualquier tecla para iniciar""", color='white')

instrucciones.draw()

ventana.flip()

c = kb.waitKeys()

if c[0].name == 'escape':
    ventana.close()
    core.quit()

ventana.flip()

directory = os.getcwd()

imagenL0 = visual.ImageStim(ventana, image=directory + '/multimedia/n1.png', size=[0.2,0.2])

imagenL1 = visual.ImageStim(ventana, image=directory + '/multimedia/n2.png', size=[0.2,0.2])

imagenL2 = visual.ImageStim(ventana, image=directory + '/multimedia/n3.png', size=[0.2,0.2])

imagenL3 = visual.ImageStim(ventana, image=directory + '/multimedia/t1.png', size=[0.2,0.2])

imagenCaja0 = visual.ImageStim(ventana, image=directory + '/multimedia/box.png', size =[0.4,0.4], pos=[0.75, 0])

imagenCaja1 = visual.ImageStim(ventana, image=directory + '/multimedia/box.png', size =[0.4,0.4], pos=[-0.75, 0])

imagenCaja2 = visual.ImageStim(ventana, image=directory + '/multimedia/box.png', size =[0.4,0.4], pos=[0, -0.75])

imagenCaja3 = visual.ImageStim(ventana, image=directory + '/multimedia/box.png', size =[0.4,0.4], pos=[0, 0.75])

imagenCorrecto = visual.ImageStim(ventana, image=directory + '/multimedia/correct.png', size=[0.2,0.2])

imagenIncorrecto = visual.ImageStim(ventana, image=directory + '/multimedia/error.png', size=[0.2,0.2])

#Estructura de datos diccionario donde la llave será un objeto imagen,
#y el valor será si la L tiene orientación correcta o no
diccionarioAux = {imagenL0 : "L incorrecta", imagenL1: "L incorrecta", imagenL2: "L incorrecta", imagenL3: "L correcta"}

cajas = [imagenCaja0, imagenCaja1, imagenCaja2, imagenCaja3]

letras = [imagenL0, imagenL1, imagenL2, imagenL3]

posiciones = [[-0.75,0],[0.75,0],[0,-0.75],[0,0.75]]

seEncuentra = False

teclaPresionada = False

respuestas = []

for k in range(5):
    dibujaCajas(cajas)

    ventana.flip()

    letrasEnCajas = random.choices(letras, k=4)

    random.shuffle(posiciones)

    apariciones = random.randint(0,3)
        
    dibujaCajas(cajas) 

    for j in range(apariciones + 1):

        letrasEnCajas[j].pos = posiciones[j]

        if letrasEnCajas[j] == imagenL3:
                
            seEncuentra = True

        letrasEnCajas[j].draw()

    ventana.flip()

    core.wait(.35)

    dibujaCajas(cajas)

    ventana.flip()

    c = kb.waitKeys(keyList=['g','h','escape'])

    if c[0].name == 'escape':
        ventana.close()
        core.quit()

    if c[0].name == 'g' and seEncuentra == True:
        imagenCorrecto.draw()
        ventana.flip()
        core.wait(1)
    elif c[0].name == 'g' and seEncuentra == False:
        imagenIncorrecto.draw()
        ventana.flip()
        core.wait(1)
    elif c[0].name == 'h' and seEncuentra == False:
        imagenCorrecto.draw()
        ventana.flip()
        core.wait(1)
    elif c[0].name == 'h' and seEncuentra == True:
        imagenIncorrecto.draw()
        ventana.flip()
        core.wait(1)
    seEncuentra= False

ventana.flip()

mensaje1 = visual.TextBox2(ventana, text="Termina la primer fase del experimento, presiona cualquier tecla para continuar", color='white')

mensaje1.draw()

ventana.flip()

c = kb.waitKeys()

if c[0].name == 'escape':
    ventana.close()
    core.quit()

for j in range(4):

    for i in range(5):
        
        dibujaCajas(cajas)

        ventana.flip()

        letrasEnCajas = random.choices(letras, k=4)

        random.shuffle(posiciones)

        apariciones = random.randint(0,3)
        
        dibujaCajas(cajas) 

        for j in range(apariciones + 1):

            letrasEnCajas[j].pos = posiciones[j]

            if letrasEnCajas[j] == imagenL3:
                
                seEncuentra = True

            letrasEnCajas[j].draw()

        ventana.flip()

        core.wait(.35)

        dibujaCajas(cajas)

        ventana.flip()

        c = kb.waitKeys(keyList=['g','h','escape'])

        if c[0].name == 'escape':
            ventana.close()
            core.quit()

        if c[0].name == 'g' and seEncuentra == True:
            imagenCorrecto.draw()
            teclaPresionada = 'g'
            ventana.flip()
            core.wait(1)
        elif c[0].name == 'g' and seEncuentra == False:
            imagenIncorrecto.draw()
            teclaPresionada = 'g'
            ventana.flip()
            core.wait(1)
        elif c[0].name == 'h' and seEncuentra == False:
            imagenCorrecto.draw()
            teclaPresionada = 'h'
            ventana.flip()
            core.wait(1)
        elif c[0].name == 'h' and seEncuentra == True:
            imagenIncorrecto.draw()
            teclaPresionada = 'h'
            ventana.flip()
            core.wait(1)
        respuestas.append(['','',listaImagenes(letrasEnCajas,apariciones+1, diccionarioAux),seEncuentra, teclaPresionada])
        seEncuentra = False

despedida = visual.TextBox2(ventana, text='Aquí termina el experimento, gracias por participar.' , color='black')

despedida.draw()

ventana.flip()

core.wait(5)

ventana.flip()

with open('respuesta_experimento.csv','w',encoding='UTF8',newline='') as f:

    writer = csv.writer(f)

    writer.writerow(['nombre','edad','listaDeLs','seEncuentraL','teclaPresionada'])

    writer.writerow(ok_data)

    writer.writerows(respuestas)

ventana.close()
core.quit()     