import pygame
from abstract_class_power_up import PowerUp


class ShootingPowerUp(PowerUp):
    def affect_player(self, player_car):
        self.player_picture = player_car.image
        player_car.image = pygame.image.load("assets/images/player_cars/tank.webp")
        player_car.image = pygame.transform.scale(player_car.image, (player_car.width, player_car.height))

    def affect_traffic(self, traffic):
        pass
