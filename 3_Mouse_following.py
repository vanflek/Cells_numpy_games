import pygame
import numpy

def following(goal, player_position):
    return numpy.sign(goal - player_position)

pygame.init()

TILE_SIZE = 32
TILE_X, TILE_Y = 32, 16

WIDTH, HEIGHT = TILE_SIZE * TILE_X, TILE_SIZE * TILE_Y
FPS = 60
colors = {0:(255,255,255), 1:(0,0,0), 2:(255, 0,0), 3:(0,255,0), 4:(0,0,255), 5:(191,191,191)}
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_matrix = numpy.zeros((WIDTH, HEIGHT), dtype=numpy.uint8)
player_position = numpy.array((2,2), dtype=numpy.uint8)
screen_matrix[player_position[0], player_position[1]] = 3
clock = pygame.time.Clock()
mouse_position = numpy.zeros((2), dtype=numpy.uint8)
goal = player_position


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #control
        elif event.type == pygame.MOUSEBUTTONDOWN:
                goal = mouse_position[:] = pygame.mouse.get_pos()[1]//TILE_SIZE, pygame.mouse.get_pos()[0]//TILE_SIZE
    d = following(goal, player_position)
    if d.any() != 0:
        screen_matrix[player_position[0], player_position[1]] = 0
        player_position[0] += d[0]
        player_position[1] += d[1]
        screen_matrix[player_position[0], player_position[1]] = 3
    #drawing
    for y in range(TILE_Y):
        for x in range(TILE_X):
            pygame.draw.rect(screen, colors[screen_matrix[y,x]], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, colors[1], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    pygame.display.update()
    mouse_position[:] = pygame.mouse.get_pos()[1]//TILE_SIZE, pygame.mouse.get_pos()[0]//TILE_SIZE

    pygame.display.set_caption(str(d) + str(goal) + str(player_position))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()