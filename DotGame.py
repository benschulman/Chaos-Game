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

    d1 = Dot([450, 100])
    d2 = Dot([150, 600])
    d3 = Dot([750, 600])

    # Main Loop
    while not done:

        # Event Loop
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
                else:
                    x = mouse[0]
                    y = mouse[1]

        # Game Logic
        mouse = pygame.mouse.get_pos()

    # Drawing Code
        if clear:
            screen.fill(BLACK)

        # Draw 3 Dots
        d1.draw(screen)
        d2.draw(screen)
        d3.draw(screen)

        # Iteration Loop
        if iterate:
            iterate = False
            for i in range(iterations):
                r = random.randint(1, 3)
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

            clear = False

        # Reset Button
        pygame.draw.rect(screen, WHITE, [10, 10, 100, 25])
        font = pygame.font.Font('freesansbold.ttf', 10)
        reset_surface, reset_rect = text_objects("RESET", font)
        reset_rect.center = ((10 + (100 / 2)), (10 + (25 / 2)))
        screen.blit(reset_surface, reset_rect)

        # Iterate Button
        pygame.draw.rect(screen, WHITE, [10, 40, 100, 25])
        iterate_surface, iterate_rect = text_objects("Iterate", font)
        iterate_rect.center = ((10 + (100 / 2)), (40 + (25 / 2)))
        screen.blit(iterate_surface, iterate_rect)

        # Adjust Iterations Button
        pygame.draw.rect(screen, WHITE, [10, 70, 100, 25])
        adj_surface, adj_rect = text_objects("Adjust Iterations", font)
        adj_rect.center = ((10 + (100 / 2)), (70 + (25 / 2)))
        screen.blit(adj_surface, adj_rect)

        pygame.display.flip()

        # Clock FPS
        clock.tick(120)

    pygame.quit()


if __name__ == '__main__':
    main()