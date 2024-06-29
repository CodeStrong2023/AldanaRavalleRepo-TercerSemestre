import pygame
import sys
import time
import psycopg2

# Inicialización de Pygame
pygame.init()

# Función para establecer la conexión a la base de datos
def conectar_db():
    try:
        # Intentar conectar a la base de datos PostgreSQL con los parámetros especificados
        conn = psycopg2.connect(
            dbname="DatabaseBunnyBuddy",  # Nombre de la base de datos
            user="postgres",              # Usuario de PostgreSQL
            password="admin",             # Contraseña de PostgreSQL
            host="localhost",             # Host donde está corriendo PostgreSQL
            port="5432"                   # Puerto por defecto de PostgreSQL
        )
        print("Conexión exitosa a PostgreSQL")
        return conn  # Devolver la conexión si es exitosa
    except psycopg2.Error as e:
        # Imprimir un mensaje de error si la conexión falla y salir del programa
        print("Error al conectar a PostgreSQL:", e)
        sys.exit(1)

# Función para crear la tabla en la base de datos si no existe
def crear_tabla(conn):
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar comandos SQL
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS "TableBunnyBuddy" (
                id SERIAL PRIMARY KEY,
                comer INTEGER NOT NULL,
                dormir INTEGER NOT NULL,
                limpieza INTEGER NOT NULL,
                tiempo_vivo INTEGER NOT NULL
            );
        """)
        conn.commit()  # Confirmar los cambios en la base de datos
        print("Tabla creada o ya existe")
    except psycopg2.Error as e:
        # Imprimir un mensaje de error si la creación de la tabla falla y deshacer los cambios
        print("Error al crear la tabla:", e)
        conn.rollback()
    finally:
        cursor.close()  # Cerrar el cursor

# Función para insertar datos en la tabla
def insertar_datos(conn, comer, dormir, limpieza, tiempo_vivo):
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar comandos SQL
        cursor.execute("""
            INSERT INTO "TableBunnyBuddy" (comer, dormir, limpieza, tiempo_vivo)
            VALUES (%s, %s, %s, %s);
        """, (comer, dormir, limpieza, tiempo_vivo))
        conn.commit()  # Confirmar los cambios en la base de datos
        print("Datos insertados correctamente")
    except psycopg2.Error as e:
        # Imprimir un mensaje de error si la inserción de datos falla y deshacer los cambios
        print("Error al insertar datos:", e)
        conn.rollback()
    finally:
        cursor.close()  # Cerrar el cursor

# Función para obtener datos iniciales de la base de datos
def get_initial_data(conn):
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar comandos SQL
        cursor.execute("SELECT comer, dormir, limpieza FROM \"TableBunnyBuddy\" LIMIT 1;")
        row = cursor.fetchone()  # Obtener la primera fila del resultado
        if row:
            # Asignar los valores obtenidos a las variables
            comer, dormir, limpieza = row
        else:
            # Asignar valores por defecto si no hay datos en la tabla
            comer, dormir, limpieza = 50, 50, 50
        cursor.close()  # Cerrar el cursor
        return comer, dormir, limpieza  # Devolver los valores obtenidos
    except psycopg2.Error as e:
        # Imprimir un mensaje de error si la consulta falla y devolver valores por defecto
        print("Error al obtener datos iniciales:", e)
        return 50, 50, 50

# Establecer la conexión a la base de datos
conn = conectar_db()

# Crear la tabla si no existe
crear_tabla(conn)

# Obtener datos iniciales de la base de datos
comer, dormir, limpieza = get_initial_data(conn)


# Configuración de la ventana
ANCHO, ALTO = 800, 600  # Dimensiones de la ventana del juego (ancho y alto en píxeles)
pantalla = pygame.display.set_mode((ANCHO, ALTO))  # Crear una ventana con las dimensiones especificadas
pygame.display.set_caption('BUNNY BUDDY - ALDANA RAVALLE')  # Establecer el título de la ventana

# Definición de colores (RGB)
BLANCO = (255, 255, 255)  # Color blanco
NEGRO = (0, 0, 0)         # Color negro
ROSA = (255, 163, 177)    # Color rosa
AZUL = (117, 207, 235)    # Color azul


# Clase Tamagotchi
class Tamagotchi:
    def __init__(self, comer=50, dormir=50, limpieza=50):
        self.comer = comer                 # Nivel de comida inicial
        self.dormir = dormir               # Nivel de sueño inicial
        self.limpieza = limpieza           # Nivel de limpieza inicial
        self.vivo = False                  # Estado de vida del Tamagotchi
        self.tiempo_vivo = 0               # Tiempo total de vida del Tamagotchi
        self.tiempo_inicio = 0             # Tiempo de inicio de vida del Tamagotchi
        self.ultimo_cambio_imagen = 0      # Tiempo del último cambio de imagen
        self.contador_imagenes = 0         # Contador para el cambio de imágenes del Tamagotchi

    # Método para alimentar al Tamagotchi
    def alimentar(self):
        if self.vivo:
            self.comer = min(self.comer + 20, 100)  # Incrementa el nivel de comida sin exceder 100
            self.limpieza = max(self.limpieza - 10, 0)  # Reduce el nivel de limpieza sin bajar de 0

    # Método para hacer descansar al Tamagotchi
    def descansar(self):
        if self.vivo:
            self.dormir = min(self.dormir + 20, 100)  # Incrementa el nivel de sueño sin exceder 100
            self.comer = max(self.comer - 10, 0)  # Reduce el nivel de comida sin bajar de 0

    # Método para limpiar al Tamagotchi
    def limpiar_tamagotchi(self):
        if self.vivo:
            self.limpieza = min(self.limpieza + 20, 100)  # Incrementa el nivel de limpieza sin exceder 100
            self.dormir = max(self.dormir - 10, 0)  # Reduce el nivel de sueño sin bajar de 0

    # Método para actualizar el estado del Tamagotchi
    def actualizar(self):
        if self.vivo:
            self.comer = max(self.comer - 1, 0)  # Reduce el nivel de comida sin bajar de 0
            self.dormir = max(self.dormir - 1, 0)  # Reduce el nivel de sueño sin bajar de 0
            self.limpieza = max(self.limpieza - 1, 0)  # Reduce el nivel de limpieza sin bajar de 0

            # Si alguno de los niveles llega a 0, el Tamagotchi muere
            if self.comer == 0 or self.dormir == 0 or self.limpieza == 0:
                self.vivo = False

            tiempo_actual = time.time()  # Obtener el tiempo actual
            if tiempo_actual - self.ultimo_cambio_imagen >= 5:  # Cambiar imagen cada 5 segundos
                self.contador_imagenes = (self.contador_imagenes + 1) % len(bunny_images)  # Cambiar a la siguiente imagen
                self.ultimo_cambio_imagen = tiempo_actual  # Actualizar el tiempo del último cambio de imagen

            if tiempo_actual - self.tiempo_inicio >= 25:  # El Tamagotchi muere después de 25 segundos
                self.vivo = False

    # Método para calcular el tiempo total de vida del Tamagotchi
    def calcular_tiempo_vivo(self):
        if self.vivo:
            self.tiempo_vivo = int(time.time() - self.tiempo_inicio)  # Calcular el tiempo de vida en segundos

def cargar_recursos():
    try:
        # Cargar las imágenes de fondo, menú y ayuda
        imagenes = {
            "fondo": pygame.image.load('imagenes/pantalla/fondo.png'), #BunnyBuddyProyect/imagenes/pantalla/fondo.png
            "menu": pygame.image.load('imagenes/pantalla/menu.png'), #BunnyBuddyProyect/imagenes/pantalla/menu.png
            "help": pygame.image.load('imagenes/pantalla/help.png'), #BunnyBuddyProyect/imagenes/pantalla/help.png
        }

        # Cargar las imágenes del Tamagotchi (bunny) en una lista
        bunny_images = [pygame.image.load(f'imagenes/skins/bunny_{i}.png') for i in range(1, 6)] #BunnyBuddyProyect/imagenes/skins/bunny_{i}.png

        # Cargar y reproducir música de fondo en bucle
        pygame.mixer.music.load('audio/audio.mp3') #BunnyBuddyProyect/audio/audio.mp3
        pygame.mixer.music.play(-1)  # Reproducir música en bucle
    except pygame.error as e:
        # Si ocurre un error al cargar los recursos, imprimir el error y salir del programa
        print("Error al cargar recursos:", e)
        sys.exit()
    
    # Devolver las imágenes cargadas y la lista de imágenes del Tamagotchi
    return imagenes, bunny_images


def dibujar_barra(valor, x, y, ancho, alto, color):
    # Dibujar el contorno de la barra en blanco
    pygame.draw.rect(pantalla, BLANCO, (x, y, ancho, alto))
    # Dibujar la barra con el color correspondiente basado en el valor actual
    pygame.draw.rect(pantalla, color, (x, y, ancho * (valor / 100), alto))
    # Dibujar el borde negro alrededor de la barra
    pygame.draw.rect(pantalla, NEGRO, (x, y, ancho, alto), 2)

def dibujar_barras(tamagotchi):
    # Dibujar la barra de alimentación en la posición correspondiente
    dibujar_barra(tamagotchi.comer, 110, 77, 180, 15, AZUL)
    # Dibujar la barra de descanso en la posición correspondiente
    dibujar_barra(tamagotchi.dormir, 315, 77, 180, 15, ROSA)
    # Dibujar la barra de limpieza en la posición correspondiente
    dibujar_barra(tamagotchi.limpieza, 515, 77, 180, 15, AZUL)

def actualizar_fondo(x_fondo1, x_fondo2, velocidad_fondo):
    # Mover el fondo hacia la izquierda a la velocidad especificada
    x_fondo1 -= velocidad_fondo
    x_fondo2 -= velocidad_fondo
    # Verificar si el primer fondo ha salido de la pantalla, y reposicionarlo
    if x_fondo1 <= -ANCHO:
        x_fondo1 = ANCHO
    # Verificar si el segundo fondo ha salido de la pantalla, y reposicionarlo
    if x_fondo2 <= -ANCHO:
        x_fondo2 = ANCHO
    # Devolver las nuevas posiciones del fondo
    return x_fondo1, x_fondo2

def mostrar_menu(imagenes, x_fondo1, x_fondo2):
    # Dibujar el fondo en la posición actual del primer fondo
    pantalla.blit(imagenes["fondo"], (x_fondo1, 0))
    # Dibujar el fondo en la posición actual del segundo fondo
    pantalla.blit(imagenes["fondo"], (x_fondo2, 0))
    # Dibujar el menú en la pantalla
    pantalla.blit(imagenes["menu"], (0, 0))
    # Actualizar la pantalla para mostrar los cambios
    pygame.display.flip()

def mostrar_help(imagenes, x_fondo1, x_fondo2):
    # Dibujar el fondo en la posición actual del primer fondo
    pantalla.blit(imagenes["fondo"], (x_fondo1, 0))
    # Dibujar el fondo en la posición actual del segundo fondo
    pantalla.blit(imagenes["fondo"], (x_fondo2, 0))
    # Dibujar la pantalla de ayuda
    pantalla.blit(imagenes["help"], (0, 0))
    # Actualizar la pantalla para mostrar los cambios
    pygame.display.flip()

def mostrar_play(imagenes, x_fondo1, x_fondo2, bunny_images, tamagotchi, reloj, ultimo_tiempo):
    global pantalla_actual
    # Configurar el tamagotchi como vivo y registrar el tiempo de inicio
    tamagotchi.vivo = True
    tamagotchi.tiempo_inicio = time.time()
    tamagotchi.ultimo_cambio_imagen = tamagotchi.tiempo_inicio
    tamagotchi.contador_imagenes = 0

    # Bucle principal del juego cuando se está en la pantalla de juego
    while pantalla_actual == "play":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if not tamagotchi.vivo:
                    # Botón de reinicio si el tamagotchi está muerto
                    if 300 <= x <= 500 and 400 <= y <= 450:
                        tamagotchi = Tamagotchi()  # Reiniciar el juego
                        pantalla_actual = "menu"
                        return
                    continue

                # Comprobar si se ha hecho clic en el botón de alimentación
                if 90 <= x <= 240 and 470 <= y <= 544:
                    tamagotchi.alimentar()
                # Comprobar si se ha hecho clic en el botón de descanso
                elif 325 <= x <= 475 and 470 <= y <= 544:
                    tamagotchi.descansar()
                # Comprobar si se ha hecho clic en el botón de limpieza
                elif 555 <= x <= 705 and 470 <= y <= 544:
                    tamagotchi.limpiar_tamagotchi()

        tiempo_actual = time.time()
        if tamagotchi.vivo and tiempo_actual - ultimo_tiempo >= 1:
            # Actualizar el estado del tamagotchi y calcular el tiempo vivo
            tamagotchi.actualizar()
            tamagotchi.calcular_tiempo_vivo()
            ultimo_tiempo = tiempo_actual

            # Insertar datos actualizados en la base de datos
            insertar_datos(conn, tamagotchi.comer, tamagotchi.dormir, tamagotchi.limpieza, tamagotchi.tiempo_vivo)

        # Dibujar el fondo con la imagen actual del tamagotchi
        pantalla.blit(bunny_images[tamagotchi.contador_imagenes], (0, 0))

        # Dibujar las barras de estado del tamagotchi
        dibujar_barras(tamagotchi)

        if not tamagotchi.vivo:
            # Si el tamagotchi está muerto, actualizar la pantalla y volver al menú
            pygame.display.flip()
            pantalla_actual = "menu"
            break

        # Actualizar la pantalla para mostrar los cambios
        pygame.display.flip()
        reloj.tick(30)  # Limitar a 30 FPS


# Variables de estado
pantalla_actual = "menu"  # Estado inicial de la pantalla

# Creación del objeto Tamagotchi y otras inicializaciones
tamagotchi = Tamagotchi()  # Instancia del Tamagotchi
reloj = pygame.time.Clock()  # Reloj para controlar la velocidad de fotogramas
ultimo_tiempo = time.time()  # Registro del tiempo actual

# Cargar recursos gráficos y de sonido
imagenes, bunny_images = cargar_recursos()

# Variables de fondo para la animación
x_fondo1 = 0  # Posición inicial del primer fondo
x_fondo2 = ANCHO  # Posición inicial del segundo fondo (fuera de la pantalla a la derecha)
velocidad_fondo = 2  # Velocidad de desplazamiento del fondo

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # Manejo de eventos de Pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Cerrar la ventana
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Click del ratón
            posicion_raton = evento.pos
            if pantalla_actual == "menu":
                # Comprobar si se hace clic en los botones del menú principal
                if pygame.Rect(90, 470, 150, 74).collidepoint(posicion_raton):
                    pantalla_actual = "help"  # Mostrar pantalla de ayuda
                elif pygame.Rect(325, 470, 150, 74).collidepoint(posicion_raton):
                    pantalla_actual = "play"  # Iniciar el juego
                elif pygame.Rect(555, 470, 150, 74).collidepoint(posicion_raton):
                    ejecutando = False  # Salir del juego
            elif pantalla_actual == 'help' or pantalla_actual == 'play':
                # Comprobar si se hace clic en el botón de retorno al menú
                if pygame.Rect(555, 470, 150, 74).collidepoint(posicion_raton):
                    pantalla_actual = "menu"  # Volver al menú principal
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            pantalla_actual = "menu"  # Tecla Esc: volver al menú principal

    # Actualizar las posiciones de los fondos para la animación de desplazamiento
    x_fondo1, x_fondo2 = actualizar_fondo(x_fondo1, x_fondo2, velocidad_fondo)

    # Según el estado actual de la pantalla, mostrar la interfaz correspondiente
    if pantalla_actual == "menu":
        mostrar_menu(imagenes, x_fondo1, x_fondo2)  # Mostrar menú principal
    elif pantalla_actual == "help":
        mostrar_help(imagenes, x_fondo1, x_fondo2)  # Mostrar pantalla de ayuda
    elif pantalla_actual == "play":
        mostrar_play(imagenes, x_fondo1, x_fondo2, bunny_images,
                     tamagotchi, reloj, ultimo_tiempo)  # Ejecutar la lógica del juego

# Terminar Pygame y salir del programa
pygame.quit()
sys.exit()