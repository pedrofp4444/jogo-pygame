import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Teste Pygame")

# Definir cores
white = (255, 255, 255)
red = (255, 0, 0)

# Definir a posição e o raio do círculo
circle_x, circle_y = width // 2, height // 2
circle_radius = 30
circle_speed = 5

# Loop principal
running = True
while running:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Obter as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Mover o círculo com as setas do teclado
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # Preencher o fundo com branco
    screen.fill(white)

    # Desenhar o círculo
    pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)

    # Atualizar o ecrã
    pygame.display.flip()

    # Definir a velocidade do jogo (frames por segundo)
    pygame.time.Clock().tick(60)

# Fechar o Pygame
pygame.quit()
sys.exit()
