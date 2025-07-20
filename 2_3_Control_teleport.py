import pygame
import numpy

pygame.init()

TILE_SIZE = 32
TILE_X, TILE_Y = 32, 16

WIDTH, HEIGHT = TILE_SIZE * TILE_X, TILE_SIZE * TILE_Y
FPS = 60
colors = {0:(0,0,0), 1:(255,255,255), 2:(255, 0,0), 3:(0,255,0), 4:(0,0,255), 5:(191,191,191)}
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_matrix = numpy.ones((WIDTH, HEIGHT), dtype=numpy.uint8)
player_position = numpy.array((2,2), dtype=numpy.int8)
player_position_previous = player_position
screen_matrix[player_position[0], player_position[1]] = 3
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #control
        elif event.type == pygame.KEYDOWN:
            screen_matrix[player_position[0],player_position[1]] = 1
            if event.key == pygame.K_UP:
                player_position[0]-=1
            if event.key == pygame.K_DOWN:
                player_position[0]+=1
            if event.key == pygame.K_LEFT:
                player_position[1]-=1
            if event.key == pygame.K_RIGHT:
                player_position[1]+=1
            player_position %= (TILE_Y, TILE_X)
            screen_matrix[player_position[0],player_position[1]] = 3


    #drawing
    for y in range(TILE_Y):
        for x in range(TILE_X):
            pygame.draw.rect(screen, colors[screen_matrix[y,x]], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, colors[0], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()