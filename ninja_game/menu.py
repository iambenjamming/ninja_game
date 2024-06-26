import pygame

from scripts.button import Button
from scripts.utils import load_image, load_images
from scripts.clouds import Clouds

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display = pygame.Surface((320, 240))
pygame.display.set_caption('MAIN MENU')

clock = pygame.time.Clock()

assets = {
    'clouds': load_images('clouds'),
    'background': load_image('background.png'),
    'back': load_image('buttons/button_back.png'),
    'quit': load_image('buttons/button_quit.png'),
    'resume': load_image('buttons/button_resume.png'),
}

clouds = Clouds(assets['clouds'], count=16)

font = pygame.font.SysFont('comicsans', 60)

TEXT_COL = (0, 0, 0)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

pygame.mixer.music.load('data/music.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

run = True
while run:

    display.blit(assets['background'], (0, 0))

    clouds.update()
    clouds.render(display)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                import game

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

    draw_text('I want to be', font, TEXT_COL, 150, 80)
    draw_text('ninja', font, (255, 0, 0), 250, 155)
    draw_text('*press space to start*', pygame.font.SysFont('comicsans', 30), TEXT_COL, 160, 250)

    pygame.display.update()
    clock.tick(60)

pygame.quit()



