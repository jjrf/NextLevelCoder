import pygame

from components.bullet import Bullet
from utils.constants import (
    GREEN,
    SCREEN_WIDHT,
    SCREEN_HEIGHT
)

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image =pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDHT/2
        self.rect.centery = SCREEN_HEIGHT/2


    def update(self):
        key = pygame.key.get_pressed()
        if key [pygame.K_RIGHT]:
            self.rect.x +=5
        if self.rect.right  >= SCREEN_WIDHT:
            self.rect.right = SCREEN_WIDHT
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
                self.rect.x -=5
        if self.rect.left <= 0:
                self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets = pygame.sprite.Group()
        self.bullets.add(bullet)




