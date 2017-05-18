import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Dot:
    def __init__(self, pos):
        self.pos = pos

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.pos, 5, 5)

    def gen_new_dot_loc(self, x, y, multiplier):
        new_x = int(self.pos[0] * multiplier + x * (1 - multiplier))
        new_y = int(self.pos[1] * multiplier + y * (1 - multiplier))
        return new_x, new_y


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def draw_button(screen, color, arr, text, font):
    surf, rect = text_objects(text, font)
    pygame.draw.rect(screen, color, arr)
    rect.center = ((arr[0] + (arr[2] / 2)), (arr[1] + (arr[3] / 2)))
    screen.blit(surf, rect)


def main():
    pygame.init()

    size = (900, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chaos Game")
    font = pygame.font.Font('freesansbold.ttf', 10)

    done = False
    iterate = False
    clear = True
    repeats = True

    # Default Settings for Iteration
    x = 450
    y = 347
    dot1_loc = [450, 100]
    dot2_loc = [150, 600]
    dot3_loc = [750, 600]
    distance_multiplier = .5
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
                        repeats = True
                        x = 450
                        y = 347
                        distance_multiplier = .5
                        dot_arr = []
                    # Clear Dots
                    elif 40 < mouse[1] < 40 + 25:
                        clear = True
                    # Iterate
                    elif 70 < mouse[1] < 70 + 25:
                        iterate = True
                    # Change Iterations
                    elif 100 < mouse[1] < 100 + 25:
                        iterations = int(input("Iterations"))
                    # Add Dot
                    elif 130 < mouse[1] < 130 + 25:
                        dot_arr.append(Dot([x, y]))
                    # Adj Multiplier
                    elif 160 < mouse[1] < 160 + 25:
                        distance_multiplier = float(input("Distance Multiplier"))
                    # Reset to Default Triangle
                    elif 190 < mouse[1] < 190 + 25:
                        clear = True
                        repeats = True
                        x = 450
                        y = 347
                        dot_arr = [d1, d2, d3]
                    # Reset to Default Square
                    elif 220 < mouse[1] < 220 + 25:
                        clear = True
                        repeats = True
                        x = 450
                        y = 347
                        dot_arr = [Dot([200, 50]), Dot([800, 50]), Dot([200, 650]), Dot([800, 650])]
                    # Toggle Repeats
                    elif 250 < mouse[1] < 250 + 25:
                        repeats = not repeats

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
            if repeats:
                for i in range(iterations):
                    pygame.draw.circle(screen, WHITE, [x, y], 1, 1)
                    r = random.randint(0, len(dot_arr) - 1)
                    x, y = dot_arr[r].gen_new_dot_loc(x, y, distance_multiplier)
            else:
                old_r = -1
                for i in range(iterations):
                    pygame.draw.circle(screen, WHITE, [x, y], 1, 1)
                    r = random.randint(0, len(dot_arr) - 1)
                    while r == old_r:
                        r = random.randint(0, len(dot_arr) - 1)
                    old_r = r
                    x, y = dot_arr[r].gen_new_dot_loc(x, y, distance_multiplier)

            clear = False

        # Reset Button
        draw_button(screen, WHITE, [10, 10, 100, 25], "RESET", font)

        # Clear Dots
        draw_button(screen, WHITE, [10, 40, 100, 25], "Clear Dots", font)

        # Iterate Button
        draw_button(screen, WHITE, [10, 70, 100, 25], "Iterate", font)

        # Adjust Iterations Button
        draw_button(screen, WHITE, [10, 100, 100, 25], "Adjust Iterations", font)

        # Add dot
        draw_button(screen, WHITE, [10, 130, 100, 25], "Add Start Dot", font)

        # Adjust Multiplier
        draw_button(screen, WHITE, [10, 160, 100, 25], "Adjust Multiplier", font)

        # RESET to Default Settings
        draw_button(screen, WHITE, [10, 190, 100, 25], "Reset to Default", font)

        # RESET to Square
        draw_button(screen, WHITE, [10, 220, 100, 25], "Reset to Square", font)

        # Repeats On/Off
        if repeats:
            draw_button(screen, WHITE, [10, 250, 100, 25], "Turn Off Repeats", font)
        else:
            draw_button(screen, WHITE, [10, 250, 100, 25], "Turn On Repeats", font)

        pygame.display.flip()

        # Clock FPS
        clock.tick(120)

    pygame.quit()


if __name__ == '__main__':
    main()
