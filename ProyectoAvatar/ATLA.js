// Variables globales para el juego
let ataqueJugador; // Almacena el tipo de ataque seleccionado por el jugador
let ataqueEnemigo; // Almacena el tipo de ataque seleccionado por el enemigo
let vidasJugador = 3; // Vidas del jugador
let vidasEnemigo = 3; // Vidas del enemigo

// Función para inicializar el juego
function iniciarJuego() {
    // Ocultar secciones no necesarias al inicio
    const sectionSeleccionarAtaque = document.getElementById('seleccionar-ataque');
    sectionSeleccionarAtaque.style.display = 'none';

    const sectionSeleccionarPersonaje = document.getElementById('seleccionar-personaje');
    sectionSeleccionarPersonaje.style.display = 'none';

    const sectionReglas = document.getElementById('reglas-del-juego');
    sectionReglas.style.display = 'none';

    const sectionReiniciar = document.getElementById('reiniciar');
    sectionReiniciar.style.display = 'none';

    // Configuración de eventos para botones
    const botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    const botonGolpe = document.getElementById('boton-golpe');
    botonGolpe.addEventListener('click', () => { ataqueGolpe(); combate(); });

    const botonPatada = document.getElementById('boton-patada');
    botonPatada.addEventListener('click', () => { ataquePatada(); combate(); });

    const botonBarrida = document.getElementById('boton-barrida');
    botonBarrida.addEventListener('click', () => { ataqueBarrida(); combate(); });

    const botonReiniciar = document.getElementById('boton-reiniciar');
    botonReiniciar.addEventListener('click', reiniciarJuego);

    const botonJugar = document.getElementById('boton-jugar');
    botonJugar.addEventListener('click', comenzarJuego);

    const botonReglas = document.getElementById('boton-reglas');
    botonReglas.addEventListener('click', mostrarReglas);
}

// Función para comenzar el juego
function comenzarJuego() {
    const sectionSeleccionarPersonaje = document.getElementById('seleccionar-personaje');
    sectionSeleccionarPersonaje.style.display = 'block';

    const sectionInicio = document.getElementById('Inicio');
    sectionInicio.style.display = 'none';
}

// Función para mostrar las reglas del juego
function mostrarReglas() {
    const sectionReglas = document.getElementById('reglas-del-juego');
    sectionReglas.style.display = 'block';

    const sectionInicio = document.getElementById('Inicio');
    sectionInicio.style.display = 'none';
}

// Función para seleccionar el personaje del jugador
function seleccionarPersonajeJugador() {
    const inputZuko = document.getElementById('zuko');
    const inputKatara = document.getElementById('katara');
    const inputAang = document.getElementById('aang');
    const inputToph = document.getElementById('toph');
    const spanPersonajeJugador = document.getElementById('personaje-jugador');

    // Verificar qué personaje ha sido seleccionado por el jugador
    if (inputZuko.checked) {
        spanPersonajeJugador.innerHTML = 'Zuko';
    } else if (inputKatara.checked) {
        spanPersonajeJugador.innerHTML = 'Katara';
    } else if (inputAang.checked) {
        spanPersonajeJugador.innerHTML = 'Aang';
    } else if (inputToph.checked) {
        spanPersonajeJugador.innerHTML = 'Toph';
    } else {
        alert('Por favor, selecciona un personaje');
        return;
    }

    // Seleccionar automáticamente el personaje enemigo
    seleccionarPersonajeEnemigo();

    // Ocultar la sección de selección de personaje y mostrar la de selección de ataque
    document.getElementById('seleccionar-personaje').style.display = 'none';
    document.getElementById('seleccionar-ataque').style.display = 'block';
}

// Función para seleccionar el personaje enemigo de manera aleatoria
function seleccionarPersonajeEnemigo() {
    const personajes = ['Zuko', 'Katara', 'Aang', 'Toph'];
    const personajeJugador = document.getElementById('personaje-jugador').innerHTML;
    const personajesRestantes = personajes.filter(personaje => personaje !== personajeJugador);
    const personajeEnemigo = personajesRestantes[Math.floor(Math.random() * personajesRestantes.length)];
    document.getElementById('personaje-enemigo').innerHTML = personajeEnemigo;
}

// Funciones para registrar los ataques seleccionados por el jugador
function ataqueGolpe() {
    ataqueJugador = 'Golpe';
}

function ataquePatada() {
    ataqueJugador = 'Patada';
}

function ataqueBarrida() {
    ataqueJugador = 'Barrida';
}

// Función para que el enemigo seleccione un ataque aleatorio
function seleccionarAtaqueEnemigo() {
    const ataques = ['Golpe', 'Patada', 'Barrida'];
    ataqueEnemigo = ataques[Math.floor(Math.random() * ataques.length)];
}

// Función principal para resolver el combate
function combate() {
    seleccionarAtaqueEnemigo(); // Seleccionar el ataque del enemigo

    const spanVidasJugador = document.getElementById('vidas-jugador');
    const spanVidasEnemigo = document.getElementById('vidas-enemigo');
    const sectionMensajes = document.getElementById('mensajes');

    let resultado = '';
    // Determinar el resultado del combate
    if (ataqueJugador === ataqueEnemigo) {
        resultado = 'Empate';
    } else if ((ataqueJugador === 'Golpe' && ataqueEnemigo === 'Barrida') ||
               (ataqueJugador === 'Patada' && ataqueEnemigo === 'Golpe') ||
               (ataqueJugador === 'Barrida' && ataqueEnemigo === 'Patada')) {
        resultado = 'Ganaste';
        vidasEnemigo--;
    } else {
        resultado = 'Perdiste';
        vidasJugador--;
    }

    // Actualizar la visualización de vidas y mensajes de combate
    spanVidasJugador.innerHTML = vidasJugador;
    spanVidasEnemigo.innerHTML = vidasEnemigo;
    sectionMensajes.innerHTML = `<p>Tu personaje atacó con ${ataqueJugador}, el personaje del enemigo atacó con ${ataqueEnemigo} - ${resultado} 🎉</p>`;

    // Verificar si alguien ha perdido todas sus vidas
    revisarVidas();
}

// Función para verificar el estado de las vidas después de un combate
function revisarVidas() {
    if (vidasJugador === 0) {
        mostrarMensajeFinal('Perdiste el juego. ¡Intenta de nuevo!');
    } else if (vidasEnemigo === 0) {
        mostrarMensajeFinal('Ganaste el juego. ¡Felicidades!');
    }
}

// Función para mostrar el mensaje final del juego
function mostrarMensajeFinal(mensaje) {
    const sectionMensajes = document.getElementById('mensajes');
    sectionMensajes.innerHTML += `<p>${mensaje}</p>`;

    // Deshabilitar botones de ataques y mostrar botón de reiniciar
    document.getElementById('boton-golpe').disabled = true;
    document.getElementById('boton-patada').disabled = true;
    document.getElementById('boton-barrida').disabled = true;
    document.getElementById('reiniciar').style.display = 'block';
}

// Función para reiniciar el juego (recarga la página)
function reiniciarJuego() {
    location.reload();
}

// Evento que se dispara cuando el contenido del DOM ha sido completamente cargado
window.addEventListener('DOMContentLoaded', iniciarJuego);
