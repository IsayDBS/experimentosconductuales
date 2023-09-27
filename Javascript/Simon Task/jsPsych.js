/*
*Simon Task es una prueba la cual consiste en responder a una tarea
*dada las instrucciones, sin dar atención a las distracciones que
* aparecen en el experimento
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
* Media 
*/
var images = ["img/green_o_f_f_b_079.jpg","img/green_o_f_h_a_079.jpg","img/green_o_f_n_b_079.jpg","img/red_o_f_f_b_079.jpg","img/red_o_f_h_a_079.jpg","img/red_o_f_n_b_079.jpg"]


/*
* Plugin que nos ayuda a carga archivos multimedia antes de usarlos 
* en nuesto experimento
*/
var preload = {
    type: jsPsychPreload,
    images: images,
    auto_preload: true
};

/*
* Pasamos el plugin preload a timeline
*/
timeline.push(preload);

/* 
* Mensaje de bienvenida 
*/
var bienvenida = {
  type: jsPsychHtmlKeyboardResponse,
  stimulus: "Bienvenido al experimento Simón dice. Presiona cualquier tecla para iniciar"
};

/*
* Pasamos bienvenidad a timeline
*/
timeline.push(bienvenida)

/* 
* Instrucciones del experimento 
*/
var instrucciones = {
  type: jsPsychHtmlKeyboardResponse,
  stimulus: `
  <p>En este experimento, varias imagenes apareceran en la pantalla</p>
  <p>Si la imagen es <strong>verde</strong> deberás presionar la tecla <strong>F</strong> la más rápido posible.</p>
  <p>Si la imagen es <strong>rojo</strong> deberás presionar la tecla <strong>J</strong> lo más rápido posible.</p>
  <p>Presiona cualquier tecla para empezar.</p>
  <div style='width: 1100px;'>
  <div style='float: left;'><img src='img/green_o_f_f_b_079.jpg'></img>
  <p class='small'><strong>Presiona la tecla F</strong></p></div>
  <div style='float: right;'><img src='img/red_o_f_f_b_079.jpg'></img>
  <p class='small'><strong>Presiona la tecla J</strong></p></div>
  </div>`
};

/*
* Pasamos instrucciones a timeline
*/
timeline.push(instrucciones)

/* 
* Cada iteración agarrará los valores de los objetos en la siguiente lista
* Mas adelante en el código se ve como funciona
* Estimulos posibles,se ponen entre {} para diferenciarlos
*/ 
var test_stimuli = [
    { stimulus: "img/green_o_f_f_b_079.jpg",  
      correct_response: 'f',
      position: 'left'
    },
    { stimulus: "img/green_o_f_h_a_079.jpg",  
      correct_response: 'f',
      position: 'left'
    },
    { stimulus: "img/green_o_f_n_b_079.jpg",  
      correct_response: 'f',
      position: 'left'
    },
    { stimulus: "img/red_o_f_f_b_079.jpg",  
      correct_response: 'j',
      position: 'left'
    },
    { stimulus: "img/red_o_f_h_a_079.jpg",  
      correct_response: 'j',
      position: 'left'
    },
    { stimulus: "img/red_o_f_n_b_079.jpg",  
      correct_response: 'j',
      position: 'left'
    },
    { stimulus: "img/green_o_f_f_b_079.jpg",  
      correct_response: 'f',
      position: 'right'
    },
    { stimulus: "img/green_o_f_h_a_079.jpg",  
      correct_response: 'f',
      position: 'right'
    },
    { stimulus: "img/green_o_f_n_b_079.jpg",  
      correct_response: 'f',
      position: 'right'
    },
    { stimulus: "img/red_o_f_f_b_079.jpg",  
      correct_response: 'j',
      position: 'right'
    },
    { stimulus: "img/red_o_f_h_a_079.jpg",  
      correct_response: 'j',
      position: 'right'
    },
    { stimulus: "img/red_o_f_n_b_079.jpg",  
      correct_response: 'j',
      position: 'right'
    }
];

/*
* Plugin que solo presenta una cruz en la pantalla por 500 ms
*/
var fixation = { 
    type: jsPsychHtmlKeyboardResponse,
    stimulus: '<div style="font-size:60px;">+</div>',
    choices: jsPsych.NO_KEYS, //Posible elecciones, puesto a sin respuesta
    trial_duration: 500,      //Duracion de la prueba, 500 ms
    data: {                 //Usamos data para agregar columnas en el archivo csv
      task: 'fixation'        //Solo nos dice como se llamará en el csv el plugin
                              //Bajo la columna task
    }
}
  
