function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function eleccion(jugada) {
    switch(jugada) {
        case 1:
            return "Piedra ✊";
        case 2:
            return "Papel 🖐️";
        case 3:
            return "Tijera ✌️";
        default:
            return "Elegiste perder 💀";
    }
}

let triunfos = 0;
let perdidas = 0;

function jugar(jugador) {
    const pc = aleatorio(1, 3);

    // Mostrar la elección de los jugadores
    document.getElementById("pc-eleccion").innerText = "PC elige: " + eleccion(pc);
    document.getElementById("jugador-eleccion").innerText = "Tú eliges: " + eleccion(jugador);

    // Combate
    let resultado = "";
    if (pc === jugador) {
        resultado = "EMPATE";
    } else if (
        (jugador === 1 && pc === 3) || // piedra vs tijera
        (jugador === 2 && pc === 1) || // papel vs piedra
        (jugador === 3 && pc === 2)    // tijera vs papel
    ) {
        resultado = "GANASTE";
        triunfos += 1;
    } else {
        resultado = "PERDISTE";
        perdidas += 1;
    }
    document.getElementById("resultado").innerText = resultado;
    document.getElementById("marcador").innerText = `GANASTE ${triunfos} VECES | PERDISTE ${perdidas} VECES`;

    // Verificar si alguien ganó 3 veces
    if (triunfos === 3 || perdidas === 3) {
        triunfos = 0;
        perdidas = 0;
        document.getElementById("marcador").innerText = '';
    }
}