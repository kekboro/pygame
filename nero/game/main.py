from operator import truediv
from turtle import bgcolor
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('game')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#colours

bgcolor = (225, 198, 153)

def draw_bg():
    screen.fill(bgcolor)


#define character class
class CHARACTER(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        #self.index = 0
        #for i in range(#amount of images in animations):
        img = pygame.image.load(f'img/{self.char_type}/IDLE/avatar.png')
        self.img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
   
    def move(self, moving_left, moving_right, moving_up, moving_down):
        #reset movement variables
        dx = 0
        dy = 0
        
        #assign movement viariables
        if moving_left:
            dx = -self.speed
            self.flip = False
            self.direction = 1
        if moving_right:
            dx = self.speed
            self.flip = True
            self.direction = 1
        if moving_up:
            dy = -self.speed
        if moving_down:
            dy = self.speed
        
        #update rect position
        self.rect.x += dx
        self.rect.y += dy
        

    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)



player = CHARACTER('PLAYER', 400, 400, .25, 5)


run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.draw()

    player.move(moving_left, moving_right, moving_up, moving_down)

    for event in  pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                moving_right = True
            if event.key == pygame.K_LEFT: 
                moving_left = True
            if event.key == pygame.K_UP: 
                moving_up = True
            if event.key == pygame.K_DOWN: 
                moving_down = True
            if event.key == pygame.K_ESCAPE:
                run = False

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: 
                moving_right = False
            if event.key == pygame.K_LEFT: 
                moving_left = False
            if event.key == pygame.K_UP: 
                moving_up = False
            if event.key == pygame.K_DOWN: 
                moving_down = False

    pygame.display.update()
pygame.quit()
