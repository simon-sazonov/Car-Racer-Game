import colors
import interface
import pygame

from button import Button


def credits():

    pygame.init()

    # Set up the screen
    screen_size = 700, 500
    screen = pygame.display.set_mode(screen_size)

    # Load and scale the background image
    background_path = "assets/images/themes/matrix.jpg"
    background_image = pygame.image.load(background_path)
    background_image = pygame.transform.scale(background_image, (screen_size[0], screen_size[1]))

    # Applies a blur effect to the background
    blur_scale = 0.2
    blurred_background = pygame.transform.smoothscale(
        pygame.transform.smoothscale(background_image,
                                     (int(screen_size[0] * blur_scale), int(screen_size[1] * blur_scale))), screen_size)

    # settings for fonts
    font_path = "assets/fonts/retro_font.ttf"
    heading_font_size = 25
    font_size = 10
    button_font_size = 15
    font_p2_size = 14
    font_small_size = 10

    heading_font = pygame.font.Font(font_path, heading_font_size)
    font_p2 = pygame.font.Font(font_path, font_p2_size)
    font = pygame.font.Font(font_path, font_size)
    button_font = pygame.font.Font(font_path, button_font_size)
    font_small = pygame.font.Font(font_path, font_small_size)

    power_up_icon_size = (50, 50)
    power_up_spacing = 60

    # text for button and for titles
    text_return = button_font.render('Quit', True, colors.colors['MATRIXGREEN'])
    text_title = heading_font.render('Instructions', True, colors.colors['MATRIXGREEN'])
    text_p1 = heading_font.render('P1', True, colors.colors['MATRIXGREEN'])
    text_p2 = heading_font.render('P2', True, colors.colors['MATRIXGREEN'])
    text_instruction_left = font.render('Move Left: A', True, colors.colors['MATRIXGREEN'])
    text_instruction_right = font.render('Move Right: D', True, colors.colors['MATRIXGREEN'])
    text_instruction_speed_up = font.render('Speed Up: W', True, colors.colors['MATRIXGREEN'])
    text_instruction_slow_down = font.render('Slow Down: S', True, colors.colors['MATRIXGREEN'])
    text_instruction_p2_left = font.render('Move Left: Left Arrow', True, colors.colors['MATRIXGREEN'])
    text_instruction_p2_right = font.render('Move Right: Right Arrow', True, colors.colors['MATRIXGREEN'])
    text_instruction_p2_up = font.render('Speed Up: Up Arrow', True, colors.colors['MATRIXGREEN'])
    text_instruction_p2_down = font.render('Slow Down: Down Arrow', True, colors.colors['MATRIXGREEN'])
    text_instruction_p1_shoot = font.render('Shoot: Left Shift', True, colors.colors['MATRIXGREEN'])
    text_instruction_p2_shoot = font.render('Shoot: Right Shift', True, colors.colors['MATRIXGREEN'])
    text_power_ups = font_p2.render('Power Ups', True, colors.colors['MATRIXGREEN'])
    power_up1_description = 'Size reduction: Reduces the size of the player car!'
    power_up2_description = 'Invincibility: Makes the player car immune to collisions for a small period of time!'
    power_up3_description = 'Tank Mode: Turns the player car into a tank that can shoot bullets that destroy' \
                            ' incoming cars (reload time)!'
    power_up4_description = 'Slowing Time: Makes the incoming cars go slower!'

    power_up1_picture_path = "assets/images/power_ups/size_reduction.webp"
    power_up2_picture_path = "assets/images/power_ups/invincibility.webp"
    power_up3_picture_path = "assets/images/power_ups/shooting.webp"
    power_up4_picture_path = "assets/images/power_ups/slowing_time.webp"

    button_powerup1 = Button(screen, (70, 350, *power_up_icon_size),
                             picture_path=power_up1_picture_path)
    button_powerup2 = Button(screen, (70, 350 + power_up_spacing, *power_up_icon_size),
                             picture_path=power_up2_picture_path)
    button_powerup3 = Button(screen, (70 + power_up_spacing, 350, *power_up_icon_size),
                             picture_path=power_up3_picture_path)
    button_powerup4 = Button(screen, (70 + power_up_spacing, 350 + power_up_spacing, *power_up_icon_size),
                             picture_path=power_up4_picture_path)
    #

    # position of button
    button_return_position = [470, 440, 200, 50]

    # Create button object
    button_return = Button(screen, button_return_position, text_return)

    # Initialize Pygame mixer for audio playback
    pygame.mixer.init()
    audio_path = "assets/sounds/elevator_music.mp3"
    pygame.mixer.music.load(audio_path)

    active_power_up_description = None

    while True:

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Display the blurred background
        screen.blit(blurred_background, (0, 0))

        # Displaying title and all the text for the instructions
        screen.blit(text_title, (70, 50))
        screen.blit(text_instruction_left, (70, 150))
        screen.blit(text_instruction_right, (70, 180))
        screen.blit(text_instruction_speed_up, (70, 210))
        screen.blit(text_instruction_slow_down, (70, 240))
        screen.blit(text_instruction_p2_left, (400, 150))
        screen.blit(text_instruction_p2_right, (400, 180))
        screen.blit(text_instruction_p2_up, (400, 210))
        screen.blit(text_instruction_p2_down, (400, 240))
        screen.blit(text_instruction_p2_shoot, (400, 270))
        screen.blit(text_instruction_p1_shoot, (70, 270))
        screen.blit(text_p1, (70, 100))
        screen.blit(text_p2, (400, 100))
        screen.blit(text_power_ups, (70, 320))
        button_powerup1.draw_button(mouse)
        button_powerup2.draw_button(mouse)
        button_powerup3.draw_button(mouse)
        button_powerup4.draw_button(mouse)

        # Draw the return button
        button_return.draw_button(mouse)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Play clicking sound
                additional_sound_path = "assets/sounds/button.mp3"
                additional_sound = pygame.mixer.Sound(additional_sound_path)
                additional_sound.play()

                if button_powerup1.is_button_pressed():
                    active_power_up_description = power_up1_description
                elif button_powerup2.is_button_pressed():
                    active_power_up_description = power_up2_description
                elif button_powerup3.is_button_pressed():
                    active_power_up_description = power_up3_description
                elif button_powerup4.is_button_pressed():
                    active_power_up_description = power_up4_description

                # button event
                if button_return.is_button_pressed():
                    pygame.mixer.music.stop()
                    interface.interface()

        if active_power_up_description:
            render_multiline_text(screen, active_power_up_description, (230, 350),
                                  font_p2, font_small, colors.colors['MATRIXGREEN'], 300, line_spacing=10)

        # Check if the background music is playing
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

        # Update the display
        pygame.display.update()


def render_multiline_text(screen, text, pos, name_font, desc_font, color, max_width, line_spacing=5):

    # Split the text into name and description
    name, _, description = text.partition(':')
    name += ':'

    # Render the name
    name_surface = name_font.render(name, True, color)
    screen.blit(name_surface, (pos[0], pos[1]))

    # Adjust Y-offset for the description
    y_offset = name_font.get_height() + line_spacing

    # Process the description text
    words = description.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        if desc_font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)

    # Render the description lines
    for line in lines:
        text_surface = desc_font.render(line, True, color)
        screen.blit(text_surface, (pos[0], pos[1] + y_offset))
        y_offset += desc_font.get_height() + line_spacing
