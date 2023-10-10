/*
* Plugin personalizado que muestra una imagen en alguna dirección de la pantalla
* Ya sea arriba, abajo, derecha o izquierda
* El nombre de nuestro plugin es jsImagen
*/
var jsImagen = (function (jspsych){
    "use strict"

    /*
    * El nombre del plugin en el csv se llamará Imagen
    * Recibirá dos parámetros
    * posicion, que es un string 
    * Se espera que sea top, bottom, left o right.
    * como default es undefined, es 
    * obligatorio que se le pase algún valor.
    * 
    * imagen, que es un tipo IMAGE, pero funciona como string,
    * Se espera que sea la dirección a la imagen
    * Como default es undefined, es obligatorio que se le pase 
    * un valor.
    */
    const info = {
        name: 'Imagen',
        parameters:{
            posicion: { //posicion de la imagen
                type: jspsych.ParameterType.STRING,
                default: undefined,
            },
            imagen: { //imagen a usar
                type: jspsych.ParameterType.IMAGE, 
                default: undefined,
            },
        }
    }

    class Imagen{

        /*
        * Constructor estándar, siempre que se crea un pulgin personalizado
        * este es obligatorio
        */
        constructor(jsPsych){
            this.jsPsych = jsPsych;
        }

        /*
        * Método trial, en este método va todo lo que hará nuestro plugin
        * display_element es un objeto que utilizamos para mostrar elementos html
        * trial es un objeto que sus atributos son los parámetros
        */
        trial(display_element, trial){

            /*
            * Variable html_content, lo inicializamos
            */
            var html_content = ""

            /*
            * Preguntamos que posicion el programador paso en el parámetro posicion, siendo
            * si es left, right o top, bottom
            * Se le pasa a la variable html_content el código correspondiente a la posicion
            */
            if(trial.posicion === "left" || trial.posicion === "right"){
                html_content = `<div style='width: 1100px;'>
                    <div style='float: ${trial.posicion};'>
                        <img src="${trial.imagen}" width="200" height="200"></img>
                    </div>
                </div>`
            }else{
                html_content = `
                    <div style='${trial.posicion}: -150px; position: relative'>
                        <img src="${trial.imagen}" width="200" height="200"></img>
                    </div>
                `
            }

            /*
            * Pasamos html_content a innerHTML, que es el que imprime en pantalla
            */
            display_element.innerHTML = html_content

            /*
            * Función que es llamada en callback_function al final de trial
            * Le pasamos el parámetro info, el cual tiene dos atributos,
            * key, que es la tecla presionada
            * rt, que es el tiempo que le tomo presionarla 
            */
            const after_key_response = (info) => {
                //Limpiamos innehHTML manualmente
                display_element.innerHTML = '';

                //Variable que nos dice si se apreto la tecla correcta
                var correcto = null;

                /*
                * Valor que guarda la tecla relacionada con la posicion
                * si la posicion es top, la llave es w
                * posicion bottom, la llave es s
                * posicion right, la llave es d
                * posicion left, la llave es a
                */
                var llave = '';

                /*
                * Preguntamos la posicion, y con respecto a eso, declaramos la llave
                */
                if(trial.posicion == "top"){
                    llave = 'w';
                }else if(trial.posicion == "bottom"){
                    llave = 's';
                }else if(trial.posicion == "right"){
                    llave = 'd';
                }else if(trial.posicion == "left"){
                    llave = 'a';
                }

                /*
                * this.jsPsych.pluginAPI.compareKeys es un método que compara
                * dos strings, en este caso, la llave que es la respuesta correcta
                * e info.key, que es la tecla que el usuario presiono
                */
                correcto = this.jsPsych.pluginAPI.compareKeys(llave, info.key);

                /*
                * Objeto data que pasaremos al archivo csv
                * rt, el tiempo que le tomo responder
                * correcto, si el particiapnte acerto 
                */
                let data = {
                    rt: info.rt,
                    correcto: correcto,
                }

                //Imprime información en terminal, no afecta la lógica
                console.log(info.rt);
                console.log(correcto);

                /*
                * Final de la función, pasamos nuestro objeto data
                */
                this.jsPsych.finishTrial(data);
            }

            /*
            * Final del método trial, en este caso, se espera una respuesta 
            * del teclado
            */
            this.jsPsych.pluginAPI.getKeyboardResponse({
                callback_function: after_key_response, //función que se llama al final
                valid_responses: ['w','a','s','d'], //teclas que el participante puede presionar
                persist: false,});  //persist en false, hace que el programa siga con el programa con
                                    //la primer tecla válida

        }

    }

    //Final de plugin
    Imagen.info = info;

    return Imagen;
    
})(jsPsychModule)