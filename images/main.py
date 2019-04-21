import pygame
from snake import Snake
pygame.init()

 #set a variable for how quick the game runs
clock = pygame.time.Clock()
size = width, height = 480, 600
black = 0, 0, 0
blue = 0, 0, 255
screen = pygame.display.set_mode(size)


snake = Snake(0, 0, 40, 40, black, screen)


isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            snake.events(event)
    
    screen.fill(blue)
    snake.draw_snake()
    snake.update_movement()
    pygame.display.flip()

    clock.tick(30)