import pygame

class Snake:
    def __init__(self, x, y, w, h, color, screen):
        #Position/Height
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        #
        self.screen = screen
        self.color = color
        #movement
        self.speed = 5
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw_snake(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, 10, 10))

    def events(self, event):
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                isRunning = False
        elif event.key == pygame.K_d:
            self.move_right = True
            self.turn_off_other_direction(move_right = True)
        elif event.key == pygame.K_a:
            self.move_left = True
            self.turn_off_other_direction(move_left = True)
        elif event.key == pygame.K_w:
            self.move_up = True
            self.turn_off_other_direction(move_up = True)
        elif event.key == pygame.K_s:
            self.move_down = True
            self.turn_off_other_direction(move_down = True)

    def update_movement(self):
        if self.move_right:
            self.x += self.speed
        if self.move_down:
            self.y += self.speed
        if self.move_left:
            self.x -= self.speed
        if self.move_up:
            self.y -= self.speed
            
    def turn_off_other_direction(self, move_up = False, move_right = False, move_down = False, move_left = False):
        self.move_up = move_up
        self.move_right = move_right
        self.move_down = move_down
        self.move_left = move_left