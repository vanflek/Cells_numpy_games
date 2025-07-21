import pygame
import numpy

pygame.init()

TILE_SIZE = 32
TILE_X, TILE_Y = 32, 16

WIDTH, HEIGHT = TILE_SIZE * TILE_X, TILE_SIZE * TILE_Y
FPS = 60
colors = {0:(255,255,255), 1:(0,0,0), 2:(255, 0,0), 3:(0,255,0), 4:(0,0,255), 5:(191,191,191)}
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_matrix = numpy.zeros((WIDTH, HEIGHT), dtype=numpy.uint8)
player_position = numpy.array((2,2), dtype=numpy.int8)
player_velocity = numpy.array((0,1), dtype=numpy.int8)
screen_matrix[player_position[0], player_position[1]] = 3
clock = pygame.time.Clock()
t = 0
t_divider = 10
key_permission = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #control
        elif event.type == pygame.KEYDOWN and key_permission:
            if event.key == pygame.K_UP and player_velocity[1]:
                player_velocity[0] = -1
                player_velocity[1] = 0
            if event.key == pygame.K_DOWN and player_velocity[1]:
                player_velocity[0] = 1
                player_velocity[1] = 0
            if event.key == pygame.K_LEFT and player_velocity[0]:
                player_velocity[1] = -1
                player_velocity[0] = 0
            if event.key == pygame.K_RIGHT and player_velocity[0]:
                player_velocity[1] = 1
                player_velocity[0] = 0
            key_permission = False

    #turn
    t += 1 if t < FPS-1 else - (FPS-1)
    if t%t_divider == 0:
        key_permission = True
        screen_matrix[player_position[0], player_position[1]] = 0
        player_position += player_velocity
        player_position %= (TILE_Y, TILE_X)
        screen_matrix[player_position[0], player_position[1]] = 3

    #drawing
    for y in range(TILE_Y):
        for x in range(TILE_X):
            pygame.draw.rect(screen, colors[screen_matrix[y,x]], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, colors[1], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()