import pygame
from abstract_class_power_up import PowerUp


class SizeReductionPowerUp(PowerUp):
    def affect_player(self, player_car):
        self.player_width = player_car.width
        self.player_height = player_car.height
        self.player_picture = player_car.image
        player_car.width = self.player_width*0.5
        player_car.height = self.player_height*0.5
        player_car.image = pygame.transform.scale(self.player_picture, (player_car.width, player_car.height))
        player_car.rect = player_car.image.get_rect(topleft=player_car.rect.topleft)

    def affect_traffic(self, traffic):
        pass
