from utils.pane import Pane

class ConsoleLog:
    """
    Represents the console log in the MarsColony game.
    """

    def __init__(self) -> None:
        """
        Initialize a ConsoleLog object.
        """
        self.text: str = ""
        self.pane: Pane = None

    def add_text(self, text: str) -> None:
        """
        Add text to the console log.

        Args:
            text (str): The text to be added to the log.
        """
        self.text = text
        self.pane.display_text(text, False, (255, 255, 255))

    def draw_log(self, screen, x_position: int, y_position: int, sidebar_width: int) -> None:
        """
        Draw the console log on the sidebar.

        Args:
            screen (Surface): The surface to draw the log on.
            x_position (int): The x-coordinate of the top-left corner of the sidebar.
            y_position (int): The y-coordinate of the top-left corner of the sidebar.
            sidebar_width (int): The width of the sidebar.
        """
        position = (x_position + 10, y_position + 500, sidebar_width - 20, 90)
        background_color = (0, 0, 0)
        self.pane = Pane(screen, position, background_color, 15)
        self.pane.draw_rect()
        self.pane.draw_rect_outline()
        self.add_text(self.text)
