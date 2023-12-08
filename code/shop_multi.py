
import colors
import pygame
import multiplayer
from button import Button


def shop_window_multi():
    pygame.init()

    # Set up the display
    screen_size = 1000, 650
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
    text_p1 = heading_font.render('P1', True, colors.colors['MATRIXGREEN'])
    text_p2 = heading_font.render('P2', True, colors.colors['MATRIXGREEN'])
    text_title_rect = text_title.get_rect(center=(screen_size[0] // 2, 50))

    car_button_width = 60
    car_button_height = 100
    spacing_between_buttons = 90  # Increase the space between buttons if needed
    total_cars_width = 5 * car_button_width + 4 * spacing_between_buttons
    start_x = (screen_size[0] - total_cars_width) // 2
    #
    # buttons

    # positions of buttons
    button_quit_position = [750, 550, 200, 50]
    button_player_car1_position = [start_x, 200, car_button_width, car_button_height]
    button_player_car2_position = [start_x + car_button_width + spacing_between_buttons, 200, car_button_width,
                                   car_button_height]
    button_player_car3_position = [start_x + 2 * (car_button_width + spacing_between_buttons), 200, car_button_width,
                                   car_button_height]
    button_player_car4_position = [start_x + 3 * (car_button_width + spacing_between_buttons), 200, car_button_width,
                                   car_button_height]
    button_player_car5_position = [start_x + 4 * (car_button_width + spacing_between_buttons), 200, car_button_width,
                                   car_button_height]

    button_player_car6_position = [start_x, 400, car_button_width, car_button_height]

    button_player_car7_position = [start_x + car_button_width + spacing_between_buttons, 400, car_button_width,
                                   car_button_height]
    button_player_car8_position = [start_x + 2 * (car_button_width + spacing_between_buttons), 400, car_button_width,
                                   car_button_height]
    button_player_car9_position = [start_x + 3 * (car_button_width + spacing_between_buttons), 400, car_button_width,
                                   car_button_height]
    button_player_car10_position = [start_x + 4 * (car_button_width + spacing_between_buttons), 400, car_button_width,
                                   car_button_height]
    text_p1_position = [start_x + 2 * (car_button_width + spacing_between_buttons), 150, car_button_width,
                        car_button_height]

    text_p2_position = [start_x + 2 * (car_button_width + spacing_between_buttons), 350, car_button_width,
                        car_button_height]

    # Create button objects
    button_quit = Button(screen, button_quit_position, text_to_restart)
    #
    player_car1_picture_path = "assets/images/player_cars/player_car1.webp"
    button_player_car1 = Button(screen, button_player_car1_position, picture_path=player_car1_picture_path)
    #
    player_car2_picture_path = "assets/images/player_cars/player_car2.webp"
    button_player_car2 = Button(screen, button_player_car2_position, picture_path=player_car2_picture_path)
    #
    player_car3_picture_path = "assets/images/player_cars/player_car3.webp"
    button_player_car3 = Button(screen, button_player_car3_position, picture_path=player_car3_picture_path)
    #
    player_car4_picture_path = "assets/images/player_cars/player_car7.webp"
    button_player_car4 = Button(screen, button_player_car4_position, picture_path=player_car4_picture_path)
    #
    player_car5_picture_path = "assets/images/player_cars/player_car6.webp"
    button_player_car5 = Button(screen, button_player_car5_position, picture_path=player_car5_picture_path)

    player_car6_picture_path = "assets/images/player_cars/player_car1.webp"
    button_player_car6 = Button(screen, button_player_car6_position, picture_path=player_car1_picture_path)
    #
    player_car7_picture_path = "assets/images/player_cars/player_car2.webp"
    button_player_car7 = Button(screen, button_player_car7_position, picture_path=player_car2_picture_path)
    #
    player_car8_picture_path = "assets/images/player_cars/player_car3.webp"
    button_player_car8 = Button(screen, button_player_car8_position, picture_path=player_car3_picture_path)
    #
    player_car9_picture_path = "assets/images/player_cars/player_car7.webp"
    button_player_car9 = Button(screen, button_player_car9_position, picture_path=player_car4_picture_path)
    #
    player_car10_picture_path = "assets/images/player_cars/player_car6.webp"
    button_player_car10 = Button(screen, button_player_car10_position, picture_path=player_car5_picture_path)

    while True:

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Display the blurred background
        screen.blit(blurred_background, (0, 0))

        # Display title and points
        screen.blit(text_title, text_title_rect)

        screen.blit(text_p1, text_p1_position)

        screen.blit(text_p2, text_p2_position)

        # Draw buttons of cars and game start
        button_player_car10.draw_button(mouse)
        button_player_car9.draw_button(mouse)
        button_player_car8.draw_button(mouse)
        button_player_car7.draw_button(mouse)
        button_player_car6.draw_button(mouse)
        button_player_car5.draw_button(mouse)
        button_player_car4.draw_button(mouse)
        button_player_car3.draw_button(mouse)
        button_player_car2.draw_button(mouse)
        button_player_car1.draw_button(mouse)
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
                    multiplayer.multi_game()

                # Handle player car selection button events
                if button_player_car5.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/francesco.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path1 = player_car5_picture_path
                if button_player_car4.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/is_that_a_supra.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path1 = player_car4_picture_path
                if button_player_car3.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/family.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path1 = player_car3_picture_path
                if button_player_car2.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/delorean.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path1 = player_car2_picture_path
                if button_player_car1.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/no_please_no.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path1 = player_car1_picture_path

                # Handle player car selection button events
                if button_player_car10.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/francesco.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path2 = player_car5_picture_path
                if button_player_car9.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/is_that_a_supra.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path2 = player_car4_picture_path
                if button_player_car8.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/family.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path2 = player_car3_picture_path
                if button_player_car7.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/delorean.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path2 = player_car2_picture_path
                if button_player_car6.is_button_pressed():
                    # Change the player car image and background music
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    background_music_path = "assets/sounds/no_please_no.mp3"
                    pygame.mixer.music.load(background_music_path)
                    pygame.mixer.music.play()
                    multiplayer.player_car_path2 = player_car1_picture_path

        # Update the display
        pygame.display.update()
