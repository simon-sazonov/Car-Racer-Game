import os
import random

import pygame

import colors
import game_over
import interface
import shop_multi
from bullet import Bullet
from button import Button
from car import Car
from invincibility_power_up import InvincibilityPowerUp
from road_lines import Line
from shooting_power_up import ShootingPowerUp
from size_reduction_power_up import SizeReductionPowerUp
from slowing_power_up import SlowingPowerUp

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Path to the default player car image
player_car_path1 = "assets/images/player_cars/player_car1.webp"
player_car_path2 = "assets/images/player_cars/player_car1.webp"

# Images for cars when power up is active:

invincible_car_path = "assets/images/player_cars/bullet_bill.webp"
slowing_car_path = "assets/images/player_cars/slow_time.webp"


# Function to initialize and run the game
def multi_game():
    pygame.init()

    # Set up the game window
    size = (1400, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing Game")

    font_path = "assets/fonts/retro_font.ttf"
    font_size = 11
    p1_font_size = 11  # Size for the "P1" label
    font = pygame.font.Font(font_path, font_size)
    p1_font = pygame.font.Font(font_path, p1_font_size)
    p2_font_size = 11
    p2_font = pygame.font.Font(font_path, p2_font_size)

    # creating road lines
    lines_left = []
    for i in range(8):
        line = Line()
        line.rect.x = 260
        line.rect.y = i * 70
        lines_left.append(line)

        line2 = Line()
        line2.rect.x = 160
        line2.rect.y = i * 70
        lines_left.append(line2)

        line3 = Line()
        line3.rect.x = 360
        line3.rect.y = i * 70
        lines_left.append(line3)

    lines_right = []
    for i in range(8):
        line4 = Line()
        line4.rect.x = 1040
        line4.rect.y = i * 70
        lines_right.append(line4)

        line5 = Line()
        line5.rect.x = 1140
        line5.rect.y = i * 70
        lines_right.append(line5)

        line6 = Line()
        line6.rect.x = 1240
        line6.rect.y = i * 70
        lines_right.append(line6)

    # player cars and background music depending on the car that user choose in the shop
    playerCar1 = None
    playerCar2 = None
    audio_path = "assets/sounds/default_song.mp3"

    if player_car_path1 == "assets/images/player_cars/player_car1.webp":  # fiat multipla
        playerCar1 = Car(45, 80, image=player_car_path1)
        audio_path = "assets/sounds/default_song.mp3"
    if player_car_path1 == "assets/images/player_cars/player_car2.webp":  # delorean
        playerCar1 = Car(35, 83, image=player_car_path1)
        audio_path = "assets/sounds/the_back_to_the_future_theme.mp3"
    if player_car_path1 == "assets/images/player_cars/player_car3.webp":  # Dodge charger 1969
        playerCar1 = Car(35, 80, image=player_car_path1)
        audio_path = "assets/sounds/bandolero.mp3"
    if player_car_path1 == "assets/images/player_cars/player_car7.webp":  # Supra
        playerCar1 = Car(35, 81, image=player_car_path1)
        audio_path = "assets/sounds/DejaVu.mp3"
    if player_car_path1 == "assets/images/player_cars/player_car6.webp":  # f1
        playerCar1 = Car(35, 85, image=player_car_path1)
        audio_path = "assets/sounds/max_super_max.mp3"

    if player_car_path2 == "assets/images/player_cars/player_car1.webp":  # fiat multipla
        playerCar2 = Car(45, 80, image=player_car_path2)
        audio_path = "assets/sounds/default_song.mp3"
    if player_car_path2 == "assets/images/player_cars/player_car2.webp":  # delorean
        playerCar2 = Car(35, 83, image=player_car_path2)
        audio_path = "assets/sounds/the_back_to_the_future_theme.mp3"
    if player_car_path2 == "assets/images/player_cars/player_car3.webp":  # Dodge charger 1969
        playerCar2 = Car(35, 80, image=player_car_path2)
        audio_path = "assets/sounds/bandolero.mp3"
    if player_car_path2 == "assets/images/player_cars/player_car7.webp":  # Supra
        playerCar2 = Car(35, 81, image=player_car_path2)
        audio_path = "assets/sounds/DejaVu.mp3"
    if player_car_path2 == "assets/images/player_cars/player_car6.webp":  # f1
        playerCar2 = Car(35, 85, image=player_car_path2)
        audio_path = "assets/sounds/max_super_max.mp3"

    # Load and play the background music
    pygame.mixer.music.load(audio_path)  # loads audio to the mixer
    pygame.mixer.music.play(-1)  # Plays the music indefinitely

    # Set initial position for the player car
    playerCar1.rect.x = 150
    playerCar1.rect.y = 300
    player_car_speed1 = 4

    playerCar2.rect.x = 1180
    playerCar2.rect.y = 300
    player_car_speed2 = 4

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

    car13 = Car(40, 80, 3, image="assets/images/enemies_cars/enemy2.webp")
    car13.rect.x = 1080
    car13.rect.y = -2100

    car14 = Car(40, 100, 1, image="assets/images/enemies_cars/enemy4.webp")
    car14.rect.x = 980
    car14.rect.y = -2321

    car15 = Car(40, 70, 5, image="assets/images/enemies_cars/enemy3.webp")
    car15.rect.x = 1180
    car15.rect.y = -2788

    car16 = Car(40, 85, 7, image="assets/images/enemies_cars/enemy1.webp")
    car16.rect.x = 1300
    car16.rect.y = -2812

    car17 = Car(40, 80, 3, image="assets/images/enemies_cars/enemy5.webp")
    car17.rect.x = 1080
    car17.rect.y = -2200

    car18 = Car(40, 100, 1, image="assets/images/enemies_cars/enemy6.webp")
    car18.rect.x = 980
    car18.rect.y = -2621

    car19 = Car(40, 70, 5, image="assets/images/enemies_cars/enemy7.webp")
    car19.rect.x = 1180
    car19.rect.y = -2888

    car20 = Car(40, 85, 7, image="assets/images/enemies_cars/enemy8.webp")
    car20.rect.x = 1300
    car20.rect.y = -2912

    car21 = Car(40, 70, 5, image="assets/images/enemies_cars/enemy9.webp")
    car21.rect.x = 1180
    car21.rect.y = -2900

    car22 = Car(40, 85, 7, image="assets/images/enemies_cars/enemy10.webp")
    car22.rect.x = 1300
    car22.rect.y = -2412

    car23 = Car(40, 80, 3, image="assets/images/enemies_cars/enemy12.webp")
    car23.rect.x = 1080
    car23.rect.y = -2400

    car24 = Car(40, 100, 1, image="assets/images/enemies_cars/enemy11.webp")
    car24.rect.x = 980
    car24.rect.y = -2721

    # Creating shooting power Up
    shooting_power_up1 = ShootingPowerUp(image="assets/images/power_ups/shooting.webp")
    shooting_power_up1.rect.x = 150
    shooting_power_up1.rect.y = -21

    shooting_power_up2 = ShootingPowerUp(image="assets/images/power_ups/shooting.webp")
    shooting_power_up2.rect.x = 1030
    shooting_power_up2.rect.y = -21

    # Creating reduction power Up
    size_reduction_power_up1 = SizeReductionPowerUp(image="assets/images/power_ups/size_reduction.webp")
    size_reduction_power_up1.rect.x = 250
    size_reduction_power_up1.rect.y = -341

    size_reduction_power_up2 = SizeReductionPowerUp(image="assets/images/power_ups/size_reduction.webp")
    size_reduction_power_up2.rect.x = 1130
    size_reduction_power_up2.rect.y = -341

    # Creating bullets
    bullet1 = Bullet(10, 20, image="assets/images/power_ups/bullet.webp")
    bullet1.rect.y = 600

    bullet2 = Bullet(10, 20, image="assets/images/power_ups/bullet.webp")
    bullet2.rect.y = 600

    # Creating the Invincibility Power Up:
    invincibility_power_up1 = InvincibilityPowerUp(image="assets/images/power_ups/invincibility.webp",
                                                   invincible_car_image=invincible_car_path)
    invincibility_power_up1.rect.x = 150
    invincibility_power_up1.rect.y = -420

    invincibility_power_up2 = InvincibilityPowerUp(image="assets/images/power_ups/invincibility.webp",
                                                   invincible_car_image=invincible_car_path)
    invincibility_power_up2.rect.x = 1030
    invincibility_power_up2.rect.y = -420

    # Adding the music for the invincibility power up
    invincibility_sound_file = "assets/sounds/mario_kart_star.mp3"

    # Creating the Slowing Time power up:
    slowing_power_up1 = SlowingPowerUp(image="assets/images/power_ups/slowing_time.webp",
                                       slowing_car_image=slowing_car_path)
    slowing_power_up1.rect.x = 300
    slowing_power_up1.rect.y = -500

    slowing_power_up2 = SlowingPowerUp(image="assets/images/power_ups/slowing_time.webp",
                                       slowing_car_image=slowing_car_path)
    slowing_power_up2.rect.x = 1230
    slowing_power_up2.rect.y = -500

    # Creating a flag for when the slowing power up is active
    slowing_power_up_active = False

    # making groups for road lines, enemies_cars, power ups and all sprites
    all_sprites_list = pygame.sprite.Group()
    list_of_lines = pygame.sprite.Group()
    list_of_power_ups1 = pygame.sprite.Group()
    list_of_power_ups2 = pygame.sprite.Group()
    incoming_cars_list1 = pygame.sprite.Group()
    incoming_cars_list2 = pygame.sprite.Group()

    incoming_cars_list1.add(car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12, )
    incoming_cars_list2.add(car13, car14, car15, car16, car17, car18, car19, car20, car21, car22, car23, car24)

    list_of_power_ups1.add(shooting_power_up1, size_reduction_power_up1, invincibility_power_up1, slowing_power_up1)

    list_of_power_ups2.add(shooting_power_up2, size_reduction_power_up2, invincibility_power_up2, slowing_power_up2)

    for the_line_l in lines_left:
        list_of_lines.add(the_line_l)
        all_sprites_list.add(the_line_l)

    for the_line_r in lines_right:
        list_of_lines.add(the_line_r)
        all_sprites_list.add(the_line_r)

    all_sprites_list.add(shooting_power_up1, size_reduction_power_up1, invincibility_power_up1, slowing_power_up1,
                         shooting_power_up2, size_reduction_power_up2, invincibility_power_up2, slowing_power_up2,
                         car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12,
                         car13, car14, car15, car16, car17, car18, car19, car20, car21, car22, car23, car24,
                         playerCar1, playerCar2, bullet1, bullet2)

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
    button_quit_position = [660, 50, 80, 30]
    button_shop_position = [660, 100, 80, 30]

    # Create button objects
    button_quit = Button(screen, button_quit_position, text_with_font_color=text_quit)
    button_shop = Button(screen, button_shop_position, text_with_font_color=text_shop)

    # Power-up loading bar
    loading_bar_width1 = 80
    loading_bar_height1 = 20
    loading_bar_rect1 = pygame.Rect(660, 320, 0, loading_bar_height1)
    border_color1 = colors.colors["DARKGREEN"]
    border_rect1 = pygame.Rect(660, 320, loading_bar_width1, loading_bar_height1)

    # Power-up loading bar
    loading_bar_width2 = 80
    loading_bar_height2 = 20
    loading_bar_rect2 = pygame.Rect(660, 380, 0, loading_bar_height2)
    border_color2 = colors.colors["BLUE"]
    border_rect2 = pygame.Rect(660, 380, loading_bar_width2, loading_bar_height2)

    # Game loop
    carryOn = True
    clock = pygame.time.Clock()

    # Duration of power ups
    timer_duration_for_power_ups = 10000

    # Used as a marker is power-up started and when
    power_up_start_time1 = 0
    power_up_start_time2 = 0

    # Copy of original car so that we can return our car to basic settings after power up
    original_playerCar1 = Car(70, 40, 8)
    original_playerCar1.copy_car(playerCar1)

    original_playerCar2 = Car(70, 40, 8)
    original_playerCar2.copy_car(playerCar2)

    # This used as a markers for shooting power up
    TANK_MODE1 = False
    TANK_MODE2 = False
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
                    carryOn = False
                    pygame.mixer.music.stop()
                    interface.interface()
                if button_shop.is_button_pressed():
                    carryOn = False
                    pygame.mixer.music.stop()
                    shop_multi.shop_window_multi()

        # Update the display after handling collisions
        pygame.display.update()
        current_time = pygame.time.get_ticks()
        # Timer-point_for_game
        elapsed_time = current_time - start_time

        # Calculate point_for_game based on time and speed
        point_for_game += (elapsed_time / 1000) * player_car_speed1 * 0.006

        # Player car controls
        keys = pygame.key.get_pressed()
        if playerCar1.rect.left > 60:
            if keys[pygame.K_a]:
                playerCar1.rect.move_ip(-5, 0)
        if playerCar1.rect.right < 460:
            if keys[pygame.K_d]:
                playerCar1.rect.move_ip(5, 0)
        if keys[pygame.K_w] and player_car_speed1 < 10:
            player_car_speed1 += 0.1
        if keys[pygame.K_s] and player_car_speed1 > 1:
            player_car_speed1 -= 0.1

        if playerCar2.rect.left > 940:
            if keys[pygame.K_LEFT]:
                playerCar2.rect.move_ip(-5, 0)
        if playerCar2.rect.right < 1340:
            if keys[pygame.K_RIGHT]:
                playerCar2.rect.move_ip(5, 0)
        if keys[pygame.K_UP] and player_car_speed2 < 10:
            player_car_speed2 += 0.1
        if keys[pygame.K_DOWN] and player_car_speed2 > 1:
            player_car_speed2 -= 0.1

        # Draw the  background
        draw_striped_background(screen)

        # Spawn bullets iff the bullet destroyed the car or went out of the screen
        reloading1 = spawn_bullet(bullet1, incoming_cars_list1, reloading)

        reloading2 = spawn_bullet(bullet2, incoming_cars_list2, reloading)

        # shooting system for TANK MODE
        if keys[pygame.K_RSHIFT] and reloading2 is False and TANK_MODE2:
            # Sound affect when tank is shooting
            additional_sound_path = "assets/sounds/pew.mp3"
            additional_sound = pygame.mixer.Sound(additional_sound_path)
            additional_sound.play()
            bullet2.rect.x = playerCar2.rect.x + (playerCar2.width - bullet2.width) / 2
            bullet2.rect.y = playerCar2.rect.y

        if keys[pygame.K_LSHIFT] and reloading1 is False and TANK_MODE1:
            # Sound affect when tank is shooting
            additional_sound_path = "assets/sounds/pew.mp3"
            additional_sound = pygame.mixer.Sound(additional_sound_path)
            additional_sound.play()
            bullet1.rect.x = playerCar1.rect.x + (playerCar1.width - bullet1.width) / 2
            bullet1.rect.y = playerCar1.rect.y

        # Update sprites
        all_sprites_list.update()

        # Draw background and lines

        # Draw the first road
        pygame.draw.rect(screen, colors.colors['ASPHALTGRAY'], [60, 0, 400, 500])
        pygame.draw.line(screen, colors.colors['BRICK'], (60, 0), (60, 500), 20)
        pygame.draw.line(screen, colors.colors['BRICK'], (460, 0), (460, 500), 20)

        # Draw the second road with 80 pixels gap
        pygame.draw.rect(screen, colors.colors['ASPHALTGRAY'], [940, 0, 400, 500])
        pygame.draw.line(screen, colors.colors['BRICK'], (940, 0), (940, 500), 20)
        pygame.draw.line(screen, colors.colors['BRICK'], (1340, 0), (1340, 500), 20)

        # Draw buttons
        button_quit.draw_button(mouse)
        button_shop.draw_button(mouse)

        # Draw power_ups if there is no activated yet
        if power_up_start_time1 == 0:
            draw_power_ups(list_of_power_ups1, player_car_speed1, True)

        if power_up_start_time2 == 0:
            draw_power_ups(list_of_power_ups2, player_car_speed2)

        # Update and draw road lines
        draw_lines(lines_left, player_car_speed1)
        draw_lines(lines_right, player_car_speed2)

        # Spawn new cars
        spawn_cars(incoming_cars_list1, player_car_speed1, True)
        spawn_cars(incoming_cars_list2, player_car_speed2)

        # Draw all sprites
        all_sprites_list.draw(screen)

        # Check for collision with power ups
        collided_power_ups1 = pygame.sprite.spritecollide(playerCar1, list_of_power_ups1, dokill=False)
        collided_power_ups2 = pygame.sprite.spritecollide(playerCar2, list_of_power_ups2, dokill=False)

        # Iterate through the collided power-ups if power-up started
        if power_up_start_time1 == 0 and collided_power_ups1:
            for power_up in collided_power_ups1:
                # Setting the time beginning of power up
                power_up_start_time1 = pygame.time.get_ticks()

                # To play the invincibility music
                if isinstance(power_up, InvincibilityPowerUp):
                    pygame.mixer.music.unload()  # removes background music from mixer
                    pygame.mixer.music.load(invincibility_sound_file)  # add invincibility power up music
                    pygame.mixer.music.play(-1)  # Start playing the power-up sound

                # Rewriting the player
                all_sprites_list.remove(playerCar1)
                power_up.affect_player(playerCar1)
                all_sprites_list.add(playerCar1)

                # if power up is a shooting turning on the tank mode
                if isinstance(power_up, ShootingPowerUp):
                    TANK_MODE1 = True

                if isinstance(power_up, SlowingPowerUp):
                    power_up.affect_traffic(incoming_cars_list1)
                    slowing_power_up_active = True

            # removing the power up square from the view
            for power_up in list_of_power_ups1:
                power_up.rect.y = 600

        if power_up_start_time2 == 0 and collided_power_ups2:
            for power_up in collided_power_ups2:
                # Setting the time beginning of power up
                power_up_start_time2 = pygame.time.get_ticks()

                # To play the invincibility music
                if isinstance(power_up, InvincibilityPowerUp):
                    pygame.mixer.music.unload()  # removes background music from mixer
                    pygame.mixer.music.load(invincibility_sound_file)  # add invincibility power up music
                    pygame.mixer.music.play(-1)  # Start playing the power-up sound

                # Rewriting the player
                all_sprites_list.remove(playerCar2)
                power_up.affect_player(playerCar2)
                all_sprites_list.add(playerCar2)

                # if power up is a shooting turning on the tank mode
                if isinstance(power_up, ShootingPowerUp):
                    TANK_MODE2 = True

                if isinstance(power_up, SlowingPowerUp):
                    power_up.affect_traffic(incoming_cars_list2)
                    slowing_power_up_active = True

            # removing the power up square from the view
            for power_up in list_of_power_ups2:
                power_up.rect.y = 600

        # code after power up finished(when power-up time is out)
        if current_time - power_up_start_time1 >= timer_duration_for_power_ups and power_up_start_time1 != 0:
            # Stop invincibility sound and resume background music if invincibility power-up was active
            if playerCar1.invincible:
                pygame.mixer.music.unload()  # this unloads the invincibility sound
                pygame.mixer.music.load(audio_path)  # returns the background sound
                pygame.mixer.music.play(-1)  # Start playing the background sound

            if slowing_power_up_active:
                for car in incoming_cars_list1:
                    car.reset_speed()
                slowing_power_up_active = False

            # Returning the player car as it was before power up
            all_sprites_list.remove(playerCar1)
            playerCar1.copy_car(original_playerCar1)
            all_sprites_list.add(playerCar1)

            all_sprites_list.update()
            # power up is off
            power_up_start_time1 = 0
            TANK_MODE1 = False
            playerCar1.invincible = False


        if current_time - power_up_start_time2 >= timer_duration_for_power_ups and power_up_start_time2 != 0:
            # Stop invincibility sound and resume background music if invincibility power-up was active
            if playerCar2.invincible:
                pygame.mixer.music.unload()  # this unloads the invincibility sound
                pygame.mixer.music.load(audio_path)  # returns the background sound
                pygame.mixer.music.play(-1)  # Start playing the background sound

            if slowing_power_up_active:
                for car in incoming_cars_list2:
                    car.reset_speed()
                slowing_power_up_active = False

            # Returning the player car as it was before power up
            all_sprites_list.remove(playerCar2)
            playerCar2.copy_car(original_playerCar2)
            all_sprites_list.add(playerCar2)

            all_sprites_list.update()
            # power up is off
            power_up_start_time2 = 0
            TANK_MODE2 = False
            playerCar2.invincible = False

        # loading bar for power ups
        if power_up_start_time1 != 0:
            p1_text = p1_font.render('P1', True, colors.colors['BLACK'])  # Change 'WHITE' to your preferred color
            p1_text_position = (660, 300)
            screen.blit(p1_text, p1_text_position)
            loading_bar_rect1.width = min(loading_bar_width1 - (
                    (current_time - power_up_start_time1) / timer_duration_for_power_ups) * loading_bar_width1,
                                          loading_bar_width1)
            pygame.draw.rect(screen, border_color1, border_rect1)
            pygame.draw.rect(screen, colors.colors["MATRIXGREEN"], loading_bar_rect1)

        if power_up_start_time2 != 0:
            p2_text = p2_font.render('P2', True, colors.colors['BLACK'])  # Change 'WHITE' to your preferred color
            p2_text_position = (720, 360)
            screen.blit(p2_text, p2_text_position)
            loading_bar_rect2.width = min((current_time - power_up_start_time2) / timer_duration_for_power_ups,
                                          1) * loading_bar_width2
            pygame.draw.rect(screen, border_color2, border_rect2)
            pygame.draw.rect(screen, colors.colors["DARKGREEN"], loading_bar_rect2)

        # Check for collision with enemy cars
        # If player is invincible, check for collisions and move collided cars off-screen
        if playerCar1.invincible:
            collided_cars = pygame.sprite.spritecollide(playerCar1, incoming_cars_list1, dokill=False)
            for car in collided_cars:
                car.rect.y = -1000  # Visually, this makes the cars that were hit disappear
        # If player is not invincible, game ends upon collision with enemy cars
        elif pygame.sprite.spritecollideany(playerCar1, incoming_cars_list1):
            pygame.display.update()
            for entity in all_sprites_list:
                entity.kill()
            carryOn = False
            pygame.mixer.music.stop()
            game_over.multiplayer_win_screen(False)

        # Check for collision with enemy cars
        # If player is invincible, check for collisions and move collided cars off-screen
        if playerCar2.invincible:
            collided_cars = pygame.sprite.spritecollide(playerCar2, incoming_cars_list2, dokill=False)
            for car in collided_cars:
                car.rect.y = -1000  # Visually, this makes the cars that were hit disappear

        # If player is not invincible, game ends upon collision with enemy cars
        elif pygame.sprite.spritecollideany(playerCar2, incoming_cars_list2):
            pygame.display.update()
            for entity in all_sprites_list:
                entity.kill()
            carryOn = False
            pygame.mixer.music.stop()
            game_over.multiplayer_win_screen(True)
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
        pygame.draw.rect(screen, colors.colors['LIGHTGREEN'], (0, y, 1400, stripe_height))
        pygame.draw.rect(screen, colors.colors['MEDIUMGREEN'], (0, y + stripe_height, 1400, stripe_height))


# Function that is drawing the power ups to the road
def draw_power_ups(power_ups, player_car_speed, first_player=False):
    k = 880
    if first_player:
        k = 0
    for power_up in power_ups:
        power_up.move_down(player_car_speed)
        # Reset the road line to the top of the screen and repaint it to create the illusion of continuous road
        if power_up.rect.y >= 500:
            # Shooting power up probability
            if isinstance(power_up, ShootingPowerUp):
                power_up.rect.y = random.randrange(-2500, -5, 243)
                power_up.rect.x = random.randrange(60 + k, 460 + k - power_up.radius * 2)

            # SizeReduction power up probability
            elif isinstance(power_up, SizeReductionPowerUp):
                power_up.rect.y = random.randrange(-500, -5, 243)
                power_up.rect.x = random.randrange(60 + k, 460 + k - power_up.radius * 2)

            # Invincibility Power Up probability
            elif isinstance(power_up, InvincibilityPowerUp):
                power_up.rect.y = random.randrange(-3000, -5, 486)  # Larger range means the spawn rate is lower
                power_up.rect.x = random.randrange(60 + k, 460 + k - power_up.radius * 2)

            # Slowing Time Down Probability
            elif isinstance(power_up, SlowingPowerUp):
                power_up.rect.y = random.randrange(-750, -5, 243)
                power_up.rect.x = random.randrange(60 + k, 460 + k - power_up.radius * 2)


# Move each road line down based on the player's car speed
# If a road line reaches the bottom of the screen, reset it to the top and repaint it
def draw_lines(lines, player_car_speed1):
    for line in lines:
        line.move_down(player_car_speed1)
        # Reset the road line to the top of the screen and repaint it to create the illusion of continuous road
        if line.rect.y >= 500:
            line.repaint()
            line.rect.y = -50


# Move each incoming car down based on the player's car speed
# If a road line reaches the bottom of the screen, reset it to the top randomly avoiding overlapping
def spawn_cars(incoming_cars_list, player_car_speed, first_player=False):
    k = 880
    if first_player:
        k = 0
    for car in incoming_cars_list:
        car.moveDown(player_car_speed)

        # Check if the car has reached the bottom of the screen
        if car.rect.y >= 500:

            # Depending on the x-coordinate of the car, reposition it to avoid overlapping with other cars
            if 60 + k <= car.rect.x < 160 + k:
                function_to_avoid_spawning_cars_on_cars(car, 60 + k, incoming_cars_list)
            if 160 + k <= car.rect.x < 260 + k:
                function_to_avoid_spawning_cars_on_cars(car, 160 + k, incoming_cars_list)
            if 260 + k <= car.rect.x < 360 + k:
                function_to_avoid_spawning_cars_on_cars(car, 260 + k, incoming_cars_list)
            if 360 + k <= car.rect.x < 460 + k:
                function_to_avoid_spawning_cars_on_cars(car, 360 + k, incoming_cars_list)


def function_to_avoid_spawning_cars_on_cars(the_car, position_of_line, incoming_cars_list):
    k = True

    # Remove the car from the list temporarily to avoid self-collision check
    incoming_cars_list.remove(the_car)

    # Keep attempting to reposition the car until a collision-free position is found
    while k:

        # Randomly set the x and y coordinates within the specified range and range for y-coordinate
        the_car.rect.x = random.randint(position_of_line, position_of_line + 100 - the_car.width)
        the_car.rect.y = random.randrange(-2000, -5, 243)

        # Check for collisions with other incoming cars
        if pygame.sprite.spritecollideany(the_car, incoming_cars_list) is None:
            # If no collision, add the car back to the list and break out of the loop
            incoming_cars_list.add(the_car)
            break
