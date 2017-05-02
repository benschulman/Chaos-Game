import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Dot:
    def __init__(self, pos):
        self.pos = pos

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.pos, 5, 5)

    def gen_new_dot_loc(self, x, y, mult):
        new_x = int(self.pos[0] * mult + x * (1 - mult))
        new_y = int(self.pos[1] * mult + y * (1 - mult))
        return new_x, new_y


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

    # Default Settings for Iteration
    x = 450
    y = 347
    dot1_loc = [450, 100]
    dot2_loc = [150, 600]
    dot3_loc = [750, 600]
    distance_mult = .5
    iterations = 10000

    # Default Dots
    d1 = Dot(dot1_loc)
    d2 = Dot(dot2_loc)
    d3 = Dot(dot3_loc)

    # Dot Array
    dot_arr = [d1, d2, d3]

    clock = pygame.time.Clock()

    # Main Loop
    while not done:

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 10 < mouse[0] < 10 + 100:
                    # RESET
                    if 10 < mouse[1] < 10 + 25:
                        clear = True
                        x = 450
                        y = 347
                        distance_mult = .5
                        dot_arr = []
                    # Iterate
                    elif 40 < mouse[1] < 40 + 25:
                        iterate = True
                    # Change Iterations
                    elif 70 < mouse[1] < 70 + 25:
                        iterations = int(input("Iterations"))
                    elif 100 < mouse[1] < 100 + 25:
                        dot_arr.append(Dot([x, y]))
                # Set Start Point
                else:
                    x = mouse[0]
                    y = mouse[1]

        # Game Logic
        mouse = pygame.mouse.get_pos()

        # -----Drawing Code-----#
        if clear:
            screen.fill(BLACK)

        # Draw 3 Dots
        for dot in dot_arr:
            dot.draw(screen)

        # Iteration Loop
        if iterate and len(dot_arr) > 0:
            iterate = False
            for i in range(iterations):
                r = random.randint(0, len(dot_arr)-1)
                pygame.draw.circle(screen, WHITE, [x, y], 1, 1)
                x, y = dot_arr[r].gen_new_dot_loc(x, y, distance_mult)

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

        # Add dot
        pygame.draw.rect(screen, WHITE, [10, 100, 100, 25])
        add_dot_surface, add_dot_rect = text_objects("Add Dot", font)
        add_dot_rect.center = ((10 + (100 / 2)), (100 + (25 / 2)))
        screen.blit(add_dot_surface, add_dot_rect)

        pygame.display.flip()

        # Clock FPS
        clock.tick(120)

    pygame.quit()


if __name__ == '__main__':
    main()
