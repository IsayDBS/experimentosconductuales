/*
*La tarea de atención espacial, se presenta una flecha apuntando a una dirección (arriba, abajo, izquierda, derecha)
*, despues de este, aparecerá una imagen, en cualquiera de estas direcciones
*al azar, el objetivo del participante es apretar la dirección en la que apareció la imagen 
*
* Como nota adicional, utiliza el navegador Google Chrome
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
* Agregamos el plugin preload a timeline
*/
timeline.push(preload)

/*
* Plugin utilizado para conseguir información del participante
*/
var cuestionario = {
    type: jsPsychSurveyText,
    questions: [
      {prompt: 'Escribe tu nombre', name: 'Nombre'},
      {prompt: 'Escribe tu edad', name: 'Edad'}
    ]
  }
  
/*
* Pasamos el plugin cuestionario a timeline
*/
timeline.push(cuestionario)

/*
* Plugin que presenta las instrucciones en pantalla
*/
var bienvenida = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: `
    <p>En este experimento, se mostrara una flecha apuntando en alguna direccion</p>
    <p>ya sea hacia arriba, abajo, derecha o izquierda, despues de esto, se presentara</p>
    <p>una imagen en alguna de estas direcciones, tu objetivo es seleccionar una tecla</p>
    <p>que indique en que lugar esta la imagen.</p>
    <p>Esto con arriba (W), abajo (S), izquierda (A) o derecha (D)</p>
    `,
}

/*
* Agregamos las instrucciones a la lista de timeline
*/
timeline.push(bienvenida)

/*
* Creamos un plugin jsFleha
* direccion es un valor entre -1 y 3
* 
*/
/*
var flecha = {
    type: jsFlecha,
    direccion: __,  
}
*/

/*
* Agregamos el plugin flecha a timeline
*/
timeline.push(flecha)

/*
* Creamos un plugin imagen
* posicion es un valor string, siendo 'top', 'bottom',
* 'left', 'right'
* imagen es un valor string, es la direccion a la 
* imagen, la cual se encuentra en la carpeta
* ejemplo: "img/circulo.png"
*/
/*
var imagen = {
    type: jsImagen,
    posicion: ____,
    imagen: ____,
  }
*/

/*
* Agregamos imagen a timeline
*/
timeline.push(imagen)

/*
* Terminamos nuestro programa, pasamos timeline al método run()
*/
jsPsych.run(timeline);