/*
*Priming Task se basa en la idea de relación de eventos 
*en el cual se da una palabra, después se presentan una imagen al azar
* y tiene que apretar el usuario cual es el que tiene mas relacion con la palabra
*
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
* Imagenes utilizadas durante el experimento
*/
var images = ["img/X","img/Y"];

/*
* Plugin que nos ayuda a carga archivos multimedia antes de usarlos 
* en nuesto experimento
*/
var preload = {
    type: jsPsychPreload,
    images: images,
    auto_preload: true,
}

/*
*Agregamos preload a timeline
*/
timeline.push(preload);

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
* Mensaje de bienvenida en el cual se le explica de que trata el experimento
*/
var bienvenida = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: `
    <p>En este experimento, se plantea que el participante presione una tecla que relacione</p>
    <p>la palabra que aparecera por un momento con alguna de las dos marcas que se mencionan,</p>
    <p>tambien aparecera una imagen al azar de alguna de las marcas.</p>
    `,
}

/*
* Agregamos bienvenida a timeline
*/
timeline.push(bienvenida)

/*
* Mostrar imagen durante 30 ms
* stimulus recibe la dirección de la imagen
*
* stimulues_height es la altura de la imagen en pixeles,
* stimulus_width es la anchura de la imagen en pixeles
*/
var imagenes = {
    type: jsPsychImageKeyboardResponse,
    stimulus: "img/X",
    stimulus_height: 500,
    stimulus_width: 500,
    trial_duration: 30,
}

/*
* Agregamos la variable imagenes a timeline
*/
timeline.push(imagenes)

/*
* Plugin que solo presenta una cruz en la pantalla por 300 ms
*/
var fixation = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: function(){
      return '<div style="font-size:40px;">+</div>'
    },
    choices: "NO_KEYS", //Esto nos dice que no puede recibir valores del teclado
    trial_duration: 300, //cuanto dura la prueba
    data: {
      task: 'fixation'    //Solo nos dice como se llamará en el csv el plugin
    }
  }

/*
* Agregamos la variable fixation a timeline
*/
timeline.push(fixation)

/*
* Muestra la palabra en azul por 500 ms
*/
var palabraAzul = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: function(){
        let html = `
                    <div style='width: 1100px;'>
                        <div class="blue-text">${jsPsych.timelineVariable('palabra')}</div>
                    </div>
                    `;
        return html;
    },
    trial_duration: 500,
    choices: "NO_KEYS",
}

/*
* Agregamos palabraAzul a timeline
*/
timeline.push(palabraAzul)

/*
* Plugin de espacio entre imagenes, una pantalla en blanco que dura 150 ms.
*/
var espacioEntreIntervalos = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: "",
    trial_duration: 150,
    choices: "NO_KEYS",
}

/*
* Agregamos espacioEntreIntervalos a timeline
*/
timeline.push(espacioEntreIntervalos)

/*
* Plugin que presenta imagenes
*/
var pruebaImagen = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: function() {
        let html = `
    <div class="container-word">
        <p class="alignleft">Presiona "E" para X</p>
        <p class="alignright">Presiona "I" para Y</p>
    </div>
    `;
    return html;
    },
    choices: "NO_KEYS",
}

/*
* Agregamos la variable pruebaImagen a timeline
*/
timeline.push(pruebaImagen)

/*
*Terminaos el experimento, recibe la lista timeline
*/
jsPsych.run(timeline);