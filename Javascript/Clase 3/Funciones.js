
miFuncion(8, 2); // hoisting

function miFuncion(a, b){
    //Cuerpo de la funcion
    // console.log('Suma: '+ (a+b) );
    return a + b; // Javascript 'agrega' la palabra return por defecto, aunque no este en el codigo
}

// LLamar a la funcion
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

// Declaramos una funcion de tipo expreción o anónima
let x = function(a, b){return a + b};
resultado = x(5, 6); // Para llamarla se usa la variable y el parentesis
console.log(resultado);

// Funciones de tipo self y invoking - no se puede reutilizar
(function(a,b){
    console.log('Ejecutando la funcion: '+ (a + b));
}) (9,6);


console.log(typeof miFuncion);
function miFuncionDos(a, b){ // (Perametros)
    console.log(arguments.length);
}

miFuncionDos(5, 7); //(Argumentos)

// toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

// Funciones flecha - no se usa la palabra function, return ni las {}
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7);
console.log(resultado);

let sumar = function(a = 4, b = 8){
    console.log(arguments[0]); // Solo muestra el parametro de 'a'
    console.log(arguments[1]); // Solo muestra el parametro de 'b'
    console.log(arguments[2]); // no es necesario que la cantidad de argumentos y parametros coincidan
    return a + b + arguments[2];
}
resultado = sumar(3, 6, 9)
console.log(resultado);

// sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; // arguments es para arreglos
    }
    return suma;
}

// Tipos primitivos
let k = 10;
function cambiarValor(a){ // Paso por valor
    a = 20;
}

cambiarValor(k);
console.log(k);

// Paso por referencia
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona)
function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}

cambiarValorObjeto(persona);
console.log(persona);