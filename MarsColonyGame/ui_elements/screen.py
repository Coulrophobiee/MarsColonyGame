from ui_elements.grid import Grid
from ui_elements.sidebar import Sidebar
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter
from ui_elements.console_log import ConsoleLog
from pygame import display
from typing import Tuple


class Screen:
    """
    Screen class to handle the main display of the MarsColony game.
    """

    def __init__(self, building_option: list, ressource_counter: RessourceCounter, 
                 day_counter: DayCounter, log: ConsoleLog, 
                 screen_height: int = 600, screen_width: int = 1100, 
                 sidebar_width: int = 200) -> None:
        """
        Initialize the Screen class.

        Args:
            building_option (list): List of building options.
            ressource_counter (RessourceCounter): Instance of RessourceCounter.
            day_counter (DayCounter): Instance of DayCounter.
            log (ConsoleLog): Instance of ConsoleLog.
            screen_height (int, optional): Height of the screen. Defaults to 600.
            screen_width (int, optional): Width of the screen. Defaults to 1100.
            sidebar_width (int, optional): Width of the sidebar. Defaults to 200.
        """
        self.screen = display.set_mode((screen_width, screen_height))
        display.set_caption("MarsColony")

        self.screen.fill((0, 0, 0))

        # Sidebar dimensions and position
        sidebar_x_position = screen_width - sidebar_width
        sidebar_y_position = 0
        sidebar_height = screen_height

        # Available grid dimensions
        available_grid_width = screen_width - sidebar_width
        available_grid_height = screen_height

        # Initialize sidebar and grid
        self.sidebar = Sidebar(sidebar_x_position, sidebar_y_position, 
                               sidebar_width, sidebar_height, building_option, 
                               day_counter, ressource_counter, log)
        self.grid = Grid(available_grid_width, available_grid_height)

    def display(self) -> None:
        """
        Display the sidebar and grid on the screen.
        """
        self.sidebar.draw_sidebar(self.screen)
        self.grid.draw_grid(self.screen)

    def where_is_mouse_click(self, mouse_position: Tuple[int, int]) -> str:
        """
        Determine where the mouse click occurred.

        Args:
            mouse_position (Tuple[int, int]): The (x, y) position of the mouse click.

        Returns:
            str: "sidebar" if the click is on the sidebar, otherwise "grid".
        """
        x, _ = mouse_position
        if self.sidebar.x <= x <= self.sidebar.x + self.sidebar.width:
            return "sidebar"
        else:
            return "grid"