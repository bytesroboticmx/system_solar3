#Autor: Profr. Aldo Glez. V.
#Licencia: MIT
#Programa en python3 que simula el sistema solar con pygame con nombres y orbitas.
import pygame
import math

# Inicializar pygame
pygame.init()

# Configuracion de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sistema solar completo con orbitas y nombres")

# Definir los colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (169, 169, 169)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)
CYAN = (0, 255, 255)

# Definir las propiedades del sistema solar
sun_radius = 50
sun_pos = (width // 2, height // 2)

planet_data = [
    {"name": "Mercurio", "color": GRAY, "radius": 10, "distance": 100, "speed": 0.03},
    {"name": "Venus", "color": ORANGE, "radius": 15, "distance": 130, "speed": 0.02},
    {"name": "Tierra", "color": BLUE, "radius": 20, "distance": 160, "speed": 0.01},
    {"name": "Marte", "color": RED, "radius": 18, "distance": 190, "speed": 0.009},
    {"name": "Jupiter", "color": ORANGE, "radius": 35, "distance": 220, "speed": 0.005},
    {"name": "Saturno", "color": YELLOW, "radius": 30, "distance": 250, "speed": 0.004},
    {"name": "Urano", "color": CYAN, "radius": 25, "distance": 280, "speed": 0.003},
    {"name": "Neptuno", "color": BLUE, "radius": 23, "distance": 310, "speed": 0.002}
]

# Configura la fuente del texto
font = pygame.font.Font(None, 25)

# Ejecuta el ciclo principal del sistema
running = True
while running:
    # Evento handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibuja el fondo de pantalla
    screen.fill(BLACK)

    # Dibuja el sol
    pygame.draw.circle(screen, YELLOW, sun_pos, sun_radius)
    sun_text = font.render("Sol", True, YELLOW)
    sun_text_rect = sun_text.get_rect(center=(sun_pos[0], sun_pos[1] + sun_radius + 20))
    screen.blit(sun_text, sun_text_rect)

    # Actualiza y dibuja cada planeta
    for planet in planet_data:
        planet_radius = planet["radius"]
        planet_distance = planet["distance"]
        planet_speed = planet["speed"]

        planet_angle = pygame.time.get_ticks() / 1000 * planet_speed
        planet_x = sun_pos[0] + planet_distance * math.cos(planet_angle)
        planet_y = sun_pos[1] + planet_distance * math.sin(planet_angle)

        pygame.draw.circle(screen, planet["color"], (int(planet_x), int(planet_y)), planet_radius)

        planet_text = font.render(planet["name"], True, planet["color"])
        planet_text_rect = planet_text.get_rect(center=(int(planet_x), int(planet_y) + planet_radius + 20))
        screen.blit(planet_text, planet_text_rect)

        # Dibuja la orbita de cada planeta con eclipse
        orbit_width = planet_distance * 2
        orbit_height = planet_distance * 2
        orbit_rect = pygame.Rect(sun_pos[0] - planet_distance, sun_pos[1] - planet_distance, orbit_width, orbit_height)
        pygame.draw.ellipse(screen, planet["color"], orbit_rect, 1)

    # Actualiza la pantalla
    pygame.display.flip()

# Termina pygame
pygame.quit()
