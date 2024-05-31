from pygame import draw, Rect, font
from ui_elements.pane import Pane

class Sidebar:
    def __init__(self, x, y, width, height, building_options) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.building_options = building_options
        self.selected_building = None
        self.day_counter = 0
    
    def draw_sidebar(self, screen):
        
        # Sidebar Background
        draw.rect(screen, (200, 200, 200), (self.x, self.y, self.width, self.height))

        # Drawing the day counter
        day_text_font = font.Font(None, 36)
        day_text = day_text_font.render(f"Day: {self.day_counter}", True, (0, 0, 0))
        screen.blit(day_text, (self.x + 10, self.y + 10))

        # Drawing the sidebar buildung options, by multiplying we calculate the vertical position of the building
        for index, building_name in enumerate(self.building_options):
            color = (150, 150, 150) if building_name == self.selected_building else (255, 255, 255)
            pane_position = (self.x + 10, self.y + 60 + index * 50, self.width - 20, 40)
            pane = Pane(screen, pane_position, color)
            pane.add_rect()
            pane.add_text(building_name)
            #draw.rect(screen, color, (self.x + 10, self.y + 10 + index * 50, self.width - 20, 40))

            # TODO: add icon or text specific for each building
    
    def handle_click(self, position):
        x, y = position
        if self.x <= x <= self.x + self.width:
            for index, building in enumerate(self.building_options):
                option_rect = Rect(self.x + 10, self.y + 10 + index * 50, self.width - 20, 40)
                if option_rect.collidepoint(x, y):
                    if self.selected_building == building:
                        # Unselect if user clicks on the selected building
                        self.selected_building = None
                    else: 
                        self.selected_building = building
                    return True
        return False
    
    def increment_day_count(self):
        self.day_counter += 1