from typing import Optional
from pygame import draw, Rect, Surface
from utils.pane import Pane
from ui_elements.sidebar_elements.day_counter import DayCounter
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.console_log import ConsoleLog

class Sidebar:
    """
    Represents the sidebar in the MarsColony game, which displays various game statistics and options.
    """

    def __init__(self, x: int, y: int, width: int, height: int, building_options: list[str], 
                 day_counter: DayCounter, ressource_counter: RessourceCounter, log: ConsoleLog) -> None:
        """
        Initialize a Sidebar object.

        Args:
            x (int): The x-coordinate of the sidebar.
            y (int): The y-coordinate of the sidebar.
            width (int): The width of the sidebar.
            height (int): The height of the sidebar.
            building_options (list[str]): A list of building options.
            day_counter (DayCounter): The day counter object.
            ressource_counter (RessourceCounter): The resource counter object.
            log (ConsoleLog): The console log object.
        """
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.building_options: list[str] = building_options
        self.selected_building: Optional[str] = None
        self.day_counter: DayCounter = day_counter
        self.ressource_counter: RessourceCounter = ressource_counter
        self.log: ConsoleLog = log
    
    def draw_sidebar(self, screen: Surface) -> None:
        """
        Draw the sidebar on the screen.

        Args:
            screen (Surface): The surface to draw the sidebar on.
        """
        draw.rect(screen, (47, 79, 79), (self.x, self.y, self.width, self.height))

        day_counter_position: tuple[int, int, int, int] = (self.x + 10, self.y + 10, self.width - 20, 40)
        day_counter_pane: Pane = Pane(screen, day_counter_position, self.day_counter.background_color)
        day_counter_pane.draw_rect()
        day_counter_pane.display_text(f"Day: {self.day_counter.days_passed}", True)

        ressources: list[str] = list(filter(lambda a: not a.startswith("__") and not callable(getattr(self.ressource_counter, a)), dir(self.ressource_counter)))

        for index, ressource in enumerate(ressources):
            ressource_counter_position: tuple[int, int, int, int] = (self.x + 10, self.y + 80 + index * 50, self.width - 20, 40)
            ressource_counter_pane: Pane = Pane(screen, ressource_counter_position, (255, 255, 255))
            ressource_counter_pane.draw_rect()
            ressource_count: int = getattr(self.ressource_counter, ressource)
            ressource: str = self.ressource_counter.get_name_of_ressource(ressource)
            ressource_counter_pane.display_text(f"{ressource}: {ressource_count}", True)
            
        for index, building_name in enumerate(self.building_options):
            color: tuple[int, int, int] = (34, 139, 34) if building_name == self.selected_building else (255, 165, 0)
            pane_position: tuple[int, int, int, int] = (self.x + 10, self.y + 260 + index * 50, self.width - 20, 40)
            pane: Pane = Pane(screen, pane_position, color)
            pane.draw_rect()
            pane.display_text(building_name, True)
        
        self.log.draw_log(screen, self.x, self.y, self.width)
    
    def handle_click(self, position: tuple[int, int]) -> None:
        """
        Handle mouse click on the sidebar.

        Args:
            position (tuple[int, int]): The position of the mouse click.
        """
        x: int
        y: int
        x, y = position
        for index, building_name in enumerate(self.building_options):
            option_rect: Rect = Rect(self.x + 10, self.y + 260 + index * 50, self.width - 20, 40)
            if option_rect.collidepoint(x, y):
                if self.selected_building == building_name:
                    self.selected_building = None  
                else:
                    self.selected_building = building_name