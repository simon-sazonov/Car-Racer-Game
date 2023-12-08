import pygame

image_background_color = (0, 0, 0)


class Line(pygame.sprite.Sprite):

    def __init__(self, width=5, height=50, color=image_background_color):
        super().__init__()

        self.width = width
        self.height = height
        self.color = color

        # Create a surface for the line and set color key for transparency
        self.image = pygame.Surface([width, height])
        self.image.fill(image_background_color)
        self.image.set_colorkey(image_background_color)

        # Draw a colored rectangle on the surface
        pygame.draw.rect(self.image, self.color, [0, 0, width, height])

        # Get the rectangular area of the line
        self.rect = self.image.get_rect()

    def move_down(self, player_car_speed):
        # Move the line downward based on the player's car speed
        pixels = player_car_speed
        self.rect.y += pixels

    def repaint(self):
        # Repaint the line
        pygame.draw.rect(self.image, (255, 255, 255), [0, 0, self.width, self.height])
