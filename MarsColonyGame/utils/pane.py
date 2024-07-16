from pygame import init, font, draw, Surface

class Pane:
    """
    Represents a drawable pane in the MarsColony game UI.
    """

    def __init__(self, screen: Surface, pane_position: tuple[int, int, int, int], 
                 background_color: tuple[int, int, int], font_size: int = 20) -> None:
        """
        Initialize a Pane object.

        Args:
            screen (Surface): The surface on which the pane will be drawn.
            pane_position (tuple[int, int, int, int]): The position and size of the pane (x, y, width, height).
            background_color (tuple[int, int, int]): The background color of the pane.
            font_size (int, optional): The font size for text displayed in the pane. Defaults to 20.
        """
        init()
        self.screen: Surface = screen
        self.pane_position: tuple[int, int, int, int] = pane_position
        self.font = font.SysFont("Arial", font_size)
        self.background_color: tuple[int, int, int] = background_color
        self.rect_outline = None

    def draw_rect(self) -> None:
        """
        Draw the rectangle representing the pane's background.
        """
        # Draw the rectangle on the screen with the specified background color
        self.rect = draw.rect(self.screen, self.background_color, self.pane_position)

    def draw_rect_outline(self, foreground_color: tuple[int, int, int] = (255, 255, 255)) -> None:
        """
        Draw the outline of the pane's rectangle.

        Args:
            foreground_color (tuple[int, int, int]): The color of the outline. Defaults to white.
        """
        # Draw the outline around the pane
        self.rect_outline = draw.rect(self.screen, foreground_color, self.pane_position, 1)

    def display_text(self, text: str, centered: bool, 
                     foreground_color: tuple[int, int, int] = (0, 0, 0)) -> None:
        """
        Display text within the pane, supporting multiline text.

        Args:
            text (str): The text to display.
            centered (bool): Whether the text should be centered in the pane.
            foreground_color (tuple[int, int, int]): The color of the text. Defaults to black.
        """
        # Split the text into lines for multiline support
        lines: list[str] = text.split('\n')
        line_height: int = self.font.get_linesize()
        
        # Calculate the maximum number of lines that can fit in the pane
        max_lines: int = self.pane_position[3] // line_height  
        # Determine how many lines to render
        num_lines: int = min(len(lines), max_lines) 

        # Calculate the total height of the text to center it vertically
        total_text_height: int = num_lines * line_height
        start_y: float = self.pane_position[1] + (self.pane_position[3] - total_text_height) / 2

        # Render only the lines that fit in the pane
        for i, line in enumerate(lines[:max_lines]):
            text_surface = self.font.render(line, True, foreground_color)

            if centered:
                # Center the text horizontally within the pane
                text_rect = text_surface.get_rect(
                    center=(
                        self.pane_position[0] + self.pane_position[2] / 2,
                        start_y + i * line_height + line_height / 2
                    )
                )
            else:
                # Align the text to the top left with some padding
                text_rect = text_surface.get_rect(
                    topleft=(
                        self.pane_position[0] + 5,
                        start_y + i * line_height
                    )
                )
            # Draw the text on the screen
            self.screen.blit(text_surface, text_rect)