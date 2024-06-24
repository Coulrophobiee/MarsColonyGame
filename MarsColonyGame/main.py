from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter
from ui_elements.screen import Screen
from ui_elements.console_log import ConsoleLog
from environment.environmental_generator import EnvironmentalGenerator
from environment.meteorite import Meteorite
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

    # Define meteorite-crash-event
    meteorite = None
    METEORITE_EVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(METEORITE_EVENT, 6_000) 

    # Create colony
    colony = Colony(ressource_counter, day_counter, screen.grid)
    colony.spawn_starting_buildings()

    # Generate environment
    env_generator = EnvironmentalGenerator()
    env_generator.generate(screen.grid)
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
                screen.sidebar.log.add_text(f"Day {screen.sidebar.day_counter.days_passed} has begun!")
                colony.generate_ressources()
                colony.consume_food()
                if colony.has_failed():
                    print("LOST")
                    running = False
                if colony.has_succeded():
                    print("WON")
                    running = False
            elif event.type == METEORITE_EVENT:
                meteorite = Meteorite(screen, screen.grid)

        if meteorite:
            meteorite.fall()
            if meteorite.current_position == None:
                meteorite = None

        screen.display()

        if meteorite and meteorite.current_position != None:
            meteorite.draw()

        pygame.display.flip()
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()