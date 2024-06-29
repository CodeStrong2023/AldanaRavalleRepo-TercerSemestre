# Bunny Buddy - Juego de Cuidado de Mascota

Bunny Buddy es un juego inspirado en los clásicos Tamagotchi, donde el jugador cuida a una carismática mascota virtual. El objetivo es mantener feliz y saludable a la mascota atendiendo sus necesidades básicas como alimentación, descanso y limpieza.

## Características del Juego

### Tecnologías Utilizadas
El juego está desarrollado en Python, utilizando la biblioteca Pygame para la interfaz gráfica y la interactividad.

### Funcionalidades Principales

#### Interfaz Gráfica
- Un menú principal permite al jugador iniciar el juego, acceder a la ayuda y salir.
- Durante el juego, se puede acceder a opciones de alimentar, descansar y limpiar al Bunny utilizando el ratón o el teclado.

#### Cuidado del Bunny
- **Alimentación:** Mantén el nivel de comida del Bunny adecuado.
- **Descanso:** Asegúrate de que el Bunny duerma lo suficiente para mantener su energía.
- **Limpieza:** Limpia al Bunny para mantenerlo feliz y saludable.

#### Base de Datos
- Utiliza PostgreSQL para almacenar y recuperar datos del estado del Bunny.
- Cada acción del jugador se refleja en la base de datos para mantener un registro preciso del progreso y estado del juego.

#### Ciclo de Vida del Bunny
- El Bunny tiene un ciclo de vida simulado donde debe ser cuidado constantemente para evitar que se enferme o muera.
- Se actualiza visualmente con diferentes imágenes que reflejan su etapa de vida.

---

# Código del Juego

El código es un juego interactivo implementado en Python con la biblioteca Pygame, que simula cuidar a un Tamagotchi virtual llamado "Bunny Buddy". A continuación se explica cada parte del código:

## Cómo Ejecutar el Juego

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las bibliotecas de pygame y postgresql. 
3. Ejecuta `python main.py` para iniciar el juego.

## 1. Inicialización y Configuración

El juego comienza inicializando Pygame y estableciendo la configuración básica, como el tamaño de la ventana (`ANCHO` y `ALTO`), el título de la ventana y los colores utilizados en la interfaz.

## 2. Conexión a la Base de Datos

Se establece una conexión a una base de datos PostgreSQL donde se almacenan y recuperan los datos del juego. La función `conectar_db()` maneja la conexión y la creación de la tabla si no existe (`crear_tabla()`). Además, permite insertar y recuperar datos del estado inicial del Tamagotchi (`get_initial_data()`).

## 3. Clase Tamagotchi

La clase `Tamagotchi` encapsula el estado y el comportamiento del personaje principal del juego:

- **Atributos:** `comer`, `dormir`, `limpieza` representan los niveles de necesidades básicas del Tamagotchi.
- **Métodos:** `alimentar()`, `descansar()`, `limpiar_tamagotchi()` permiten modificar estas necesidades.
- **Métodos de actualización:** `actualizar()` y `calcular_tiempo_vivo()` actualizan el estado del Tamagotchi según el paso del tiempo y determinan cuánto tiempo ha estado vivo.

## 4. Carga de Recursos

La función `cargar_recursos()` carga imágenes de fondo, menú y ayuda, así como imágenes de diferentes apariencias del Tamagotchi. También carga y reproduce música de fondo utilizando Pygame Mixer.

## 5. Funciones de Dibujo y Animación

- **Funciones de Dibujo:** `dibujar_barra()` y `dibujar_barras(tamagotchi)` se utilizan para dibujar barras que representan las necesidades del Tamagotchi en la pantalla de juego.
- **Función de Animación:** `actualizar_fondo(x_fondo1, x_fondo2, velocidad_fondo)` maneja la animación del fondo desplazándolo horizontalmente.

## 6. Gestión de Pantallas y Eventos

- **Mostrar Pantallas:** `mostrar_menu()`, `mostrar_help()`, y `mostrar_play()` muestran respectivamente las pantallas de menú, ayuda y juego principal en la ventana de Pygame.
- **Gestión de Eventos:** El bucle principal del juego maneja eventos de usuario como clics del ratón para interactuar con botones del menú, tecla Escape para volver al menú, y la función `pygame.event.get()` para manejar eventos de cierre de ventana.

## 7. Bucle Principal del Juego

El bucle principal (`while ejecutando:`) gestiona el ciclo de vida del juego:

- Controla la ejecución del juego (`ejecutando = True`) y maneja eventos de usuario.
- Actualiza la posición del fondo y la pantalla que se muestra según el estado (`pantalla_actual`).
- Llama a funciones para dibujar elementos en la pantalla y actualizar el estado del Tamagotchi en tiempo real.

## 8. Cierre del Juego

Cuando el usuario decide cerrar la ventana (`pygame.QUIT`) o salir del juego (`ejecutando = False`), se termina Pygame limpiamente (`pygame.quit()`) y se finaliza el programa (`sys.exit()`).

---

# Créditos

Desarrollado por Aldana Ravalle como parte de un proyecto de aprendizaje en programación de Python.

## Contribuciones y Mejoras

¡Bienvenido a contribuir al proyecto! Si tienes ideas para mejorar el juego o encuentras problemas, puedes crear un pull request o reportar un issue en el [repositorio](https://github.com/tu_usuario/bunny-buddy).

---
