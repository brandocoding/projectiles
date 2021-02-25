import pygame
import os
from os import path
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 96
        self.pos = vec(WIDTH / 2, HEIGHT - 96)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        #print(self.pos)
        self.acc = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.center = self.pos

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.shoot_delay = 200
        self.last_shot = pygame.time.get_ticks()
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.shoot()

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time
            # down and up
            self.game.projectile = Projectile(self, self.rect.centerx, self.rect.centery, 3, 0)
            self.game.all_sprites.add(self.game.projectile) 
            self.game.projectile = Projectile(self, self.rect.centerx, self.rect.centery, -3, 0)
            self.game.all_sprites.add(self.game.projectile)
            
            # left and right
            self.game.projectile = Projectile(self, self.rect.centerx, self.rect.centery, 0, 3)
            self.game.all_sprites.add(self.game.projectile)
            self.game.projectile = Projectile(self, self.rect.centerx, self.rect.centery, 0, -3)
            self.game.all_sprites.add(self.game.projectile)
            
class Projectile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, speed_1, speed_2):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = speed_1
        self.speedx = speed_2

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
               
        if self.rect.bottom < 0:
            self.kill()
                    
    
        
