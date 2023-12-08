import colors
import credits
import game
import pygame
import multiplayer
from button import Button


def interface():
    pygame.init()

    # Set up the screen
    screen_size = 700, 600
    screen = pygame.display.set_mode(screen_size)

    # Load and scale the background image
    background_path = "assets/images/themes/matrix.jpg"
    background_image = pygame.image.load(background_path)
    background_image = pygame.transform.scale(background_image, (screen_size[0], screen_size[1]))

    # settings for fonts
    font_path = "assets/fonts/retro_font.ttf"
    font_size = 33
    headings_font = pygame.font.Font(font_path, font_size)
    headings_font.set_italic(True)
    buttons_font = pygame.font.Font(font_path, 20)
    credits_font = pygame.font.Font(font_path, 10)

    # text for button and for titles
    text_interface = headings_font.render('Drive for your life', True, colors.colors['MATRIXGREEN'])
    text_car_racing = buttons_font.render('Car Racing', True, colors.colors['MATRIXGREEN'])
    text_game2 = buttons_font.render('Multiplayer', True, colors.colors['MATRIXGREEN'])
    text_instructions = buttons_font.render('Instructions', True, colors.colors['MATRIXGREEN'])
    text_quit = buttons_font.render('Quit', True, colors.colors['MATRIXGREEN'])

    # Decorative line
    line_color = colors.colors['MATRIXGREEN']
    line_start_pos = (25, 170)
    line_end_pos = (675, 170)
    line_thickness = 5

    # Decorative car
    small_car_path = 'assets/images/decoration/lambo.webp'
    small_car_image = pygame.image.load(small_car_path)
    small_car_image = pygame.transform.scale(small_car_image, (250, 45))
    car_image_pos_x = line_end_pos[0] - 240
    car_image_pos_y = line_end_pos[1] - 43

    # position of buttons
    button_car_racing_position = [100, 200, 200, 100]
    button_game2_position = [400, 200, 250, 100]
    button_credits_position = [80, 380, 250, 100]
    button_quit_position = [420, 380, 200, 100]

    # Create buttons object
    car_racing_button = Button(screen, button_car_racing_position, text_car_racing)
    game2_button = Button(screen, button_game2_position, text_game2)
    credits_button = Button(screen, button_credits_position, text_instructions)
    quit_button = Button(screen, button_quit_position, text_quit)

    text_interface_rect = text_interface.get_rect(center=(screen_size[0] // 2, 100))

    made_by_text_line1 = credits_font.render('Project by:', True, line_color)
    made_by_text_line2 = credits_font.render('Guilherme Pereira 20221856', True, line_color)
    made_by_text_line3 = credits_font.render('Rodrigo Azevedo 20222044', True, line_color)
    made_by_text_line4 = credits_font.render('Semen Sazonov 20221689', True, line_color)

    # Defining the position for each line of text
    line_height = 20
    made_by_rect_line1 = made_by_text_line1.get_rect(center=(screen_size[0] // 2, screen_size[1] - 60))
    made_by_rect_line2 = made_by_text_line2.get_rect(center=(screen_size[0] // 2, made_by_rect_line1.y + line_height))
    made_by_rect_line3 = made_by_text_line3.get_rect(center=(screen_size[0] // 2, made_by_rect_line2.y + line_height))
    made_by_rect_line4 = made_by_text_line4.get_rect(center=(screen_size[0] // 2, made_by_rect_line3.y + line_height))

    while True:

        # Display the background image
        screen.blit(background_image, (0, 0))

        # Display the title "Interface"
        screen.blit(text_interface, text_interface_rect.topleft)

        # Draw the decorative line
        pygame.draw.line(screen, line_color, line_start_pos, line_end_pos, line_thickness)

        # Draw the small car image at the end of the line
        screen.blit(small_car_image, (car_image_pos_x, car_image_pos_y))

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Draw buttons for Car Racing, Game2, Credits, and Quit
        car_racing_button.draw_button(mouse)
        game2_button.draw_button(mouse)
        credits_button.draw_button(mouse)
        quit_button.draw_button(mouse)

        # Display each line of the made_by_text
        screen.blit(made_by_text_line1, made_by_rect_line1.topleft)
        screen.blit(made_by_text_line2, made_by_rect_line2.topleft)
        screen.blit(made_by_text_line3, made_by_rect_line3.topleft)
        screen.blit(made_by_text_line4, made_by_rect_line4.topleft)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Play clicking sound
                additional_sound_path = "assets/sounds/button.mp3"
                additional_sound = pygame.mixer.Sound(additional_sound_path)
                additional_sound.play()

                # Check which button is pressed and take appropriate action
                if car_racing_button.is_button_pressed():
                    pygame.mixer.music.stop()
                    game.game()
                if game2_button.is_button_pressed():
                    pygame.mixer.music.stop()
                    multiplayer.multi_game()
                if credits_button.is_button_pressed():
                    pygame.mixer.music.stop()
                    credits.credits()
                if quit_button.is_button_pressed():
                    pygame.quit()

        # Check if background music is playing
        if not pygame.mixer.music.get_busy():
            pygame.mixer.init()
            audio_path = "assets/sounds/interface.mp3"
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

        # Update the display
        pygame.display.update()
