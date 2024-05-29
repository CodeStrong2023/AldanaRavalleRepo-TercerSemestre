function seleccionarPersonajeJugador(){
    let personajeSeleccionado = document.querySelector('input[name="personaje"]:checked');

    if (personajeSeleccionado) {
        let nombrePersonaje = document.querySelector('label[for="' + personajeSeleccionado.id + '"]').innerText;
        alert('SELECCIONASTE A: ' + nombrePersonaje);
    } else {
        alert('Debes seleccionar un personaje antes de continuar.');
    }
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
