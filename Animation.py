import pygame
import time

class Animation :
    def __init__(self):
        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load("Audiomachine - Guardians At the Gate.mp3")
        pygame.mixer.music.play(-1)

        width, height = 1080, 600
        screen = pygame.display.set_mode((width, height))

        frame1 = pygame.image.load('fight1.png')
        frame2 = pygame.image.load('fight2.png')

        animation_time = 7
        frame_duration = 0.5
        num_frames = int(animation_time / frame_duration)

        start_time = time.time()
        running = True

        while running and (time.time() - start_time < animation_time):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            current_frame = int((time.time() - start_time) // frame_duration) % 2

            screen.fill((0, 0, 0))

            if current_frame == 0:
                screen.blit(frame1, (0, 0))
            else:
                screen.blit(frame2, (0, 0))

            pygame.display.flip()

            time.sleep(frame_duration / 2)


        pygame.quit()