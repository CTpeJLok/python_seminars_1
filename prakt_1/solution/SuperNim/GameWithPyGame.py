import pygame
pygame.init()

width, height = 800, 600
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption('Игра "Супер ним"')

clock = pygame.time.Clock()
FPS = 30

IsGameRun = True
while IsGameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            IsGameRun = False

    clock.tick(FPS)