import pygame
import numpy

pygame.init()

TILE_SIZE = 32
TILE_X, TILE_Y = 32, 16

WIDTH, HEIGHT = TILE_SIZE * TILE_X, TILE_SIZE * TILE_Y
FPS = 60
colors = {0:(0,0,0), 1:(255,255,255), 2:(255, 0,0), 3:(0,255,0), 4:(0,0,255), 5:(191,191,191)}
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_matrix = numpy.zeros((WIDTH, HEIGHT), dtype=numpy.uint8)
clock = pygame.time.Clock()
mouse_position = numpy.zeros((2), dtype=numpy.uint8)
pygame.mouse.set_visible(False)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                cells_possible = []
                for y in range(1, TILE_Y-1):
                    for x in range(1, TILE_X-1):
                        if screen_matrix[y][x] == 2:
                            screen_matrix[y][x] = 0
                for y in range(1, TILE_Y-1):
                    for x in range(1, TILE_X-1):
                        if sum(screen_matrix[y-1:y+2,x]==1) + sum(screen_matrix[y,x-1:x+2]==1) == 1:
                            cells_possible.append([y,x])
                for cell in cells_possible:
                        screen_matrix[cell[0], cell[1]] = 2

        #control
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                screen_matrix[pygame.mouse.get_pos()[1]//TILE_SIZE, pygame.mouse.get_pos()[0]//TILE_SIZE] = 1
            if event.button == 3:
                screen_matrix[pygame.mouse.get_pos()[1]//TILE_SIZE, pygame.mouse.get_pos()[0]//TILE_SIZE] = 0
    #drawing
    for y in range(TILE_Y):
        for x in range(TILE_X):
            pygame.draw.rect(screen, colors[screen_matrix[y,x]], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, colors[1], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    pygame.draw.rect(screen, colors[4],
                     ((pygame.mouse.get_pos()[0]//TILE_SIZE)*TILE_SIZE,
                      (pygame.mouse.get_pos()[1]//TILE_SIZE)*TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
    pygame.display.update()
    mouse_position[:] = pygame.mouse.get_pos()[1]//TILE_SIZE, pygame.mouse.get_pos()[0]//TILE_SIZE
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()