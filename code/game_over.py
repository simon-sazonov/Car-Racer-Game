import random
import multiplayer
import colors
import cv2
import game
import global_variables
import pygame
import interface
from button import Button


def loss_video():
    pygame.init()

    # Set up the display
    screen_width, screen_height = 700, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game Over")

    # Choose a random video and audio path for game over
    if random.randint(1, 2) == 1:
        video_path = "assets/videos/you_died.mp4"
        audio_path = "assets/sounds/you_died.mp3"
    else:
        video_path = "assets/videos/the_end.mp4"
        audio_path = "assets/sounds/the_end.mp3"

    # Load the video
    cap = cv2.VideoCapture(video_path)

    # Initialize Pygame mixer for audio playback
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the original video dimensions
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calculate the scaling factor based on the desired display size
    scaling_factor = min(screen_width / original_width, screen_height / original_height)
    scaled_width = int(original_width * scaling_factor)
    scaled_height = int(original_height * scaling_factor)

    # Create a clock to control the frame rate
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ret, frame = cap.read()
        if not ret:
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == total_frames:
                break

        # Convert the OpenCV frame to a Pygame surface
        pygame_frame = pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], "BGR")

        # Scale the Pygame surface to fit the window
        scaled_frame = pygame.transform.scale(pygame_frame, (scaled_width, scaled_height))

        # Calculate the position to center the video in the window
        x_offset = (screen_width - scaled_width) // 2
        y_offset = (screen_height - scaled_height) // 2

        # Clear the screen
        screen.fill((0, 0, 0))
        screen.blit(scaled_frame, (x_offset, y_offset))
        pygame.display.flip()

        # Check if audio playback has started
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        clock.tick(30)

    # Stop the audio and release the video
    pygame.mixer.music.stop()
    cap.release()

    # Open the loss window after displaying the video
    open_loss_window()
    pygame.quit()


def open_loss_window():
    pygame.init()

    # Set up the screen
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
    heading_font_size = 40
    font_size = 13
    button_font_size = 15
    heading_font = pygame.font.Font(font_path, heading_font_size)
    font = pygame.font.Font(font_path, font_size)
    button_font = pygame.font.Font(font_path, button_font_size)

    # text for button and for titles
    text_restart = button_font.render('Restart Game', True, colors.colors['MATRIXGREEN'])
    text_title = heading_font.render('GAME OVER', True, colors.colors['MATRIXGREEN'])
    text_points = font.render(f'That`s your total amount of points: {global_variables.all_points}.', True,
                              colors.colors['MATRIXGREEN'])
    text_quit = button_font.render('Quit', True, colors.colors['MATRIXGREEN'])

    # position of button
    button_return_position = [470, 400, 200, 50]

    button_quit_position = [30, 400, 200, 50]

    button_quit = Button(screen, button_quit_position, text_quit)

    # Create button object
    button_return = Button(screen, button_return_position, text_restart)

    # Initialize Pygame mixer for audio playback
    pygame.mixer.init()
    audio_path = "assets/sounds/elevator_music.mp3"
    pygame.mixer.music.load(audio_path)

    while True:

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Display the blurred background
        screen.blit(blurred_background, (0, 0))

        # Display title and points
        screen.blit(text_title, (170, 100))
        screen.blit(text_points, (50, 200))

        # Draw the restart button
        button_return.draw_button(mouse)

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

                # button event
                if button_return.is_button_pressed():
                    pygame.mixer.music.stop()
                    game.game()

                if button_quit.is_button_pressed():
                    pygame.mixer.music.stop()
                    interface.interface()

        # Check if the background music is playing
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

        # Update the display
        pygame.display.update()


def multiplayer_win_screen(first_player_win):
    pygame.init()

    # Set up the screen
    screen_size = 700, 500
    screen = pygame.display.set_mode(screen_size)

    win_text=""

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
    font_path = "assets/fonts/retro_font.ttf"
    heading_font_size = 40
    button_font_size = 15
    heading_font = pygame.font.Font(font_path, heading_font_size)
    button_font = pygame.font.Font(font_path, button_font_size)

    # text for button and for titles
    text_restart = button_font.render('Restart Game', True, colors.colors['MATRIXGREEN'])

    button_quit_position = [30, 400, 200, 50]

    text_quit = button_font.render('Quit', True, colors.colors['MATRIXGREEN'])

    button_quit = Button(screen, button_quit_position, text_quit)

    # Render the text for "Player Wins"
    if first_player_win:
        win_text = 'Player1 Wins'
    else:
        win_text = 'Player2 Wins'

    text_title = heading_font.render(win_text, True, colors.colors['MATRIXGREEN'])
    # Calculate the width of the rendered text
    text_width = text_title.get_width()

    # Calculate x position to center the text
    x_position = (700 - text_width) // 2

    # position of button
    button_return_position = [470, 400, 200, 50]

    # Create button object
    button_return = Button(screen, button_return_position, text_restart)

    # Initialize Pygame mixer for audio playback
    pygame.mixer.init()
    audio_path = "assets/sounds/elevator_music.mp3"
    pygame.mixer.music.load(audio_path)

    while True:

        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Display the blurred background
        screen.blit(blurred_background, (0, 0))

        # Display title and points
        screen.blit(text_title, (x_position, 100))

        # Draw the restart button
        button_return.draw_button(mouse)

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

                # button event
                if button_return.is_button_pressed():
                    pygame.mixer.music.stop()
                    multiplayer.multi_game()

                if button_quit.is_button_pressed():
                    pygame.mixer.music.stop()
                    interface.interface()

        # Check if the background music is playing
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

        # Update the display
        pygame.display.update()

