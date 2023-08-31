/*
*Priming Task se basa en la idea de relación de eventos 
*en el cual se da una palabra, después se presentan una imagen al azar
* y tiene que apretar el usuario cual es el que tiene mas relacion con la palabra
*
*/

var jsPsych = initJsPsych({
    on_finish: function(){
        jsPsych.data.get().localSave('csv','informacion.csv');
    },
});

var timeline = [];

var images = ["img/apple.png","img/samsung.png"];

var preload = {
    type: jsPsychPreload,
    images: images,
    auto_preload: true,
}

timeline.push(preload);

var bienvenida = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: `
    <p>En este experimento, se plantea que el participante presione una tecla que relacione</p>
    <p>la palabra que aparecerá por un momento con alguna de las dos marcas que se mencionan,</p>
    <p>también aparecerá una imagen al azar de alguna de las marcas.</p>
    `,
}

timeline.push(bienvenida)

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
        palabra: 'FOTOGRAFÍA',
        imagen: ["img/samsung.png","img/apple.png"],
    },
    {
        palabra: 'PRESTIGIO',
        imagen: ["img/samsung.png","img/apple.png"],
    },
];

//Muestra la imagen
var pruebaImagen = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: function() {
        let html = `
    <div class="container">
        <div>Presiona "E" para Apple</div>
        <div>Presiona "I" para Samsung</div>
    </div>
    <div style='width: 1100px;'>
        <img src="${jsPsych.timelineVariable('imagen')[jsPsych.randomization.randomInt(0,1)]}" style="width:500px;height:500px;">
    </div>
    `;
    return html;
    },
}

//Muestra la palabra 
var pruebaPalabra = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: function(){
        let html = `
    <div class="container-word">
        <div>Presiona "E" para Apple</div>
        <div>Presiona "I" para Samsung</div>
    </div>
    <div style='width: 1100px;'>
        <div class="blue-text">${jsPsych.timelineVariable('palabra')}</div>
    </div>
    `;

    return html;
    },
    trial_duration: 250,
    choices: "NO_KEYS",
}

var test_procedure = {
    timeline: [pruebaPalabra, pruebaImagen],
    timeline_variables: dummies,
    randomize_order: true,
}


timeline.push(test_procedure);

jsPsych.run(timeline);