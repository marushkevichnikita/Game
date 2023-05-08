import pygame
import random


class Alf(pygame.sprite.Sprite):
    # one alien class

    def __init__(self, screen):
        super(Alf, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('files/alf.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.screen.get_width())  # horizontal random starting position
        self.rect.y = random.randint(-self.screen.get_height(), 0)  # vertical random starting position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1)])  # random starting moving

    def draw(self):
        # alf on the screen
        self.screen.blit(self.image, self.rect)

    def update(self):
        # alfs moving
        self.x += 0.2 * self.direction[0]
        self.y += 0.2 * self.direction[1]
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # changing the direction if the object out of the screem
        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.direction = (-self.direction[0], self.direction[1])
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
            self.direction = (self.direction[0], -self.direction[1])

