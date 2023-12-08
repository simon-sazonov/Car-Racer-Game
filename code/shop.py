import pygame

import colors
import game
import global_variables
from button import Button


def shop_window():
    pygame.init()

    # Set up the display
    screen_size = 700, 500
    screen = pygame.display.set_mode(screen_size)

    # Load and scale the background image
    background_path = "assets/images/themes/matrix.jpg"
    background_image = pygame.image.load(background_path)
    background_image = pygame.transform.scale(background_image, (screen_size[0], screen_size[1]))

    # Apply a blur effect to the background
    blur_scale = 0.2
    blurred_background = pygame.transform.smoothscale(
        pygame.transform.smoothscale(background_image,
                                     (int(screen_size[0] * blur_scale), int(screen_size[1] * blur_scale))), screen_size)

    # settings for fonts
    font_path = "assets/fonts/retro_font.ttf"  # Adjust the path accordingly
    heading_font_size = 25
    font_size = 10
    button_font_size = 15

    heading_font = pygame.font.Font(font_path, heading_font_size)
    font = pygame.font.Font(font_path, font_size)
    button_font = pygame.font.Font(font_path, button_font_size)

    # text for button and titles
    text_to_restart = button_font.render('Start Game', True, colors.colors['MATRIXGREEN'])
    text_title = heading_font.render('Shop', True, colors.colors['MATRIXGREEN'])
    #
    # buttons

    # positions of buttons
    button_quit_position = [470, 400, 200, 50]
    button_player_car1_position = [100, 200, 60, 150]
    button_player_car2_position = [200, 200, 60, 150]
    button_player_car3_position = [300, 200, 60, 150]
    button_player_car4_position = [400, 200, 60, 150]
    button_player_car5_position = [500, 200, 60, 150]

    # Create button objects
    button_quit = Button(screen, button_quit_position, text_to_restart)
    #
    player_car1_picture_path = "assets/images/player_cars/player_car1.webp"
    button_player_car1 = Button(screen, button_player_car1_position, picture_path=player_car1_picture_path)
    player_car1_price = 0
    player_car1_price_text = font.render(f"{player_car1_price}", True, colors.colors['MATRIXGREEN'])

    #
    player_car2_picture_path = "assets/images/player_cars/player_car2.webp"
    button_player_car2 = Button(screen, button_player_car2_position, picture_path=player_car2_picture_path)
    player_car2_price = 100
    player_car2_price_text = font.render(f"{player_car2_price}", True, colors.colors['MATRIXGREEN'])
    #
    player_car3_picture_path = "assets/images/player_cars/player_car3.webp"
    button_player_car3 = Button(screen, button_player_car3_position, picture_path=player_car3_picture_path)
    player_car3_price = 200
    player_car3_price_text = font.render(f"{player_car3_price}", True, colors.colors['MATRIXGREEN'])

    #
    player_car4_picture_path = "assets/images/player_cars/player_car7.webp"
    button_player_car4 = Button(screen, button_player_car4_position, picture_path=player_car4_picture_path)
    player_car4_price = 500
    player_car4_price_text = font.render(f"{player_car4_price}", True, colors.colors['MATRIXGREEN'])

    #
    player_car5_picture_path = "assets/images/player_cars/player_car6.webp"
    button_player_car5 = Button(screen, button_player_car5_position, picture_path=player_car5_picture_path)
    player_car5_price = 1000
    player_car5_price_text = font.render(f"{player_car5_price}", True, colors.colors['MATRIXGREEN'])

    while True:

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Display the blurred background
        screen.blit(blurred_background, (0, 0))

        # Display title and points
        screen.blit(text_title, (300, 50))
        text_points = font.render(f'That`s your money: {global_variables.all_points}. Choose the car you wanna buy',
                                  True,
                                  colors.colors['MATRIXGREEN'])
        screen.blit(text_points, (50, 100))

        # Draw buttons of cars and game start
        button_player_car5.draw_button(mouse)

        screen.blit(player_car5_price_text, (512, 365))
        button_player_car4.draw_button(mouse)
        screen.blit(player_car4_price_text, (420, 365))
        button_player_car3.draw_button(mouse)
        screen.blit(player_car3_price_text, (318, 365))
        button_player_car2.draw_button(mouse)
        screen.blit(player_car2_price_text, (218, 365))
        button_player_car1.draw_button(mouse)
        screen.blit(player_car1_price_text, (127, 365))

        button_quit.draw_button(mouse)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Play clicking sound
                additional_sound_path = "assets/sounds/button.mp3"
                additional_sound = pygame.mixer.Sound(additional_sound_path)
                additional_sound.play()

                # buttons events
                if button_quit.is_button_pressed():
                    # Stop the background music and return to the game
                    pygame.mixer.music.stop()
                    game.game()

                if button_player_car1.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/no_please_no.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    game.player_car_path = player_car1_picture_path

                # Handle player car selection button events
                elif button_player_car5.is_button_pressed() and (
                        (global_variables.all_points - player_car5_price) > 0 or global_variables.car5_received):
                    if not global_variables.car5_received:
                        global_variables.all_points -= player_car5_price
                    global_variables.car5_received = True
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/francesco.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    game.player_car_path = player_car5_picture_path
                elif button_player_car4.is_button_pressed() and (
                        (global_variables.all_points - player_car4_price) > 0 or global_variables.car4_received):
                    if not global_variables.car4_received:
                        global_variables.all_points -= player_car4_price
                    global_variables.car4_received = True

                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/is_that_a_supra.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    game.player_car_path = player_car4_picture_path
                elif button_player_car3.is_button_pressed() and (
                        (global_variables.all_points - player_car3_price) > 0 or global_variables.car3_received):
                    if not global_variables.car3_received:
                        global_variables.all_points -= player_car3_price
                    global_variables.car3_received = True
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/family.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    game.player_car_path = player_car3_picture_path
                elif button_player_car2.is_button_pressed() and (
                        (global_variables.all_points - player_car2_price) > 0 or global_variables.car2_received):
                    if not global_variables.car2_received:
                        global_variables.all_points -= player_car2_price
                    global_variables.car2_received = True
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/delorean.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    game.player_car_path = player_car2_picture_path
                else:
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/error.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()

        # Update the display
        pygame.display.update()
