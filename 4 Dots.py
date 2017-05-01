import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Dot:
    def __init__(self, pos):
        self.pos = pos

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.pos, 5, 5)

    def x_pos(self):
        return self.pos[0]

    def y_pos(self):
        return self.pos[1]


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def main():
    pygame.init()

    size = (900, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chaos Game")

    done = False
    iterate = False
    clear = True
    x = 0
    y = 0
    iterations = 10000
    clock = pygame.time.Clock()

    d1 = Dot([200, 50])
    d2 = Dot([200, 450])
    d3 = Dot([600, 50])
    d4 = Dot([600, 450])

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 10 < mouse[0] < 10 + 100:
                    if 10 < mouse[1] < 10 + 25:
                        clear = True
                    elif 40 < mouse[1] < 40 + 25:
                        iterate = True
                    elif 70 < mouse[1] < 70 + 25:
                        iterations = int(input("Iterations"))
                elif not (10 < mouse[0] < 10 + 100) and not (10 < mouse[1] < 70 + 25):
                    x = mouse[0]
                    y = mouse[1]

        # Game Logic
        mouse = pygame.mouse.get_pos()

        # Drawing Code
        if clear:
            screen.fill(BLACK)

        # draw_dots()
        d1.draw(screen)
        d2.draw(screen)
        d3.draw(screen)
        d4.draw(screen)

        if iterate:
            iterate = False
            for i in range(iterations):
                r = random.randint(1, 4)
                pygame.draw.circle(screen, WHITE, [x, y], 1, 1)
                if r == 1:
                    x += d1.x_pos()
                    x = int(x/2)
                    y += d1.y_pos()
                    y = int(y / 2)
                if r == 2:
                    x += d2.x_pos()
                    x = int(x / 2)
                    y += d2.y_pos()
                    y = int(y / 2)
                if r == 3:
                    x += d3.x_pos()
                    x = int(x / 2)
                    y += d3.y_pos()
                    y = int(y/2)
                if r == 4:
                    x += d4.x_pos()
                    x = int(x / 2)
                    y += d4.y_pos()
                    y = int(y/2)

            clear = False

        # Reset Button
        pygame.draw.rect(screen, WHITE, [10, 10, 100, 25])
        font = pygame.font.Font('freesansbold.ttf', 10)
        text_surf1, text_rect1 = text_objects("RESET", font)
        text_rect1.center = ((10 + (100 / 2)), (10 + (25 / 2)))
        screen.blit(text_surf1, text_rect1)

        # Number of Dots Button
        pygame.draw.rect(screen, WHITE, [10, 40, 100, 25])
        text_surf2, text_rect2 = text_objects("Iterate", font)
        text_rect2.center = ((10 + (100 / 2)), (40 + (25 / 2)))
        screen.blit(text_surf2, text_rect2)

        pygame.draw.rect(screen, WHITE, [10, 70, 100, 25])
        text_surf3, text_rect3 = text_objects("Adjust Iterations", font)
        text_rect3.center = ((10 + (100 / 2)), (70 + (25 / 2)))
        screen.blit(text_surf3, text_rect3)

        pygame.display.flip()

        # Clock FPS
        clock.tick(120)

    pygame.quit()


if __name__ == '__main__':
    main()