import pygame
import numpy

def apple_insert(screen_matrix):
    while True:
        apple_position = numpy.array((numpy.random.randint(0, TILE_Y-1),numpy.random.randint(0, TILE_X-1)), dtype=numpy.int32)
        if screen_matrix[apple_position[0], apple_position[1]] == 1:
            return apple_position

pygame.init()

TILE_SIZE = 32
TILE_X, TILE_Y = 32, 16

WIDTH, HEIGHT = TILE_SIZE * TILE_X, TILE_SIZE * TILE_Y
FPS = 60
colors = {0:(0,0,0), 1:(255,255,255), 2:(255, 0,0), 3:(0,255,0), 4:(0,0,255), 5:(191,191,191)}
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_matrix = numpy.ones((WIDTH, HEIGHT), dtype=numpy.uint32)

player_position = numpy.array((14,14), dtype=numpy.int32)
player_velocity = numpy.array((0,1), dtype=numpy.int32)

clock = pygame.time.Clock()
body = [[player_position[1] ,player_position[0]-x] for x in range(3)]
body.reverse()

for b in body:
    screen_matrix[b[0], b[1]] = 3

apple_position = apple_insert(screen_matrix)
screen_matrix[apple_position[0], apple_position[1]] = 2
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
    if t % t_divider == 0:
        key_permission = True
        player_position += player_velocity
        player_position %= (TILE_Y, TILE_X)
        if [player_position[0], player_position[1]] in body:
            run = False
        if screen_matrix[player_position[0], player_position[1]] == 2:
            apple_position = apple_insert(screen_matrix)
            screen_matrix[apple_position[0], apple_position[1]] = 2
        else:
            body_erased = body.pop(0)
        body.append([player_position[0], player_position[1]])
        screen_matrix[body_erased[0], body_erased[1]] = 1
        for b in body:
            screen_matrix[b[0], b[1]] = 3

    #drawing
    for y in range(TILE_Y):
        for x in range(TILE_X):
            pygame.draw.rect(screen, colors[screen_matrix[y,x]], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, colors[0], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    pygame.draw.rect(screen, colors[4],(body[-1][1]* TILE_SIZE, body[-1][0] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 5)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()