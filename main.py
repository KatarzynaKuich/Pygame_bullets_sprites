import pygame, sys


# classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(white)
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((40, 10))  # how big bullet surface
        self.image.fill(yellow)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.x += 3  # move bullet speed


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 800
white = (255, 255, 255)
yellow = (255, 255, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Player and Bullet")

# mouse setup
pygame.mouse.set_visible(False)  # mouse not visible

# Creating the sprites and groups
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # on mouse click
            bullet_group.add(player.create_bullet())

    # Drawing
    screen.fill((0, 0, 0))

    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    pygame.display.flip()
    clock.tick(60)
