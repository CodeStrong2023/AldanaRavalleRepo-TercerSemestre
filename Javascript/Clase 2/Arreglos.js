
// Creacion de arrays
// let autos = new Array('Ferrari', 'Renault', 'BMW') -> Sintaxis vieja para definir array
const autos = ['Ferrari', 'Renault', 'BMW']; // Sintaxis para definir array
console.log(autos);


// Recorrer los elementos del arreglo
console.log(autos[0]);
console.log(autos[2]);
for(let i = 0; i < autos.length; i++){
    console.log(i + ' ' + autos[i]);
}


// Modificar los elementos del arreglo
autos[1] = 'Volvo';
console.log(autos[1]);


// Agregar elementos al array
autos.push('Audi'); // Primera forma de agregar elementos
console.log(autos);

autos[autos.length] = 'Porche'; // Segunda forma de agregar elementos
console.log(autos);

autos[5] = 'Renault'; // Tercera foema de agregar elementos
console.log(autos);


// Identificar un array
console.log(Array.isArray(autos));
console.log(autos instanceof Array);