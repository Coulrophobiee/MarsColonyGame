from pygame import draw, Rect

class Sidebar:
    def __init__(self, x, y, width, height, building_options) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.building_options = building_options
        self.selected_building = None
    
    def draw_sidebar(self, screen):
        # Sidebar Background
        draw.rect(screen, (200, 200, 200), (self.x, self.y, self.width, self.height))

        # Drawing the sidebar, by multiplying we calculate the vertical position of the building
        for index, building in enumerate(self.building_options):
            color = (150, 150, 150) if building == self.selected_building else (255, 255, 255)
            draw.rect(screen, color, (self.x + 10, self.y + 10 + index * 50, self.width - 20, 40))

            # TODO: add icon or text specific for each building
    
    def handle_click(self, position):
        x, y = position
        if self.x <= x <= self.x + self.width:
            for index, building in enumerate(self.building_options):
                option_rect = Rect(self.x + 10, self.y + 10 + index * 50, self.width - 20, 40)
                if option_rect.collidepoint(x, y):
                    self.selected_building = building
                    return True
        return False