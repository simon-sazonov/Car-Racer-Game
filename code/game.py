import random

import colors
import game_over
import interface
import pygame
import shop
from bullet import Bullet
from button import Button
from car import Car
from road_lines import Line
from shooting_power_up import ShootingPowerUp
from size_reduction_power_up import SizeReductionPowerUp
from invincibility_power_up import InvincibilityPowerUp
from slowing_power_up import SlowingPowerUp

# Global variable for points
import global_variables

# Path to the default player car image
player_car_path = "assets/images/player_cars/player_car1.webp"

# Images for cars when power up is active:

invincible_car_path = "assets/images/player_cars/bullet_bill.webp"
slowing_car_path = "assets/images/player_cars/slow_time.webp"


# Function to initialize and run the game
def game():
    pygame.init()
    global_variables.all_points
    # Set up the game window
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing Game")

    # creating road lines
    lines = []
    for i in range(8):
        line = Line()
        line.rect.x = 260
        line.rect.y = i * 70
        lines.append(line)

        line2 = Line()
        line2.rect.x = 160
        line2.rect.y = i * 70
        lines.append(line2)

        line3 = Line()
        line3.rect.x = 360
        line3.rect.y = i * 70
        lines.append(line3)

    # player cars and background music depending on the car that user choose in the shop
    playerCar = None

    audio_path = "assets/sounds/default_song.mp3"

    if player_car_path == "assets/images/player_cars/player_car1.webp":  # fiat multipla
        playerCar = Car(45, 80, image=player_car_path)
        audio_path = "assets/sounds/default_song.mp3"
    if player_car_path == "assets/images/player_cars/player_car2.webp":  # delorean
        playerCar = Car(35, 83, image=player_car_path)
        audio_path = "assets/sounds/the_back_to_the_future_theme.mp3"
    if player_car_path == "assets/images/player_cars/player_car3.webp":  # Dodge charger 1969
        playerCar = Car(35, 80, image=player_car_path)
        audio_path = "assets/sounds/bandolero.mp3"
    if player_car_path == "assets/images/player_cars/player_car7.webp":  # Supra
        playerCar = Car(35, 81, image=player_car_path)
        audio_path = "assets/sounds/DejaVu.mp3"
    if player_car_path == "assets/images/player_cars/player_car6.webp":  # f1
        playerCar = Car(35, 85, image=player_car_path)
        audio_path = "assets/sounds/max_super_max.mp3"

    # Load and play the background music
    pygame.mixer.music.load(audio_path)          # loads audio to the mixer
    pygame.mixer.music.play(-1)              # Plays the music indefinitely

    # Set initial position for the player car
    playerCar.rect.x = 150
    playerCar.rect.y = 300
    player_car_speed1 = 4

    # create enemy cars
    car1 = Car(40, 80, 3, image="assets/images/enemies_cars/enemy2.webp")
    car1.rect.x = 200
    car1.rect.y = -2100

    car2 = Car(40, 100, 1, image="assets/images/enemies_cars/enemy4.webp")
    car2.rect.x = 100
    car2.rect.y = -2321

    car3 = Car(40, 70, 5, image="assets/images/enemies_cars/enemy3.webp")
    car3.rect.x = 300
    car3.rect.y = -2788

    car4 = Car(40, 85, 7, image="assets/images/enemies_cars/enemy1.webp")
    car4.rect.x = 400
    car4.rect.y = -2812

    car5 = Car(40, 80, 3, image="assets/images/enemies_cars/enemy5.webp")
    car5.rect.x = 200
    car5.rect.y = -2200

    car6 = Car(40, 100, 1, image="assets/images/enemies_cars/enemy6.webp")
    car6.rect.x = 100
    car6.rect.y = -2621

    car7 = Car(40, 70, 5, image="assets/images/enemies_cars/enemy7.webp")
    car7.rect.x = 300
    car7.rect.y = -2888

    car8 = Car(40, 85, 7, image="assets/images/enemies_cars/enemy8.webp")
    car8.rect.x = 400
    car8.rect.y = -2912

    car9 = Car(40, 70, 5, image="assets/images/enemies_cars/enemy9.webp")
    car9.rect.x = 300
    car9.rect.y = -2900

    car10 = Car(40, 85, 7, image="assets/images/enemies_cars/enemy10.webp")
    car10.rect.x = 400
    car10.rect.y = -2412

    car11 = Car(40, 80, 3, image="assets/images/enemies_cars/enemy12.webp")
    car11.rect.x = 200
    car11.rect.y = -2400

    car12 = Car(40, 100, 1, image="assets/images/enemies_cars/enemy11.webp")
    car12.rect.x = 100
    car12.rect.y = -2721

    # Creating shooting power Up
    shooting_power_up = ShootingPowerUp(image="assets/images/power_ups/shooting.webp")
    shooting_power_up.rect.x = 150
    shooting_power_up.rect.y = -21

    # Creating reduction power Up
    size_reduction_power_up = SizeReductionPowerUp(image="assets/images/power_ups/size_reduction.webp")
    size_reduction_power_up.rect.x = 250
    size_reduction_power_up.rect.y = -341

    # Creating bullets
    bullet1 = Bullet(10, 20, image="assets/images/power_ups/bullet.webp")
    bullet1.rect.y = 600

    # Creating the Invincibility Power Up:
    invincibility_power_up = InvincibilityPowerUp(image="assets/images/power_ups/invincibility.webp",
                                                  invincible_car_image=invincible_car_path)
    invincibility_power_up.rect.x = 150
    invincibility_power_up.rect.y = -420

    # Adding the music for the invincibility power up
    invincibility_sound_file = "assets/sounds/mario_kart_star.mp3"

    # Creating the Slowing Time power up:
    slowing_power_up = SlowingPowerUp(image="assets/images/power_ups/slowing_time.webp",
                                      slowing_car_image=slowing_car_path)
    slowing_power_up.rect.x = 300
    slowing_power_up.rect.y = -500

    # Creating a flag for when the slowing power up is active
    slowing_power_up_active = False

    # making groups for road lines, enemies_cars, power ups and all sprites
    all_sprites_list = pygame.sprite.Group()
    list_of_lines = pygame.sprite.Group()
    list_of_power_ups = pygame.sprite.Group()
    incoming_cars_list = pygame.sprite.Group()

    incoming_cars_list.add(car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12)
    list_of_power_ups.add(shooting_power_up, size_reduction_power_up, invincibility_power_up, slowing_power_up)

    for the_line in lines:
        list_of_lines.add(the_line)
        all_sprites_list.add(the_line)
    all_sprites_list.add(shooting_power_up, size_reduction_power_up, invincibility_power_up, slowing_power_up, car1,
                         car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12, playerCar, bullet1)

    # Initialize Pygame mixer for audio playback
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)

    # Set starting time for the game timer
    start_time = pygame.time.get_ticks()

    # each new game the score = 0
    point_for_game = 0

    # settings for fonts
    font_path = "assets/fonts/retro_font.ttf"
    font_size = 15
    font = pygame.font.Font(font_path, font_size)

    # text for buttons
    text_quit = font.render('Quit', True, colors.colors['MATRIXGREEN'])
    text_shop = font.render('Shop', True, colors.colors['MATRIXGREEN'])

    # position of buttons
    button_quit_position = [540, 50, 80, 30]
    button_shop_position = [540, 100, 80, 30]

    # Create button objects
    button_quit = Button(screen, button_quit_position, text_with_font_color=text_quit)

    button_shop = Button(screen, button_shop_position, text_with_font_color=text_shop)

    # Power-up loading bar
    loading_bar_width = 80
    loading_bar_height = 20
    loading_bar_rect = pygame.Rect(540, 400, 0, loading_bar_height)
    border_color = colors.colors["DARKGREEN"]
    border_rect = pygame.Rect(540, 400, loading_bar_width, loading_bar_height)

    # Game loop
    carryOn = True
    clock = pygame.time.Clock()

    # Duration of power ups
    timer_duration_for_power_ups = 10000

    # Used as a marker is power-up started and when
    power_up_start_time = 0

    # Copy of original car so that we can return our car to basic settings after power up
    original_playerCar = Car(70, 40, 8)
    original_playerCar.copy_car(playerCar)

    # This used as a markers for shooting power up
    TANK_MODE = False
    reloading = False
    while carryOn:

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Event handling
        for event in pygame.event.get():

            # settings for quitting
            if event.type == pygame.QUIT:
                carryOn = False

            # settings for clicking
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Play click sound
                additional_sound_path = "assets/sounds/button.mp3"
                additional_sound = pygame.mixer.Sound(additional_sound_path)
                additional_sound.play()

                # buttons events
                if button_quit.is_button_pressed():
                    global_variables.all_points += round(point_for_game)
                    carryOn = False
                    pygame.mixer.music.stop()
                    interface.interface()
                if button_shop.is_button_pressed():
                    global_variables.all_points += round(point_for_game)
                    carryOn = False
                    pygame.mixer.music.stop()
                    shop.shop_window()

        # Update the display after handling collisions
        pygame.display.update()
        current_time = pygame.time.get_ticks()
        # Timer-point_for_game
        elapsed_time = current_time - start_time

        # Calculate point_for_game based on time and speed
        point_for_game += (elapsed_time / 1000) * player_car_speed1 * 0.006

        # Display the point_for_game*speed
        text_score = font.render(f"Score: {int(point_for_game)}", True, colors.colors['BLACK'])

        # Player car controls
        keys = pygame.key.get_pressed()
        if playerCar.rect.left > 60:
            if keys[pygame.K_a]:
                playerCar.rect.move_ip(-5, 0)
        if playerCar.rect.right < 460:
            if keys[pygame.K_d]:
                playerCar.rect.move_ip(5, 0)
        if keys[pygame.K_w] and player_car_speed1 < 10:
            player_car_speed1 += 0.1
        if keys[pygame.K_s] and player_car_speed1 > 1:
            player_car_speed1 -= 0.1

        # Draw the  background
        draw_striped_background(screen)

        # shooting system for TANK MODE
        if keys[pygame.K_LSHIFT] and reloading is False and TANK_MODE:
            # Sound affect when tank is shooting
            additional_sound_path = "assets/sounds/pew.mp3"
            additional_sound = pygame.mixer.Sound(additional_sound_path)
            additional_sound.play()
            bullet1.rect.x = playerCar.rect.x + (playerCar.width - bullet1.width) / 2
            bullet1.rect.y = playerCar.rect.y

        # Spawn bullets iff the bullet destroyed the car or went out of the screen
        reloading = spawn_bullet(bullet1, incoming_cars_list, reloading)

        # Update sprites
        all_sprites_list.update()

        # Draw background and lines

        pygame.draw.rect(screen, colors.colors['ASPHALTGRAY'], [60, 0, 400, 500])
        pygame.draw.line(screen, colors.colors['BRICK'], (60, 0), (60, 500), 20)
        pygame.draw.line(screen, colors.colors['BRICK'], (460, 0), (460, 500), 20)

        # Draw buttons
        button_quit.draw_button(mouse)
        button_shop.draw_button(mouse)


        # Draw power_ups if there is no activated yet
        if power_up_start_time == 0:
            draw_power_ups(list_of_power_ups, player_car_speed1)

        # Update and draw road lines
        draw_lines(list_of_lines, player_car_speed1)

        # Spawn new cars
        spawn_cars(incoming_cars_list, player_car_speed1)

        # Draw all sprites
        all_sprites_list.draw(screen)

        screen.blit(text_score, (215, 50))


        # Check for collision with power ups
        collided_power_ups = pygame.sprite.spritecollide(playerCar, list_of_power_ups, dokill=False)

        # Iterate through the collided power-ups if power-up started
        if power_up_start_time == 0 and collided_power_ups:
            for power_up in collided_power_ups:
                # Setting the time beginning of power up
                power_up_start_time = pygame.time.get_ticks()

                # To play the invincibility music
                if isinstance(power_up, InvincibilityPowerUp):
                    pygame.mixer.music.unload()     # removes background music from mixer
                    pygame.mixer.music.load(invincibility_sound_file)   # add invincibility power up music
                    pygame.mixer.music.play(-1)     # Start playing the power-up sound

                # Rewriting the player
                all_sprites_list.remove(playerCar)
                power_up.affect_player(playerCar)
                all_sprites_list.add(playerCar)

                # if power up is a shooting turning on the tank mode
                if isinstance(power_up, ShootingPowerUp):
                    TANK_MODE = True

                if isinstance(power_up, SlowingPowerUp):
                    power_up.affect_traffic(incoming_cars_list)
                    slowing_power_up_active = True

            # removing the power up square from the view
            for power_up in list_of_power_ups:
                power_up.rect.y = 600

        # code after power up finished(when power-up time is out)
        if current_time - power_up_start_time >= timer_duration_for_power_ups and power_up_start_time != 0:
            # Stop invincibility sound and resume background music if invincibility power-up was active
            if playerCar.invincible:
                pygame.mixer.music.unload()     # this unloads the invincibility sound
                pygame.mixer.music.load(audio_path)     # returns the background sound
                pygame.mixer.music.play(-1)     # Start playing the background sound

            if slowing_power_up_active:
                for car in incoming_cars_list:
                    car.reset_speed()
                slowing_power_up_active = False

            # Returning the player car as it was before power up
            all_sprites_list.remove(playerCar)
            playerCar.copy_car(original_playerCar)
            all_sprites_list.add(playerCar)

            all_sprites_list.update()
            # power up is off
            power_up_start_time = 0
            TANK_MODE = False
            playerCar.invincible = False

        # loading bar for power ups
        if power_up_start_time != 0:
            loading_bar_rect.width = min(loading_bar_width - (
                    (current_time - power_up_start_time) / timer_duration_for_power_ups) * loading_bar_width,
                                         loading_bar_width)
            pygame.draw.rect(screen, border_color, border_rect)
            pygame.draw.rect(screen, colors.colors["MATRIXGREEN"], loading_bar_rect)

    # Check for collision with enemy cars
        # If player is invincible, check for collisions and move collided cars off-screen
        if playerCar.invincible:
            collided_cars = pygame.sprite.spritecollide(playerCar, incoming_cars_list, dokill=False)
            for car in collided_cars:
                car.rect.y = -1000   # Visually, this makes the cars that were hit disappear

        # If player is not invincible, game ends upon collision with enemy cars
        elif pygame.sprite.spritecollideany(playerCar, incoming_cars_list):
            pygame.display.update()
            for entity in all_sprites_list:
                entity.kill()
            global_variables.all_points += round(point_for_game)
            carryOn = False
            pygame.mixer.music.stop()
            game_over.loss_video()
            # Update the display to show the changes made in the current frame
        pygame.display.flip()

        # Check if background music is not currently playing, and if so, start playing it
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

        clock.tick(60)

    pygame.quit()


