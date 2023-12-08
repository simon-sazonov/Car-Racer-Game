from abstract_class_power_up import PowerUp
import pygame


class InvincibilityPowerUp(PowerUp):
    def __init__(self, image, invincible_car_image, duration_ms=10000):
        super().__init__(image)
        self.invincible_car_image = invincible_car_image
        self.duration_ms = duration_ms
        self.timer_start_time = None

    def affect_player(self, player):
        player.invincible = True
        player.original_image = player.image  # Stores the original image
        invincible_image = pygame.image.load(self.invincible_car_image).convert_alpha()
        player.image = pygame.transform.scale(invincible_image, (player.width, player.height))
        self.timer_start_time = pygame.time.get_ticks()

    def affect_traffic(self, traffic):

        pass
