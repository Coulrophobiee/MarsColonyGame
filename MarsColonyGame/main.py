from ui_elements.sidebar import Sidebar
from ui_elements.screen import Screen
from sys import exit

import pygame

def main():

    # Initialize Pygame 
    pygame.init()

    # List of buildings
    BUILDING_OPTIONS = ("Solar Panel", "Living Compartment", "Ore Mine", "Bio Dome")
    
    screen = Screen(BUILDING_OPTIONS)
    
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
                click_location = screen.where_is_mouse_click(mouse_position)

                if click_location == "sidebar":
                    screen.sidebar.handle_click(mouse_position)
                elif click_location == "grid":
                    screen.grid.handle_click(mouse_position, screen.sidebar)
            elif event.type == NEW_DAY_EVENT:
                screen.sidebar.increment_day_count()
    	
        screen.display()

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