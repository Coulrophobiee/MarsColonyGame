from grid import Grid
from sys import exit
import pygame

def main():
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GRID V1")

    ROWS = 20
    COLS = 20
    cell_width = SCREEN_WIDTH // COLS
    cell_height = SCREEN_HEIGHT // ROWS 

    grid = Grid(ROWS, COLS, cell_width, cell_height)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                grid.handle_click(pygame.mouse.get_pos())

        screen.fill((0, 0, 0))
        grid.draw_grid(screen)
        pygame.display.flip()
    
    pygame.quit()
    exit()

    
if __name__ == "__main__":
    main()