import pygame
import sys
import time

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
fuente = pygame.font.Font('fuente/Minecraftia-Regular.ttf', 30)

# Cargar las imágenes
imagen_tamagotchi = pygame.image.load('skins_img/pixil-layer-3.png')
imagen_comer = pygame.image.load('stats_img/comer.png')
imagen_dormir = pygame.image.load('stats_img/dormir.png')
imagen_jugar = pygame.image.load('stats_img/jugar.png')

# Escalar las imágenes
imagen_tamagotchi = pygame.transform.scale(imagen_tamagotchi, (300, 300))
imagen_comer = pygame.transform.scale(imagen_comer, (30, 30))
imagen_dormir = pygame.transform.scale(imagen_dormir, (30, 30))
imagen_jugar = pygame.transform.scale(imagen_jugar, (30, 30))

# Clase Tamagotchi
class Tamagotchi:
    def __init__(self):
        self.comer = 50
        self.dormir = 50
        self.jugar = 50
        self.vivo = True
        self.tiempo_vivo = 0
        self.tiempo_inicio = time.time()

    def alimentar(self):
        if self.vivo:
            self.comer = min(self.comer + 20, 100)
            self.jugar = max(self.jugar - 10, 0)

    def descansar(self):
        if self.vivo:
            self.dormir = min(self.dormir + 20, 100)
            self.jugar = max(self.jugar - 10, 0)

    def divertir(self):
        if self.vivo:
            self.jugar = min(self.jugar + 20, 100)
            self.dormir = max(self.dormir - 10, 0)

    def actualizar(self):
        if self.vivo:
            self.comer = max(self.comer - 1, 0)
            self.dormir = max(self.dormir - 1, 0)
            self.jugar = max(self.jugar - 1, 0)

            if self.comer == 0 or self.dormir == 0 or self.jugar == 0:
                self.vivo = False

    def calcular_tiempo_vivo(self):
        if self.vivo:
            self.tiempo_vivo = int(time.time() - self.tiempo_inicio)

def dibujar_barra(valor, x, y, ancho, alto, color):
    pygame.draw.rect(ventana, GRIS, (x, y, ancho, alto))
    pygame.draw.rect(ventana, color, (x, y, ancho * (valor / 100), alto))
    pygame.draw.rect(ventana, NEGRO, (x, y, ancho, alto), 2)

def dibujar_boton(texto, x, y, ancho, alto):
    pygame.draw.rect(ventana, NEGRO, (x, y, ancho, alto), 2)
    texto_superficie = fuente.render(texto, True, NEGRO)
    ventana.blit(texto_superficie, (x + 10, y + 10))

def pantalla_inicio():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if 300 <= x <= 500 and 250 <= y <= 300:
                    return

        ventana.fill(BLANCO)
        texto_titulo = fuente.render("Bienvenido a Tamagotchi", True, NEGRO)
        ventana.blit(texto_titulo, (250, 150))
        dibujar_boton("Play", 300, 250, 200, 50)

        pygame.display.flip()

def pantalla_juego():
    tamagotchi = Tamagotchi()
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
                        tamagotchi.descansar()
                    elif 500 <= x <= 750 and 320 <= y <= 370:
                        tamagotchi.divertir()
                else:
                    if 300 <= x <= 500 and 400 <= y <= 450:
                        tamagotchi = Tamagotchi()

        tiempo_actual = time.time()
        if tiempo_actual - ultimo_tiempo >= 1:
            tamagotchi.actualizar()
            tamagotchi.calcular_tiempo_vivo()
            ultimo_tiempo = tiempo_actual

        ventana.fill(BLANCO)
        pygame.draw.rect(ventana, NEGRO, (50, 150, 300, 300), 2)
        pygame.draw.rect(ventana, NEGRO, (450, 150, 300, 300), 2)
        ventana.blit(imagen_tamagotchi, (75, 175))

        ventana.blit(imagen_comer, (420, 20))
        dibujar_barra(tamagotchi.comer, 460, 20, 300, 30, NEGRO)
        ventana.blit(imagen_dormir, (420, 60))
        dibujar_barra(tamagotchi.dormir, 460, 60, 300, 30, NEGRO)
        ventana.blit(imagen_jugar, (420, 100))
        dibujar_barra(tamagotchi.jugar, 460, 100, 300, 30, NEGRO)

        dibujar_boton("Comer", 500, 200, 250, 50)
        dibujar_boton("Dormir", 500, 260, 250, 50)
        dibujar_boton("Jugar", 500, 320, 250, 50)

        if not tamagotchi.vivo:
            texto_muerte = fuente.render("El Tamagotchi ha muerto", True, NEGRO)
            ventana.blit(texto_muerte, (250, 450))
            texto_tiempo_vivo = fuente.render(f"Tiempo vivo: {tamagotchi.tiempo_vivo} segundos", True, NEGRO)
            ventana.blit(texto_tiempo_vivo, (200, 500))
            dibujar_boton("Volver a jugar", 300, 400, 200, 50)

        pygame.display.flip()
        reloj.tick(30)

if __name__ == "__main__":
    pantalla_inicio()
    pantalla_juego()
