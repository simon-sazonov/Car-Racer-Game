import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, width, height, image):
        super().__init__()
        # If an image is provided, load and scale the image
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Get the rectangular area of the car
        self.rect = self.image.get_rect()

        # Set the initial speed of the car
        self.speed = 10

    def move_up(self):
        # Move the car upward by the specified number of pixels
        self.rect.y -= self.speed
