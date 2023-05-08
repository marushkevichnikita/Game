import pygame
import sys
from pygame.sprite import Sprite

class Starship(Sprite):
    def __init__(self,screen):
        super(Starship, self).__init__()
        self.screen=screen
        self.image = pygame.image.load('files/starship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.rect.center = self.screen_rect.center
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False


    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_starship(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerx += 1.5
        if self.mleft and self.rect.left > 0:
            self.centerx -= 1.5
        if self.mtop and self.rect.top > 0:
            self.centery -= 1.5
        if self.mbottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 1.5
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def create_starship(self):
        #bottom center starship position
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

