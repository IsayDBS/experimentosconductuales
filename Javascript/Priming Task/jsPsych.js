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
var images = ["img/apple.png","img/samsung.png"];

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
* Mostrar imagenes al azar durante 30 ms
* jsPsych.timelineVariable('imagen') consigue el objetgo relacionado con
* la palabra imagen de la lista de variables
*
* [jsPsych.randomization.randomInt(0,1)] nos ayuda a sacar una posición al azar de una
* lista de dos elementos.
*
* stimulues_height es la altura de la imagen en pixeles,
* stimulus_width es la anchura de la imagen en pixeles
*/
var imagenes = {
    type: jsPsychImageKeyboardResponse,
    stimulus: function(){
               return `${jsPsych.timelineVariable('imagen')[jsPsych.randomization.randomInt(0,1)]}`
            },
    stimulus_height: 500,
    stimulus_width: 500,
    trial_duration: 30,
}

/* 
* Cada iteración agarrará los valores de los objetos en la siguiente lista
* Mas adelante en el código se ve como funciona
* Estimulos posibles,se ponen entre {} para diferenciarlos
*/ 
var dummies = [
    {
        palabra: 'COSTO',
        imagen: ["img/samsung.png","img/apple.png"],
    },
    {
        palabra: 'DURABILIDAD',
        imagen: ["img/samsung.png","img/apple.png"],
    },
    {
        palabra: 'VANGUARDIA',
        imagen: ["img/samsung.png","img/apple.png"],
    },
    {
        palabra: 'ESTILO',
        imagen: ["img/samsung.png","img/apple.png"],
    },
    {
        palabra: 'ACCESIBILIDAD',
        imagen: ["img/samsung.png","img/apple.png"],
    },
    {
        palabra: 'FOTOGRAFIA',
        imagen: ["img/samsung.png","img/apple.png"],
    },
    {
        palabra: 'PRESTIGIO',
        imagen: ["img/samsung.png","img/apple.png"],
    },
];

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
* Plugin que presenta imagenes
*/
var pruebaImagen = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: function() {
        let html = `
    <div class="container-word">
        <p class="alignleft">Presiona "E" para Apple</p>
        <p class="alignright">Presiona "I" para Samsung</p>
    </div>
    `;
    return html;
    },
    choices: "NO_KEYS",
}

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
* Objeto que utilizaremos para repetir plugins con ciertas condiciones, en este caso
* timeline es una lista de los plugins que se mostraran en un orden fijo, primero irá
* imagenes, fixation, palabraAzul, espacioEntreIntervalos, pruebaImagen
*
* timeline_variables son las variables que tomaran jsPsych.timelineVariable durante el ensayo,
* se repetirá la cantidad de objetos en la lista, con cada iteración con valores diferentes, por ejemplo:
* 1ra iteracion:
* jsPsych.timelineVariable('palabra') = 'COSTO'
* jsPsych.timelineVariable('imagen') = ["img/samsung.png","img/apple.png"]
*
* 2da iteracion:
* jsPsych.timelineVariable('palabra') = 'DURABILIDAD'
* jsPsych.timelineVariable('imagen') = ["img/samsung.png","img/apple.png"]
*/
var test_procedure = {
    timeline: [imagenes, fixation, palabraAzul, espacioEntreIntervalos, pruebaImagen],
    timeline_variables: dummies,
}

/*
* Podras notar que no empujamos los plugins individuales, si no lo que hicimos en test_procedure
*/
timeline.push(test_procedure);

/*
*Terminaos el experimento, recibe la lista timeline
*/
jsPsych.run(timeline);