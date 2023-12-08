from abstract_class_power_up import PowerUp
import pygame


class SlowingPowerUp(PowerUp):
    def __init__(self, image, slowing_car_image, duration_ms=10000):
        super().__init__(image)
        self.slowing_car_image = slowing_car_image
        self.duration_ms = duration_ms

    def affect_player(self, player):
        # The power up itself doesn't really affect the player,
        # The only thing is to change the player car when the power up once activated
        scale_factor = 1.2
        new_width = int(player.width * scale_factor)
        new_height = int(player.height * scale_factor)      # Only because original image looked too small

        slowing_image = pygame.image.load(self.slowing_car_image).convert_alpha()
        player.image = pygame.transform.scale(slowing_image, (new_width, new_height))

    def affect_traffic(self, traffic):
        for car in traffic:
            if not hasattr(car, 'original_speed'):
                car.original_speed = car.speed
            car.speed /= 4  # 1/4 of the speed
