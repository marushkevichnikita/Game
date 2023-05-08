import pygame, controls
from starship import Starship
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((900,700))
    pygame.display.set_caption("Myke's game")
    bg_image = pygame.image.load('files/space.jpg')
    starship = Starship(screen)
    bullets = Group()
    alfs = Group()
    controls.create_army(screen, alfs)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        screen.blit(bg_image, (0, 0))  # нарисовать фон
        controls.events(screen, starship, bullets)
        if stats.run_game:
            starship.update_starship()
            controls.update(bg_image, screen, stats, sc, starship, alfs, bullets)
            controls.update_bullets(screen, stats, sc, alfs, bullets)
            controls.update_alfs(stats, screen, sc, starship, alfs, bullets)
        pygame.display.flip()

run()