# Function that is spawning bullets and delete the cars that collide with the bullet
def spawn_bullet(bullet, incoming_cars_list, reloading):
    if 0 < bullet.rect.y < 500:
        bullet.move_up()
        reloading = True
    collided_bullet_and_car = pygame.sprite.spritecollide(bullet, incoming_cars_list, dokill=False)
    if bullet.rect.y <= 0 or collided_bullet_and_car:
        for destroyed_car in collided_bullet_and_car:
            destroyed_car.rect.y = 600
        bullet.rect.y = 600
        reloading = False
    return reloading


def draw_striped_background(screen, stripe_height=75):
    screen_height = screen.get_height()
    for y in range(0, screen_height, stripe_height * 2):
        pygame.draw.rect(screen, colors.colors['LIGHTGREEN'], (0, y, 700, stripe_height))
        pygame.draw.rect(screen, colors.colors['MEDIUMGREEN'], (0, y + stripe_height, 700, stripe_height))


# Function that is drawing the power ups to the road
def draw_power_ups(power_ups, player_car_speed):
    for power_up in power_ups:
        power_up.move_down(player_car_speed)
        # Reset the road line to the top of the screen and repaint it to create the illusion of continuous road
        if power_up.rect.y >= 500:
            # Shooting power up probability
            if isinstance(power_up, ShootingPowerUp):
                power_up.rect.y = random.randrange(-2500, -5, 243)
                power_up.rect.x = random.randrange(60, 460 - power_up.radius * 2)

            # SizeReduction power up probability
            elif isinstance(power_up, SizeReductionPowerUp):
                power_up.rect.y = random.randrange(-500, -5, 243)
                power_up.rect.x = random.randrange(60, 460 - power_up.radius * 2)

            # Invincibility Power Up probability
            elif isinstance(power_up, InvincibilityPowerUp):
                power_up.rect.y = random.randrange(-3000, -5, 486)  # Larger range means the spawn rate is lower
                power_up.rect.x = random.randrange(60, 460 - power_up.radius * 2)

            # Slowing Time Down Probability
            elif isinstance(power_up, SlowingPowerUp):
                power_up.rect.y = random.randrange(-750, -5, 243)
                power_up.rect.x = random.randrange(60, 460 - power_up.radius * 2)


