
// While - Mientras
let contadorA = 0;

while (contadorA < 3) {
    console.log(contadorA);
    contadorA++;
}

console.log("Fin del ciclo while")

// Do While - Hacer mientras 
let contadorB = 0;

do {
    console.log(contadorB);
    contadorB++;
} while (contadorB < 3);

console.log("Fin del ciclo do while")

// Ciclo for - Para
for(let contadorC = 0; contadorC < 3; contadorC++){
    console.log(contadorC);
}

console.log("Fin del ciclo for")

// Palabra reservada Break
for(let contadorD = 0; contadorD <= 10; contadorD++){
    if(contadorD % 2 == 0){
        console.log(contadorD); // Se muestran los numeros pares
        break; // Solo va a mostrar el primer número par
    }
}
console.log("Fin del ciclo, se encontró el primer número par")

// Palabra reservada Continue
for(let contadorE = 0; contadorE <= 10; contadorE++){
    if(contadorE % 2 !== 0){
        continue; // Continua a la siguiente iteración
    }
    console.log(contadorE);
}
console.log("Fin del ciclo")

// Etiquetas labels - no se recomienda su uso
inicio:
for(let contadorE = 0; contadorE <= 10; contadorE++){
    if(contadorE % 2 !== 0){
        continue inicio; // Tambien se puede usar con break
    }
    console.log(contadorE);
}
console.log("Fin del ciclo")
