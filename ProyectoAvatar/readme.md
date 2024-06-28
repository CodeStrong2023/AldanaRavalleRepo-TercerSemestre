# Avatar: La Leyenda de Aang - Juego Interactivo

Este proyecto es un juego interactivo basado en la serie "Avatar: La Leyenda de Aang", donde los jugadores pueden seleccionar un personaje y enfrentarse en combate estratégico contra un enemigo asignado aleatoriamente.

Este juego fue creado dentro del marco de la clase Programacion III inspirado en la serie animada "Avatar: La Leyenda de Aang".

## Funciones del Código

### HTML

El archivo `ATLA.html` define la estructura del juego y utiliza elementos como botones, secciones para reglas y mensajes, y contenedores para mostrar personajes y vidas.

### CSS

El archivo `ATLA.css` proporciona los estilos visuales para el juego, incluyendo diseño responsivo, animaciones para imágenes de personajes, y estilización de botones y secciones.

### JavaScript (`ATLA.js`)

#### Variables Globales

- `ataqueJugador`: Almacena el tipo de ataque seleccionado por el jugador.
- `ataqueEnemigo`: Almacena el tipo de ataque seleccionado aleatoriamente por el enemigo.
- `vidasJugador`: Contador de vidas restantes del jugador.
- `vidasEnemigo`: Contador de vidas restantes del enemigo.

#### Funciones Principales

- `iniciarJuego()`: Configura los eventos de click para los botones y oculta secciones no necesarias inicialmente.
  
- `comenzarJuego()`: Muestra la sección de selección de personaje y oculta la pantalla de inicio.

- `mostrarReglas()`: Muestra la sección de reglas del juego y oculta la pantalla de inicio.

- `seleccionarPersonajeJugador()`: Gestiona la selección de personaje por parte del jugador, mostrando el nombre del personaje seleccionado y ocultando la sección de selección de personaje.

- `seleccionarPersonajeEnemigo()`: Elige aleatoriamente un personaje enemigo entre los restantes después de que el jugador haya seleccionado su personaje.

- `ataqueGolpe()`, `ataquePatada()`, `ataqueBarrida()`: Estas funciones actualizan `ataqueJugador` con el tipo de ataque seleccionado por el jugador.

- `seleccionarAtaqueEnemigo()`: Elige aleatoriamente un ataque para el enemigo entre Golpe, Patada o Barrida.

- `combate()`: Compara los ataques seleccionados por el jugador y el enemigo, actualiza las vidas según el resultado y muestra mensajes de combate en la sección de mensajes.

- `revisarVidas()`: Verifica si el jugador o el enemigo han perdido todas sus vidas y muestra un mensaje final correspondiente.

- `mostrarMensajeFinal(mensaje)`: Muestra un mensaje final en la sección de mensajes indicando si el jugador ganó o perdió, y desactiva los botones de ataque y muestra el botón de reinicio.

- `reiniciarJuego()`: Recarga la página para reiniciar el juego desde cero.

#### Event Listeners

- Los eventos de click están asignados a los botones relevantes (selección de personaje, selección de ataques, reiniciar juego) para activar las funciones correspondientes.

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local.
2. Abre el archivo `ATLA.html` en tu navegador web.
3. Selecciona tu personaje y comienza a jugar haciendo clic en "Jugar".
4. Elige tus ataques y observa el resultado del combate en la pantalla.
5. Intenta derrotar al enemigo antes de que pierdas todas tus vidas.


