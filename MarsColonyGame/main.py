from ui_elements.grid import Grid
from ui_elements.sidebar import Sidebar
from sys import exit

import pygame

def main():

    # Initialize Pygame 
    pygame.init()

    # List of buildings
    BUILDING_OPTIONS = ("Solar Panel", "Living Compartment", "Ore Mine", "Bio Dome")

    # Define screen dimensions
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GRID V1")

    # Define grid dimensions and cell size
    ROWS = 20
    COLS = 20
    cell_width = (SCREEN_WIDTH - 200) // COLS
    cell_height = SCREEN_HEIGHT // ROWS 

    # Create a Grid object
    grid = Grid(ROWS, COLS, cell_width, cell_height)

    # Create a Sidebar object
    SIDEBAR_WIDTH = 200
    SIDEBAR_HEIGHT = SCREEN_HEIGHT
    SIDEBAR_X_POSTION  = SCREEN_WIDTH - SIDEBAR_WIDTH
    SIDEBAR_Y_POSITION = 0
    sidebar = Sidebar(SIDEBAR_X_POSTION, SIDEBAR_Y_POSITION, SIDEBAR_WIDTH, SIDEBAR_HEIGHT, BUILDING_OPTIONS)
    
    # Define timer event and interval in milliseconds (currently 20 sceonds)
    NEW_DAY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(NEW_DAY_EVENT, 20_000)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                click_location = where_is_mouse_click(mouse_position, sidebar)

                if click_location == "sidebar":
                    sidebar.handle_click(mouse_position)
                elif click_location == "grid":
                    grid.handle_click(mouse_position, sidebar)
            elif event.type == NEW_DAY_EVENT:
                sidebar.increment_day_count()
                
        # Fill screen black
        screen.fill((0, 0, 0))

        # Draw the grid
        grid.draw_grid(screen)

        # Draw the sidebar
        sidebar.draw_sidebar(screen)

        # Update display
        pygame.display.flip()
    
    pygame.quit()
    exit()

def where_is_mouse_click(mouse_position, sidebar:Sidebar):
    x, _ = mouse_position
    if sidebar.x <= x <= sidebar.x + sidebar.width:
        return "sidebar"
    else:
        return "grid"
    
if __name__ == "__main__":
    main()