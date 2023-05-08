import pygame

class Bulletup (pygame.sprite.Sprite):

    def __init__(self, screen, starship):
        #bullet in the starship
        super(Bulletup, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 139, 195, 74
        self.speed = 4.5
        self.rect.centerx = starship.rect.centerx
        self.rect.top = starship.rect.top
        self.y = float(self.rect.y)


    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bulletdown (pygame.sprite.Sprite):

    def __init__(self, screen, starship):
        #bullet in the starship
        super(Bulletdown, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 139, 195, 74
        self.speed = 4.5
        self.rect.centerx = starship.rect.centerx
        self.rect.bottom = starship.rect.bottom
        self.y = float(self.rect.y)


    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bulletright (pygame.sprite.Sprite):

    def __init__(self, screen, starship):
        #bullet in the starship
        super(Bulletright, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 12, 2)
        self.color = 139, 195, 74
        self.speed = 4.5
        self.rect.centery = starship.rect.centery # same y coordinate as starship
        self.rect.left = starship.rect.right # x coordinate for right way shooting
        self.x = float(self.rect.x)


    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bulletleft (pygame.sprite.Sprite):

    def __init__(self, screen, starship):
        #bullet in the starship
        super(Bulletleft, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 12, 2)
        self.color = 139, 195, 74
        self.speed = 4.5
        self.rect.centery = starship.rect.centery
        self.rect.left = starship.rect.left
        self.x = float(self.rect.x)


    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