/*
* Se presenta la imagen en una posicion de la pantalla, ya sea a la derecha o a la izquierda
* Se espera una respuesta, ya sea la tecla f o j
* En las columnas que se agregan al csv:
* task con valor response
* correct_response, con la letra que tiene el valor correcto
* position, en que posicion estaba la imagen (izquierda o derecha)
* image_stim, la imagen utilizada durante la prueba
*
* el parámetro on_finish, que como dice, al finalizar la prueba, hará algo
* en este caso, ese algo, es agregar una nueva columna al csv, llamado correct, el cual compara el 
* valor dado por el participante y el que se tenía relacionado con dicha prueba
* El parámetro data que es pasado a on_finish contiene valores como rt, los que nosotros definimos
* en data y key, que es la tecla que el participante presiono.
*/
var prueba = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: function(){
                var html = `
                  <div style='width: 1100px;'>
                    <div style='float: ${jsPsych.timelineVariable('position')};'>
                      <img src="${jsPsych.timelineVariable('stimulus')}">
                    </div>
                  </div>`;
                return html;
            },
    choices: ['f', 'j'],  //posibles elecciones del teclado
    data: {
      task: 'response',
      correct_response: jsPsych.timelineVariable('correct_response'),
      position: jsPsych.timelineVariable('position'),
      imagen_stim: jsPsych.timelineVariable('stimulus')
    },
    on_finish: function(data){
      data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response);
    }
}  
  
/*
* Objeto que utilizaremos para repetir plugins con ciertas condiciones, en este caso
* timeline es una lista de los plugins que se mostraran en un orden fijo, primero irá
* fixation, seguido por prueba (cruz, seguido por la imagen)
*
* timeline_variables son las variables que tomaran jsPsych.timelineVariable durante el ensayo,
* se repetirá la cantidad de objetos en la lista, con cada iteración con valores diferentes, por ejemplo:
* 1ra iteracion:
* jsPsych.timelineVariable('correct_response') = 'j'
* jsPsych.timelineVariable('position') = 'right'
* jsPsych.timelineVariable('stimulus') = "img/red_o_f_h_a_079.jpg"
*
* 2daa iteracion:
* jsPsych.timelineVariable('correct_response') = 'f'
* jsPsych.timelineVariable('position') = 'right'
* jsPsych.timelineVariable('stimulus') = "img/red_o_f_n_b_079.jpg"
*
*randomize_order, como indica, hace al azar timeline_variables cuando su valor es true, por default es false
*
* repetitions, cuantas veces repite la lista, en este caso 2
*/
var test_procedure = {
    timeline: [fixation, prueba],
    timeline_variables: test_stimuli,
    randomize_order: true,
    repetitions: 2 
}

/*
* Podras notar que no empujamos los plugins individuales, si no lo que hicimos en test_procedure
*/
timeline.push(test_procedure);

/* 
* Ahora, mostraremos los valores que agarramos durante el experimento
* var trials = jsPsych.data.get().filter({task: 'response'}), nos da todos los renglones donde la columna
* 'task' su valor sea response
*
* var correct_trials = trials.filter({correct: true}); trials tiene todos los renglones anteriormente mencionados
* de estos, los que en su columna correct tengan el valor true, los guardamos en correct_trials
* 
* La variable acurracy guarda la precisión del experimento, esta se calcula como la cantidad de pruebas correctas
* entre los pruebas totales por 100, y todo eso lo redondeamos.
*
* var rt = Math.round(correct_trials.select('rt').mean()) nso devuelve el tiempo promedio que le tomo responder en ms
* todas las que tuve correctas.
* 
*/
var valoresFinales = {
  type: jsPsychHtmlKeyboardResponse,
  stimulus: function() {

    var trials = jsPsych.data.get().filter({task: 'response'});
    var correct_trials = trials.filter({correct: true});
    var accuracy = Math.round(correct_trials.count() / trials.count() * 100);
    var rt = Math.round(correct_trials.select('rt').mean());

    return `<p>Tus respuestas correctas fueron ${accuracy}% de las pruebas.</p>
      <p>Tú tiempo de respuesta promedio fue ${rt}ms.</p>
      <p>Presiona cualquier tecla para terminar el experimento. Gracias!</p>`;

  }
};

/*
* Empujamos los valores finales a timeline
*/
timeline.push(valoresFinales);

/*
*Terminaos el experimento
*/
jsPsych.run(timeline);