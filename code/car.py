import pygame

WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):

    def __init__(self, width, height, speed=0, image=None, color=(255, 255, 255)):

        super().__init__()
        if image == None:

            # If no image is provided, create a colored rectangle
            self.image = pygame.Surface([width, height])
            self.image.fill(WHITE)
            self.image.set_colorkey(WHITE)
            self.width = width
            self.height = height
            self.color = color

            pygame.draw.rect(self.image, color, [0, 0, width, height])
        else:
            # If an image is provided, load and scale the image
            self.width = width
            self.height = height
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.original_image = self.image.copy()      # To store the original image

        # Get the rectangular area of the car
        self.rect = self.image.get_rect()

        # Set the initial speed of the car
        self.speed = speed

        # Set the car to not be invincible
        self.invincible = False

        # To store the initial speed
        self.original_speed = speed

    def copy_car(self, another_car):
        self.width = another_car.width
        self.height = another_car.height
        self.image = pygame.transform.scale(another_car.image, (self.width, self.height))
        self.original_image = another_car.original_image.copy() if another_car.original_image else None
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.speed = another_car.speed
        self.invincible = another_car.invincible

    def moveRight(self, pixels):
        # Move the car to the right by the specified number of pixels
        self.rect.x += pixels

    def moveLeft(self, pixels):
        # Move the car to the left by the specified number of pixels
        self.rect.x -= pixels

    def moveUp(self, pixels):
        # Move the car upward by the specified number of pixels
        self.rect.y -= pixels

    def moveDown(self, playerCar_speed):
        # Move the car downward based on its speed and the player's car speed
        pixels = self.speed + playerCar_speed
        self.rect.y += pixels

    def repaint(self):
        # Repaint the car with a colored rectangle
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

    def reset_speed(self):
        # To reset to the original speed -- mainly for the slowing time power up
        self.speed = self.original_speed
