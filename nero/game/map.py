from turtle import bgcolor
import pygame
import spritesheet_class

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('game')

bgcolor = (225, 198, 153)
black = (0, 0, 0)

#sprite sheets
sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()
sprite_sheet = spritesheet_class.Spritesheet(sprite_sheet_image)

frame_0 = sprite_sheet.get_image(0, 24, 24, 3, black) 
frame_1 = sprite_sheet.get_image(1, 24, 24, 3, black) 
frame_2 = sprite_sheet.get_image(2, 24, 24, 3, black) 
frame_3 = sprite_sheet.get_image(3, 24, 24, 3, black) 
frame_4 = sprite_sheet.get_image(4, 24, 24, 3, black) 
frame_5 = sprite_sheet.get_image(5, 24, 24, 3, black) 

run = True
while run:
    
    screen.fill(bgcolor)

    screen.blit(frame_0, (0, 0))
    screen.blit(frame_1, (48, 0))
    screen.blit(frame_2, (96, 0))

    
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
    pygame.display.update()


pygame.quit()
