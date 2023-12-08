from abc import ABC, abstractmethod

import pygame

# Base model for the power ups
class PowerUp(ABC, pygame.sprite.Sprite):
    def __init__(self, image=None, color=(255, 255, 255)):
        super().__init__()

        self.radius = 25

        if image is None:
            # If no image is provided, create a colored circle
            self.image = pygame.Surface([self.radius * 2, self.radius * 2], pygame.SRCALPHA)
            self.color = color

            pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        else:
            # If an image is provided, load and scale the image
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))

        # Get the rectangular area of the power-up
        self.rect = self.image.get_rect()

    def move_down(self, pixels):
        self.rect.y += pixels

    @abstractmethod
    def affect_player(self, player):
        pass

    @abstractmethod
    def affect_traffic(self, traffic):
        pass
