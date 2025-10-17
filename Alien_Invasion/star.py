import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load and scale down the star image
        original_image = pygame.image.load('images/star.png')
        self.image = pygame.transform.scale(original_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.x = float(self.rect.x)