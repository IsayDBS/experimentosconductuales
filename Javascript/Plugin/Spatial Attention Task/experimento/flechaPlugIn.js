/*
* Plugin personalizado que muestra una flecha apuntando a una dirección, 
* ya sea arriba, abajo, derecha o izquierda.
* El nombre de nuestro plugin es jsFlecha
*/
var jsFlecha = (function (jspsych){
    "use strict"

    /*
    * Decidimos el nombre del plugin que aparecerá en el csv
    * junto con los parámetros que recibirá, en este caso
    * la direccion, siendo un número del 0 al 4
    * 0 : arriba
    * 1 : abajo
    * 2 : derecha
    * 3 : izquierda
    * Al agregar un valor en default, podemos no pasarle este parametro
    */
    const info = {
        name: 'Flecha',
        parameters:{
            direccion: { //posicion de la imagen
                type: jspsych.ParameterType.INT,
                default: -1,
            }
        }
    }

    class Flecha{

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

            //Lista con las flechas aputando en diferentes direcciones
            let arrows =  ['↑','↓' ,'→',' ←'];

            /*
            * Guardamos la direccion, que es un parámetro de nuestro plugin
            * lo llamamos utilizando la el objeto trial
            */
            var flecha = trial.direccion;

            /*
            * Preguntamos si la dirección es -1, es decir, si el programador no
            * le paso ningún valor.
            */
            if(flecha == -1){
                //Elige un numero entre 0 y 3
                flecha = Math.floor(Math.random()*4)
            }

            /*
            * Creamos una variable que guardará un string con código html
            * el cual se lo pasaremos al objeto display_element
            */
            var html_content = `
            <div style="font-size: 50px;">
                <p>${arrows[flecha]}</p>   
            </div>
            `
            /*
            * Imprime en terminal del navegador la variable html_content
            * No tiene efectos en la lógica del plugin si se quita
            */
            console.log(html_content);

            /*
            * Le damos el valor de la variable html_content al atributo
            * inneHTML del objeto display_element, y es este el que imprime
            * en pantalla.
            */
            display_element.innerHTML = html_content;

            /*
            * Final de método trial
            * En este caso, se esperará 2000 ms
            */
            this.jsPsych.pluginAPI.setTimeout(() =>{
                //Limpia aspectos técnicos del pluginAPI, SIEMPRE es necesario.
                this.jsPsych.pluginAPI.clearAllTimeouts();

                //innerHTML SIEMPRE debe ser limpiado a mano, por lo que lo ponemos a ""
                display_element.innerHTML = "";

                /*
                * Objeto trial_data, este es un objeto que pasa información relevante del plugin
                * En este caso, pasamos el tiempo que le tomo al plugin que son 2000 a rt
                * Y pasamos la flecha que se utilizó en este plugin
                */
                var trial_data = {
                    rt: info.rt,
                    arrow: arrows[flecha],
                };
    
                /*
                * Finalizamos el plugin, pasamos el objeto creado anteriormente como parámetro
                */
                this.jsPsych.finishTrial(trial_data);
            }, 2000);

        }

    }

    //Final del plugin
    Flecha.info = info;

    return Flecha;
    
})(jsPsychModule)