# Move each road line down based on the player's car speed
# If a road line reaches the bottom of the screen, reset it to the top and repaint it
def draw_lines(lines, player_car_speed):
    for line in lines:
        line.move_down(player_car_speed)
        # Reset the road line to the top of the screen and repaint it to create the illusion of continuous road
        if line.rect.y >= 500:
            line.repaint()
            line.rect.y = -50


# Move each incoming car down based on the player's car speed
# If a road line reaches the bottom of the screen, reset it to the top randomly avoiding overlapping
def spawn_cars(incoming_cars_list, player_car_speed):
    for car in incoming_cars_list:
        car.moveDown(player_car_speed)

        # Check if the car has reached the bottom of the screen
        if car.rect.y >= 500:

            # Depending on the x-coordinate of the car, reposition it to avoid overlapping with other cars
            if 60 <= car.rect.x < 160:
                function_to_avoid_spawning_cars_on_cars(car, 60, incoming_cars_list)
            if 160 <= car.rect.x < 260:
                function_to_avoid_spawning_cars_on_cars(car, 160, incoming_cars_list)
            if 260 <= car.rect.x < 360:
                function_to_avoid_spawning_cars_on_cars(car, 260, incoming_cars_list)
            if 360 <= car.rect.x < 460:
                function_to_avoid_spawning_cars_on_cars(car, 360, incoming_cars_list)


def function_to_avoid_spawning_cars_on_cars(the_car1, position_of_line, incoming_cars_list):
    k = True

    # Remove the car from the list temporarily to avoid self-collision check
    incoming_cars_list.remove(the_car1)

    # Keep attempting to reposition the car until a collision-free position is found
    while k:

        # Randomly set the x and y coordinates within the specified range and range for y-coordinate
        the_car1.rect.x = random.randint(position_of_line, position_of_line + 100 - the_car1.width)
        the_car1.rect.y = random.randrange(-10000, -5, 243)

        # Check for collisions with other incoming cars
        if pygame.sprite.spritecollideany(the_car1, incoming_cars_list) is None:
            # If no collision, add the car back to the list and break out of the loop
            incoming_cars_list.add(the_car1)
            break
