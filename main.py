import pygame, time, random
from pygame.locals import *

pygame.init()

# -- Global constants

# COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 20

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Walking Around ...")
clock = pygame.time.Clock()
spriteSheet = pygame.image.load("Assets/spriteSheet.png").convert_alpha()
image_up_list = [spriteSheet.subsurface(Rect(0, 120, 40, 40)),
                 spriteSheet.subsurface(Rect(40, 120, 40, 40)),
                 spriteSheet.subsurface(Rect(80, 120, 40, 40)),
                 spriteSheet.subsurface(Rect(120, 120, 40, 40)),
                 spriteSheet.subsurface(Rect(160, 120, 40, 40))]

image_down_list = [spriteSheet.subsurface(Rect(0, 0, 40, 40)),
                 spriteSheet.subsurface(Rect(40, 0, 40, 40)),
                 spriteSheet.subsurface(Rect(80, 0, 40, 40)),
                 spriteSheet.subsurface(Rect(120, 0, 40, 40)),
                 spriteSheet.subsurface(Rect(160, 0, 40, 40))]

image_left_list = [spriteSheet.subsurface(Rect(0, 40, 40, 40)),
                 spriteSheet.subsurface(Rect(40, 40, 40, 40)),
                 spriteSheet.subsurface(Rect(80, 40, 40, 40)),
                 spriteSheet.subsurface(Rect(120, 40, 40, 40)),
                 spriteSheet.subsurface(Rect(160, 40, 40, 40))]

image_right_list = [spriteSheet.subsurface(Rect(0, 80, 40, 40)),
                 spriteSheet.subsurface(Rect(40, 80, 40, 40)),
                 spriteSheet.subsurface(Rect(80, 80, 40, 40)),
                 spriteSheet.subsurface(Rect(120, 80, 40, 40)),
                 spriteSheet.subsurface(Rect(160, 80, 40, 40))]

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_down_list[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - self.rect.y - 100
        self.lives = 4
        self.current_image = 0
        self.timer = 0
        self.frame_duration = 250  # about 15 frames at 60 fps (250 is ms)

    def update(self, dt):

        # Animation timer
        self.timer += dt

        while self.timer >= self.frame_duration:
            self.timer = 0
            self.current_image = (self.current_image + 1) % 5

        # Movement
        self.speedX = 0
        self.speedY = 0

        if keystate[K_LEFT]:
            self.speedX = -1
        if keystate[K_RIGHT]:
            self.speedX = 1
        if keystate[K_UP]:
            self.speedY = -1
        if keystate[K_DOWN]:
            self.speedY = 1

        # Instead of
        # self.rect.x += self.speedX
        # self.rect.y += self.speedY

        # we do..
        self.rect.x = (self.rect.x + self.speedX * 5) % SCREEN_WIDTH
        self.rect.y = (self.rect.y + self.speedY * 5) % SCREEN_HEIGHT

        if self.rect.right > 600:
            self.rect.right = 600
        if self.rect.left < 0:
            self.rect.left = 0

        if self.speedX == 1:
            self.image = image_right_list[self.current_image]
        if self.speedX == -1:
            self.image = image_left_list[self.current_image]
        if self.speedY == 1:
            self.image = image_down_list[self.current_image]
        if self.speedY == -1:
            self.image = image_up_list[self.current_image]



player = Player()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
gameOn = True

while gameOn:

    clock.tick(FPS)

    keystate = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gameOn = False

    all_sprites_list.update(250)

    screen.fill(WHITE)
    all_sprites_list.draw(screen)

    pygame.display.flip()
