import pygame, csv, os
from sprites import*
from config import *
import sys
#from tilemap import *

#taken from different video on how to add csv file as map -> see tilemap.py
#map = Tilemap('test_map.csv', spritesheet)

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('I dont know')
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font('Ariel', 32)
        self.running = True

        self.character_spritesheet = Spritesheet('img/Hero.png')
        self.terrain_spritesheet = Spritesheet('img/Tileset.png')
    
    def createTilemap(self):
        for i, row in enumerate(TILEMAP):
            for j, column in enumerate(row):
                Ground(self, j , i)
                if column == "B":
                   Block(self, j, i)
                if column == "P":
                    Player(self, j, i)


    def new(self):
        #a new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    
    def events(self):
    #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
    #game loop updates
        self.all_sprites.update()

    def draw(self):
    #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def game_over(self):
        pass

    def intro_screen(self):
        pass

    def main(self):
    #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()