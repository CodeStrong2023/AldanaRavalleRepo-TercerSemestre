// Declaración de variables globales para almacenar los ataques del jugador y del enemigo
let ataqueJugador
let ataqueEnemigo

// Función para inicializar el juego y agregar los escuchadores de eventos
function iniciarJuego(){
    // Obtenemos el botón de selección de personaje y le agregamos un escuchador de eventos
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    // Obtenemos los botones de ataque y les agregamos escuchadores de eventos
    let botonGolpe = document.getElementById('boton-golpe')
    botonGolpe.addEventListener('click', ataqueGolpe)
    let botonPatada = document.getElementById('boton-patada')
    botonPatada.addEventListener('click', ataquePatada)
    let botonBarrida = document.getElementById('boton-barrida')
    botonBarrida.addEventListener('click', ataqueBarrida)
}

// Función para seleccionar el personaje del jugador
function seleccionarPersonajeJugador(){
    // Obtenemos los inputs de selección de personaje y el elemento para mostrar el personaje del jugador
    let inputZuko = document.getElementById('zuko')
    let inputKatara = document.getElementById('katara')
    let inputAang = document.getElementById('aang')
    let inputToph = document.getElementById('toph')
    let spanPersonajeJugador = document.getElementById('personaje-jugador')

    // Verificamos qué personaje fue seleccionado y actualizamos el elemento correspondiente
    if(inputZuko.checked){
        spanPersonajeJugador.innerHTML = 'Zuko'
    }else if(inputKatara.checked){
        spanPersonajeJugador.innerHTML = 'Katara'
    }else if(inputAang.checked){
        spanPersonajeJugador.innerHTML = 'Aang'
    }else if(inputToph.checked){
        spanPersonajeJugador.innerHTML = 'Toph'
    }else{
        alert('Selecciona un personaje') // Mensaje de alerta si no se selecciona ningún personaje
    }
    seleccionarPersonajeEnemigo() // Seleccionamos el personaje enemigo de forma aleatoria
}

// Función para seleccionar el personaje enemigo de forma aleatoria
function seleccionarPersonajeEnemigo(){
    // Generamos un número aleatorio para determinar el personaje enemigo
    let personajeAleatorio = aleatorio(1, 4)
    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo')

    // Asignamos el personaje enemigo basado en el número aleatorio
    if(personajeAleatorio == 1){
        spanPersonajeEnemigo.innerHTML = 'Zuko'
    } else if(personajeAleatorio == 2){
        spanPersonajeEnemigo.innerHTML = 'Katara'
    } else if(personajeAleatorio == 3){
        spanPersonajeEnemigo.innerHTML = 'Aang'
    } else {
        spanPersonajeEnemigo.innerHTML = 'Toph'
    }
}

// Función para manejar el ataque de Golpe del jugador
function ataqueGolpe(){
    ataqueJugador = 'Golpe' // Asignamos el ataque del jugador
    ataqueAleatorioEnemigo() // Determinamos el ataque del enemigo de forma aleatoria
}

// Función para manejar el ataque de Patada del jugador
function ataquePatada(){
    ataqueJugador = 'Patada' // Asignamos el ataque del jugador
    ataqueAleatorioEnemigo() // Determinamos el ataque del enemigo de forma aleatoria
}

// Función para manejar el ataque de Barrida del jugador
function ataqueBarrida(){
    ataqueJugador = 'Barrida' // Asignamos el ataque del jugador
    ataqueAleatorioEnemigo() // Determinamos el ataque del enemigo de forma aleatoria
}

// Función para determinar el ataque del enemigo de forma aleatoria
function ataqueAleatorioEnemigo(){
    let ataqueAleatorio = aleatorio(1, 3) // Generamos un número aleatorio para el ataque

    // Asignamos el ataque del enemigo basado en el número aleatorio
    if(ataqueAleatorio == 1){
        ataqueEnemigo = 'Golpe'
    } else if(ataqueAleatorio == 2){
        ataqueEnemigo = 'Patada'
    } else {
        ataqueEnemigo = 'Barrida'
    }
}

// Función para generar un número aleatorio entre un mínimo y un máximo
function aleatorio(min, max){
    return Math.floor( Math.random() * (max - min + 1) + min)
}

// Agregamos un escuchador de eventos para iniciar el juego cuando la ventana se carga
window.addEventListener('load', iniciarJuego)
