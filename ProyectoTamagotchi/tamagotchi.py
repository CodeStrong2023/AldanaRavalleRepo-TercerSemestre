# Importaciones
import pygame
import sys
import time

class Tamagotchi:  # La clase Tamagotchi define las propiedades y comportamientos del Tamagotchi
    def __init__(self):
        # Stats
        self.hambre = 50
        self.energia = 50
        self.felicidad = 50
        self.vivo = True

        self.tiempo_vivo = 0
        self.tiempo_inicio = time.time()

    # Métodos de la clase Tamagotchi
    def alimentar(self):  # Reduce el hambre y aumenta la felicidad
        if self.vivo:
            self.hambre = max(self.hambre - 20, 0)
            self.felicidad = min(self.felicidad + 10, 100)

    def dormir(self):  # Aumenta la energía y el hambre
        if self.vivo:
            self.energia = min(self.energia + 20, 100)
            self.hambre = min(self.hambre + 10, 100)

    def jugar(self):  # Aumenta la felicidad y reduce la energía
        if self.vivo:
            self.felicidad = min(self.felicidad + 20, 100)
            self.energia = max(self.energia - 10, 0)

    def actualizar(self):  # Incrementa el hambre, disminuye la energía y la felicidad con el tiempo, y verifica si el Tamagotchi sigue vivo
        if self.vivo:
            self.hambre = min(self.hambre + 1, 100)
            self.energia = max(self.energia - 1, 0)
            self.felicidad = max(self.felicidad - 1, 0)

            if self.hambre == 0 or self.energia == 0 or self.felicidad == 0:
                self.vivo = False

    # Calcula el tiempo que el Tamagotchi ha estado vivo
    def calcular_tiempo_vivo(self):
        if self.vivo:
            self.tiempo_vivo = int(time.time() - self.tiempo_inicio)


# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tamagotchi")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)

# Fuente
fuente = pygame.font.SysFont(None, 36)

# Cargar las imagenes
imagen_tamagotchi = pygame.image.load('tamagotchi.png')
imagen_hambre = pygame.image.load('hambre.png')
imagen_energia = pygame.image.load('energia.png')
imagen_felicidad = pygame.image.load('felicidad.png')

# Escalar las imagenes
imagen_tamagotchi = pygame.transform.scale(imagen_tamagotchi, (300, 300))
imagen_hambre = pygame.transform.scale(imagen_hambre, (30, 30))
imagen_energia = pygame.transform.scale(imagen_energia, (30, 30))
imagen_felicidad = pygame.transform.scale(imagen_felicidad, (30, 30))


# Dibujar barras de estado
def dibujar_barra(valor, x, y, ancho, alto, color):
    pygame.draw.rect(ventana, GRIS, (x, y, ancho, alto))
    pygame.draw.rect(ventana, color, (x, y, ancho * (valor / 100), alto))
    pygame.draw.rect(ventana, NEGRO, (x, y, ancho, alto), 2)


# Función para dibujar botones
def dibujar_boton(texto, x, y, ancho, alto):
    pygame.draw.rect(ventana, NEGRO, (x, y, ancho, alto), 2)
    texto_superficie = fuente.render(texto, True, NEGRO)
    ventana.blit(texto_superficie, (x + 10, y + 10))

# Función para reiniciar el juego
def reiniciar_juego():
    global tamagotchi
    tamagotchi = Tamagotchi()

# Crear el Tamagotchi y tiempo de inicio
tamagotchi = Tamagotchi()

# Bucle principal del juego
def juego():
    reloj = pygame.time.Clock()
    ultimo_tiempo = time.time()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if tamagotchi.vivo:
                    if 500 <= x <= 750 and 200 <= y <= 250:
                        tamagotchi.alimentar()
                    elif 500 <= x <= 750 and 260 <= y <= 310:
                        tamagotchi.dormir()
                    elif 500 <= x <= 750 and 320 <= y <= 370:
                        tamagotchi.jugar()
                else:
                    if 300 <= x <= 500 and 400 <= y <= 450:
                        reiniciar_juego()

        # Actualizar estado del Tamagotchi cada segundo
        tiempo_actual = time.time()
        if tiempo_actual - ultimo_tiempo >= 1:
            tamagotchi.actualizar()
            tamagotchi.calcular_tiempo_vivo()
            ultimo_tiempo = tiempo_actual

        # Dibujar la interfaz
        ventana.fill(BLANCO)

        # Dibujar rectángulos
        pygame.draw.rect(ventana, GRIS, (50, 150, 300, 300))
        pygame.draw.rect(ventana, GRIS, (450, 150, 300, 300))

        # Dibujar imagen del Tamagotchi
        ventana.blit(imagen_tamagotchi, (75, 175))

        # Dibujar barras de estado
        ventana.blit(imagen_hambre, (420, 20))  # Imagen de hambre
        dibujar_barra(tamagotchi.hambre, 460, 20, 300,
                      30, NEGRO)    # Hambre (rojo)
        ventana.blit(imagen_energia, (420, 60))  # Imagen de energía
        dibujar_barra(tamagotchi.energia, 460, 60, 300,
                      30, NEGRO)   # Energía (verde)
        ventana.blit(imagen_felicidad, (420, 100))  # Imagen de felicidad
        dibujar_barra(tamagotchi.felicidad, 460, 100,
                      300, 30, NEGRO)  # Felicidad (azul)

        # Dibujar botones
        dibujar_boton("Alimentar", 500, 200, 250, 50)
        dibujar_boton("Dormir", 500, 260, 250, 50)
        dibujar_boton("Jugar", 500, 320, 250, 50)

        # Dibujar mensaje de muerte y botón de reinicio
        if not tamagotchi.vivo:
            texto_muerte = fuente.render(
                "El Tamagotchi ha muerto", True, NEGRO)
            ventana.blit(texto_muerte, (250, 450))
            texto_tiempo_vivo = fuente.render(
                f"Tiempo vivo: {tamagotchi.tiempo_vivo} segundos", True, NEGRO)
            ventana.blit(texto_tiempo_vivo, (200, 500))
            dibujar_boton("Volver a jugar", 300, 400, 200, 50)

        pygame.display.flip()
        reloj.tick(30)


if __name__ == "__main__":  # Esto inicia el juego al reiniciar el Tamagotchi y ejecutar el bucle principal del juego
    reiniciar_juego()
    juego()