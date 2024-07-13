from pygame import font, Surface, display, event, QUIT, quit, KEYDOWN
from ui_elements.screen import Screen

class Popup:
    """
    Represents a popup message on the screen in the MarsColony game.
    """

    def __init__(self, screen: Screen, message: str) -> None:
        """
        Initialize a Popup object.

        Args:
            screen (Screen): The screen object where the popup will be displayed.
            message (str): The message to display in the popup.
        """
        self.screen: Screen = screen
        self.message: str = message
        self.font = font.SysFont(None, 48)
        self.popup_width: int = 400
        self.popup_height: int = 200
        self.popup_surface: Surface = Surface((self.popup_width, self.popup_height))
        self.popup_surface.fill((255, 255, 255))
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.popup_width // 2, self.popup_height // 2))
        self.popup_surface.blit(self.text, self.text_rect)
        self.popup_rect = self.popup_surface.get_rect(center=(self.screen.width // 2, self.screen.height // 2))
    
    def display(self) -> None:
        """
        Display the popup on the screen and wait for user input to close it.
        """
        self.screen.screen.blit(self.popup_surface, self.popup_rect)
        display.update()

        waiting = True
        while waiting:
            for events in event.get():
                if events.type == QUIT:
                    quit()
                    exit()
                elif events.type == KEYDOWN:
                    waiting = False