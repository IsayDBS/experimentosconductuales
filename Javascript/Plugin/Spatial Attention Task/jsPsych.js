/*
*La tarea de atención espacial, se presenta una flecha apuntando a una dirección (arriba, abajo, izquierda, derecha)
*, despues de este, aparecerá una imagen, en cualquiera de estas direcciones
*al azar, el objetivo del participante es apretar la dirección en la que apareció la imagen 
*/

/*
* Variable jsPsych que utilizaremos a lo largo de programa, es lo mínimo requerido 
* para un programa jspsych
* el parámetro on_finish es una función que se ejecuta al terminar el experimento
* Crea un archivo csv con con nombre informacion.csv
*/
var jsPsych = initJsPsych({
    on_finish: function(){
        jsPsych.data.get().localSave('csv','informacion.csv');
    },
});

/*
* Variable timeline que es una lista que dice en que 
* orden va nuestro experimento
*/
var timeline = [];

/*
* Plugin que nos ayuda a carga archivos multimedia antes de usarlos 
* en nuesto experimento
*/
var preload = {
    type: jsPsychPreload, 
    images: ['img/circulo.png'], //lista de imagenes que se cargaran antes del experimento
    auto_preload: true, //si es true, carga las imagenes antes de que sean llamadas
}

/*
* Plugin que presenta las isntrucciones en pantalla
*/
var bienvenida = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: `
    <p>En este experimento, se mostrará una flecha apuntando en alguna dirección</p>
    <p>ya sea hacia arriba, abajo, derecha o izquierda, después de esto, se presentará</p>
    <p>una imagen en alguna de estas direcciones, tu objetivo es seleccionar una tecla</p>
    <p>que indique en que lugar esta la image.</p>ß
    <p>Esto con arriba(w), abajo(s), izquierda(a) o derecha(d)</p>
    `,
}

/*
* Agregamos las instrucciones a la lista de timeline
*/
timeline.push(bienvenida)

/*
* Creamos un plugin jsFleha
* No le pasamos ningun valor a posicion, por lo que su 
* valor es -1
*/
var flecha = {
    type: jsFlecha,
}

/*
* Agregamos el plugin flecha a timeline
*/
timeline.push(flecha)

/*
* Creamos un plugin jsImagen
* La imagen estará en la parte de arriba de la pantalla
*/

/*
* Creamos un plugin imagen
* Los parámetros que utilizaremos son posicion con el valor top
* y el parámetro imagen, con la dirección a la imagen.
*/
var imagen = {
    type: jsImagen,
    posicion: 'top',
    imagen: 'img/circulo.png',
  }

/*
* Agregamos el plugin imagen a timeline
*/
timeline.push(imagen)

/*
* Terminamos nuestro programa, pasamos timeline al método run()
*/
jsPsych.run(timeline);