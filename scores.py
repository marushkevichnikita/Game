import pygame.font
from starship import Starship
from pygame.sprite import Group

class Scores():
    #game info output
    def __init__(self, screen, stats):
    #scores initialization
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_starships()

    def image_score(self):
        #score text into the image convertation
        self.score_img  = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_starships(self):
        #lifes
        self.starships = Group()
        for starship_number in range(self.stats.starships_left):
            starship = Starship(self.screen)
            starship.rect.x = 15 + starship_number * starship.rect.width
            starship.rect.y = 20
            self.starships.add(starship)

    def image_high_score(self):
        #record score into the image convertation
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self):

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.starships.draw(self.screen)
