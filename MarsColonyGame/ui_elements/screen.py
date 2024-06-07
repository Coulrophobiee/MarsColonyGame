from ui_elements.grid import Grid
from ui_elements.sidebar import Sidebar
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter
from pygame import display

class Screen:
    
    def __init__(self, BUILDING_OPTION, ressource_counter: RessourceCounter, day_counter:DayCounter, SCREEN_HEIHGT=600, SCREEN_WIDTH=1100, SIDEBAR_WIDTH=200) -> None:
        self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIHGT))
        display.set_caption("MarsColony")

        self.screen.fill((0, 0, 0))

        SIDEBAR_X_POSITION = SCREEN_WIDTH - SIDEBAR_WIDTH
        SIDEBAR_Y_POSITION = 0
        SIDEBAR_HEIGHT = SCREEN_HEIHGT

        AVAIABLE_GRID_WIDTH = SCREEN_WIDTH - SIDEBAR_WIDTH
        AVAIABLE_GRID_HEIHGT = SCREEN_HEIHGT

        self.sidebar = Sidebar(SIDEBAR_X_POSITION, SIDEBAR_Y_POSITION, SIDEBAR_WIDTH, SIDEBAR_HEIGHT, BUILDING_OPTION, day_counter, ressource_counter)
        self.grid = Grid(AVAIABLE_GRID_WIDTH, AVAIABLE_GRID_HEIHGT)

    def display(self):
        self.sidebar.draw_sidebar(self.screen)
        self.grid.draw_grid(self.screen)

    def where_is_mouse_click(self, mouse_position):
        x, _ = mouse_position
        if self.sidebar.x <= x <= self.sidebar.x + self.sidebar.width:
            return "sidebar"
        else:
            return "grid"