import pygame
import colors

class Button:
    def __init__(self, screen, position, text_with_font_color=None, picture_path=None):

        # Initialize Button object with position, text, font color, and picture path
        self.mouse_y = None
        self.mouse_x = None
        x, y, width, height = position
        self.position = position
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.picture_path = picture_path

        # If text_with_font_color is not provided, use default values
        if text_with_font_color is None:
            # Default text and font color
            default_font = pygame.font.SysFont('PetMe', 1)
            text_with_font_color = default_font.render('', True, (0, 0, 0))
        self.text_with_font_color = text_with_font_color

    def draw_button(self, mouse):

        # Draw the button on the screen with the given mouse position
        mouse_x, mouse_y = mouse
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

        # Set alpha value based on mouse position
        alpha = 0
        if self.x <= self.mouse_x <= self.x + self.width and self.y <= self.mouse_y <= self.y + self.height:
            alpha = 150  # Make it whiter when the mouse is over the button

        # Create a transparent surface for the button
        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, (colors.colors['GREY'][0],colors.colors['GREY'][1],colors.colors['GREY'][2], alpha),
                         (0, 0, self.width, self.height))

        # Draw the button surface onto the screen
        self.screen.blit(button_surface, (self.x, self.y))

        # If a picture_path is provided, load and draw the image on the button
        if self.picture_path:
            button_image = pygame.image.load(self.picture_path)
            button_image = pygame.transform.scale(button_image, (self.width, self.height))
            self.screen.blit(button_image, (self.x, self.y))

        # Calculate center of the button
        center_x, center_y = self.x + self.width // 2, self.y + self.height // 2

        # Center the text
        text_rect = self.text_with_font_color.get_rect(center=(center_x, center_y))

        # Draw the text on the button
        self.screen.blit(self.text_with_font_color, text_rect.topleft)

    def is_button_pressed(self):
        # Check if the button is pressed by comparing mouse coordinates with button coordinates
        return self.x <= self.mouse_x <= self.x + self.width \
               and self.y <= self.mouse_y <= self.y + self.height
