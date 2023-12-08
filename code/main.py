from interface import interface
import pygame


def main():
    pygame.mixer.init()
    audio_path = "assets/sounds/ps2_start_sound.mp3"
    pygame.mixer.music.load(audio_path)
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    interface()


if __name__ == '__main__':

    main()
