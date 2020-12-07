import pygame

from components.ball import Ball
from components.player import Player
from os import path
from utils.text_utils import draw_text
from utils.constants import (SCREEN_WIDTH, SCREEN_HEIGHT, TITTLE,  BLACK, IMG_DIR)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITTLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image = pygame.image.load(path.join(IMG_DIR, "spacefield.png")).convert()
        self.image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.runnig = True

    def run(self):
        self.create_components()
        # Game loop:

        self.playing = True

        while self.playing:
            self.clock.tick(120)
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        ball = Ball(1)
        self.all_sprites.add(ball)
        self.balls.add(ball)



    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        if hits:
            self.playing = False

        hits = pygame.sprite.groupcollide(self.balls, self.player.bullets, True, True)

        for hit in hits:
            if hit.size <4:
                for i in  range(0, 2):
                    ball = Ball(hit.size + 1 )
                    self.all_sprites.add(ball)
                    self.balls.add(ball)




    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.runnig = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()





    def draw(self):
        background_rect = self.background_image.get_rect()
        self.screen.blit(self.background_image, background_rect)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        self.screen.blit(self.background_image, self.background_image.get_rect())
        draw_text(self.screen, "Game Punch that", 64, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
        draw_text(self.screen, "Press left right keys to move and SPACE to shoot", 20, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        draw_text(self.screen, "Press ENTER key to begin", 20, SCREEN_WIDTH/2, SCREEN_HEIGHT*3/5)

        pygame.display.flip()

        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        waiting = False