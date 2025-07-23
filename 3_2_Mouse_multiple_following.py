import pygame
import numpy

def following(goal, player_position):
    return numpy.sign(goal - player_position)

pygame.init()

TILE_SIZE = 16
TILE_X, TILE_Y = 64, 32

WIDTH, HEIGHT = TILE_SIZE * TILE_X, TILE_SIZE * TILE_Y
FPS = 60
colors = {0:(255,255,255), 1:(0,0,0), 2:(255, 0,0), 3:(0,255,0), 4:(0,0,255), 5:(191,191,191)}
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_matrix = numpy.zeros((WIDTH, HEIGHT), dtype=numpy.uint8)
player_position = numpy.array((2,2), dtype=numpy.int8)
nmbrs = 40
player_positions = [player_position.copy() for _ in range(nmbrs)]
screen_matrix[player_position[0], player_position[1]] = 3
clock = pygame.time.Clock()
mouse_position = numpy.zeros((2), dtype=numpy.uint8)
goal = player_position
cells_active = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #control
        elif event.type == pygame.MOUSEBUTTONDOWN:
                goal = mouse_position[:] = pygame.mouse.get_pos()[1]//TILE_SIZE, pygame.mouse.get_pos()[0]//TILE_SIZE
                cells_active = 0

    g = numpy.full_like(player_positions, goal, dtype=numpy.uint8)

    d = numpy.sign(g-player_positions)


    for j in range(nmbrs):
        if j <= cells_active:
            screen_matrix[player_positions[j][0], player_positions[j][1]] = 0
            player_positions[j][0] += d[j][0]
            player_positions[j][1] += d[j][1]
            screen_matrix[player_positions[j][0], player_positions[j][1]] = 3
        else:
            screen_matrix[player_positions[j][0], player_positions[j][1]] = 3

    if numpy.any(d) != 0:
        cells_active += 1
    if cells_active > nmbrs:
        cells_active = nmbrs

    #drawing
    for y in range(TILE_Y):
        for x in range(TILE_X):
            pygame.draw.rect(screen, colors[screen_matrix[y,x]], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, colors[1], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    pygame.display.update()
    mouse_position[:] = pygame.mouse.get_pos()[1]//TILE_SIZE, pygame.mouse.get_pos()[0]//TILE_SIZE

    pygame.display.set_caption(str(cells_active))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()