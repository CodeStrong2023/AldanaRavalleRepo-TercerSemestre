let x = 10; // Vatiable primitiva
console.log(x.length);

console.log('TIPOS PRIMITIVOS');
// Objeto
let persona = {
    // Atributos
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    idioma: 'es',
    
    // metodos o funciones
    get lang(){
        return this.idioma.toUpperCase() // Convierte a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    
    nombreCompleto: function(){
        return this.nombre +' '+this.apellido;
    },
    get nombreEdad(){
        return 'El nombre es '+this.nombre+' . Edad, '+this.edad;
    }
}
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto())


console.log('EJECUTANDO CON UN OBJETO');
let persona2 = new Object(); // crea un nuevo objeto
persona2.nombre = 'Juan';
persona2.direccion = 'salada 14';
persona2.telefono = 123456789;
console.log(persona2.telefono);


console.log('CREAMOS UN NUEVO OBJETO');
console.log(persona['apellido']); // se accede como si fuera un arreglo

console.log('USAMOS EL CICLO FOR IN');
for(propiedad in persona){ 
    console.log(propiedad);
    console.log(persona[propiedad]);
}


console.log('CAMBIAMOS Y ELIMINAMOS UN ERROR');
persona.apellida = 'Betancud'; // cambiar dinamicamente el valor de un objeto
delete persona.apellida; // eliminar un error
console.log(persona);


console.log('DISTINTAS FORMAS DE IMPRIMIR UN OBJETO - 1');
// Numero 1, concatenar cada valor
console.log(persona.nombre+', '+persona.apellido);

console.log('DISTINTAS FORMAS DE IMPRIMIR UN OBJETO - 2');
// numero 2, con un ciclo for in
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

console.log('DISTINTAS FORMAS DE IMPRIMIR UN OBJETO - 3');
// Numero 3, la funcion Objet.values()
let personaArray = Object.values(persona);
console.log(personaArray)

console.log('DISTINTAS FORMAS DE IMPRIMIR UN OBJETO - 4');
// Numero 4, metodo JSON.stringify
let personaString = JSON.stringify(persona);
console.log(personaString); 

console.log('Comenzamos a usar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

// Crear una funcion
function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Mario';
padre.telefono = '123456789';
console.log(padre.nombreCompleto())
console.log(padre);

let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono);
console.log(madre.nombreCompleto())

// Diferentes formas de crear objetos

// caso objeto 1 - Sintaxis formal
let miObjeto1 = new Object();

// caso objeto 2 - Sintaxis simplificada y recomendada
let miObjeto2 = {};

// caso String 1 - Sintaxis formal
let miCadena1 = new String('Hola');

// caso String 2 - Sintaxis simplificada y recomendada
let miCadena2 = 'Hola';

// caso numeros 1 - Sintaxis formal
let miNumero1 = new Number(1);

// caso numeros 2 - Sintaxis simplificada y recomendada
let miNumero2 = 1;

//caso boolean 1  - Sintaxis formal
let miBoolean1 = new Boolean(false);

//caso boolean 2  - Sintaxis simplificada y recomendada
let miBoolean2 = false;

//caso Arreglos 1  - Sintaxis formal
let miArreglo1 = new Array();

//caso Arreglos 2  - Sintaxis simplificada y recomendada
let miArreglo2 = [];

//caso function 1  - Sintaxis formal
let miFuncion1 = new function(){};

//caso function 2  - Sintaxis simplificada y recomendada
let miFuncion2 = function(){};

// Uso de prototype
Persona3.prototype.telefono = '987654321';
console.log(padre);
console.log(madre);
madre.telefono = '789456123';
console.log(madre);

// Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+'. '+this.nombre+' '+this.apellido+' '+telefono;
    }
}
let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara',
}
console.log(persona4.nombreCompleto2('Lic', '123456789'))
console.log(persona4.nombreCompleto2.call(persona5, 'Ing', '321654987'));

// Metodo Apply
let arreglo = ['Ing', '321654987'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
