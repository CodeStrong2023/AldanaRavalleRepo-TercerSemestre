// let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer: Persona is not defined

class Persona { // Clase padre

    static contadorPersonas = 0; // Atributo perteneciente a la clase y no a un objeto
    email = 'Valor default email'; // Atributo no estatico

    static get MAX_OBJ() { // simula una constante
        return 5; // Maximo de objetos que se pueden crear de la clase persona
    }

    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
        if (Persona.contadorPersonas < Persona.MAX_OBJ) {
            this.idPersona = ++Persona.contadorPersonas;
        }
        else {
            console.log('Se ha superado el maximo de objetos permitidos');
        }

    }

    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }

    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }

    nombreCompleto() {
        return this.idPersona + ' ' + this._nombre + ' ' + this._apellido;
    }

    // Sobreescribir el metodo de la clase padre (Objet)
    toString() {
        // Se aplica polimorfismo, el metodo se ejecuta dependiendo de el objeto (Padre o Hija)
        return this.nombreCompleto();
    }

    static saludar1() {
        console.log('Saludos desde el metodo static');
    }

    static saludar2(persona) {
        console.log(persona.nombre + ' ' + persona.apellido);
    }
}

class Empleado extends Persona { // Clase hija
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }

    // Sobreescritura
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;;
    }
}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);

persona1.nombre = 'Juan';
console.log(persona1.nombre);

persona1.apellido = 'Martinez';
console.log(persona1.apellido);

let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);

persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);

persona2.apellido = 'Gonzalez';
console.log(persona2.apellido);

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

// Object.prototype.toString -> acceder a metodos y atributos de forma dinamica
console.log(empleado1.toString());
console.log(persona1.toString());

// persona1.saludar(); no se puede utilizar desde el objetp
Persona.saludar1();
Persona.saludar2(persona1);

Empleado.saludar1();
Empleado.saludar2(empleado1);

// console.log(persona1.contadorPersonas);
console.log(Persona.contadorPersonas);
console.log(Empleado.contadorPersonas);

console.log(persona1.email);
console.log(empleado1.email);
//console.log(Persona.email); no se puede acceder desde la clase
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);

let persona3 = new Persona('Carla', 'Pertosi');
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);
// Persona.MAX_OBJ = 10; -> no se puede modificar el MAX.OBJ

let persona4 = new Persona('Franco', 'Diaz');
console.log(persona4.toString());

let persona5 = new Persona('Liliana', 'Paz');
console.log(persona5.toString());