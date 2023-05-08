import pygame, sys
from bullet import Bulletup
from bullet import Bulletdown
from bullet import Bulletright
from bullet import Bulletleft
from alf import Alf
import time

def events(screen, starship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                starship.mright = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                starship.mleft = True
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                starship.mtop = True
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                starship.mbottom = True
            elif event.key == pygame.K_i:
                new_bullet = Bulletup(screen, starship)
                bullets.add(new_bullet)
            elif event.key == pygame.K_k:
                new_bullet = Bulletdown(screen, starship)
                bullets.add(new_bullet)
            elif event.key == pygame.K_l:
                new_bullet = Bulletright(screen, starship)
                bullets.add(new_bullet)
            elif event.key == pygame.K_j:
                new_bullet = Bulletleft(screen, starship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                starship.mright = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                starship.mleft = False
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                starship.mtop = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                starship.mbottom = False

def update(bg_image, screen, stats, sc, starship, alfs, bullets):
    #screen updating
    screen.blit(bg_image, (0, 0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    starship.output()
    alfs.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, alfs, bullets):
    #erase bullets after the end of screen to reduce memory
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, alfs, True, True)
    if collisions:
        for alfs in collisions.values():
            stats.score += 1 * len(alfs)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_starships()

    if len(alfs) == 0:
        bullets.empty()
        create_army(screen, alfs)

def starship_kill(stats, screen, sc, starship, alfs, bullets):
    #starship and alfs hitting together
    if stats.starships_left > 0:
        stats.starships_left -= 1
        sc.image_starships()
        alfs.empty()
        bullets.empty()
        create_army(screen, alfs)
        starship.create_starship()
        time.sleep(1)
    else:
        stats.run_game = False
        image = pygame.image.load('files/gameover.png')
        image_rect = image.get_rect()
        image_rect.center = screen.get_rect().center
        screen.blit(image, image_rect)
        pygame.display.flip()

    # waiting before exit
        pygame.time.wait(3000)

    # exit
        pygame.quit()
        sys.exit()

def update_alfs(stats, screen, sc, starship, alfs, bullets):
    alfs.update()
    if pygame.sprite.spritecollideany(starship, alfs):
        starship_kill(stats, screen, sc, starship, alfs, bullets)
    alfs_check(stats, screen, sc, starship, alfs, bullets)

def alfs_check(stats, screen, sc, starship, alfs, bullets):
    #alf deadline position check
    screen_rect = screen.get_rect()
    for alf in alfs.sprites():
        if alf.rect.bottom >= screen_rect.bottom:
            starship_kill(stats, screen, sc, starship, alfs, bullets)
            break

def create_army (screen, alfs):
    #army creating
    alf = Alf(screen)
    alf_width = alf.rect.width
    number_alf_x = int((900 - 2 * alf_width) / alf_width)
    alf_height = alf.rect.height
    number_alf_y = int((700 - 128 - 4 * alf_height) / alf_height)

    for row_number in range(number_alf_y - 5):

        for alf_number in range(number_alf_x):
            alf = Alf(screen)
            alf.x = alf_width + (alf_width * alf_number)
            alf.y = alf_height + (alf_height * row_number)
            alf.rect.x = alf.x
            alf.rect.y = alf.rect.height + alf.rect.height * row_number
            alfs.add(alf)


def check_high_score(stats, sc):
    #new records checking
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('files/highscore.txt', 'w') as f:
            f.write(str(stats.high_score))












