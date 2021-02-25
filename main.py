import pygame
import os
from os import path
from settings import *
from sprites import *

class Game():
    def __init__(self):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group() 
        self.enemy = Enemy(self)
        self.all_sprites.add(self.enemy)
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS) 
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()

    def events(self):
        # game loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        pass

g = Game()
while g.running:
    g.new()

pygame.quit()
quit()
