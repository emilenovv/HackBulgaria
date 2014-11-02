import pygame


def play():
    while True:
        choise = input("Enter command: ")
        if choise == "play":
            pygame.init()
            pygame.mixer.music.load("(19) [Rammstein] Mutter.mp3")
            pygame.mixer.music.play()
        elif choise == "stop":
            pygame.mixer.music.stop()

if __name__ == '__main__':
    play()
