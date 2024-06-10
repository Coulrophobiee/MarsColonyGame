from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter
from ui_elements.screen import Screen
from ui_elements.console_log import ConsoleLog
from colony import Colony
from sys import exit

import pygame

def main():

    # Initialize Pygame 
    pygame.init()

    # List of buildings
    BUILDING_OPTIONS = ("Solar Park", "Living Compartment", "Ore Mine", "Bio Dome")

    # Initialize Counter Objects
    day_counter = DayCounter()
    ressource_counter = RessourceCounter()

    # Initialize Log
    log = ConsoleLog()
    screen = Screen(BUILDING_OPTIONS, ressource_counter, day_counter, log)
    
    # Define timer event and interval in milliseconds (currently 20 sceonds)
    NEW_DAY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(NEW_DAY_EVENT, 20_00)

    # Create colony
    colony = Colony(ressource_counter, day_counter, screen.grid)
    colony.spawn_starting_buildings()

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
                    screen.grid.handle_click(mouse_position, screen.sidebar, colony)
            elif event.type == NEW_DAY_EVENT:
                screen.sidebar.day_counter.increment_day()
                colony.generate_ressources()
                colony.consume_food()
                if not colony.check_loss():
                    print("LOST")
                    running = False
                elif colony.check_win():
                    print("WON")
                    running = False
    	
        screen.display()

        pygame.display.flip()
    pygame.quit()
    exit()
    
if __name__ == "__main__":
    main()