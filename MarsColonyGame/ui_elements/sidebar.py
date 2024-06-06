from pygame import draw, Rect, font
from utils.pane import Pane
from ui_elements.sidebar_elements.day_counter import DayCounter
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter

class Sidebar:
    def __init__(self, x, y, width, height, building_options, day_counter:DayCounter, ressource_counter:RessourceCounter) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.building_options = building_options
        self.selected_building = None
        self.day_counter = day_counter
        self.ressource_counter = ressource_counter
    
    def draw_sidebar(self, screen):
        
        # Sidebar Background
        draw.rect(screen, (47, 79, 79), (self.x, self.y, self.width, self.height))

        day_counter_position = (self.x + 10, self.y + 10, self.width - 20, 40)
        day_counter_pane = Pane(screen, day_counter_position, self.day_counter.background_color)
        day_counter_pane.draw_rect()
        day_counter_pane.display_text(f"Day: {self.day_counter.days_passed}")

        ressources = list(filter(lambda a: not a.startswith("__") and not callable(getattr(self.ressource_counter, a)), dir(self.ressource_counter)))

        for index, ressource in enumerate(ressources):
            ressource_counter_position = (self.x + 10, self.y + 80 + index * 50, self.width - 20, 40)
            ressource_counter_pane = Pane(screen, ressource_counter_position, (255, 255, 255))
            ressource_counter_pane.draw_rect()
            ressource_count = getattr(self.ressource_counter, ressource)
            ressource = self.ressource_counter.get_name_of_ressource(ressource)
            ressource_counter_pane.display_text(f"{ressource}: {ressource_count}")
            
        # Drawing the sidebar buildung options, by multiplying we calculate the vertical position of the building
        for index, building_name in enumerate(self.building_options):
            color = (34, 139, 34) if building_name == self.selected_building else (255, 165, 0)
            pane_position = (self.x + 10, self.y + 260 + index * 50, self.width - 20, 40)
            pane = Pane(screen, pane_position, color)
            pane.draw_rect()
            pane.display_text(building_name)
            #draw.rect(screen, color, (self.x + 10, self.y + 10 + index * 50, self.width - 20, 40))

            # TODO: add icon or text specific for each building
    
    def handle_click(self, position):
        # return False
        x, y = position
        for index, building_name in enumerate(self.building_options):
            option_rect = Rect(self.x + 10, self.y + 260 + index * 50, self.width - 20, 40)
            if option_rect.collidepoint(x, y):
                if self.selected_building == building_name:
                    # Unselect if the same building is clicked again
                    self.selected_building = None  
                else:
                     # Select the new building
                    self.selected_building = building_name 