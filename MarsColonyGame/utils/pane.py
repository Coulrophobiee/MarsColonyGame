from pygame import init, font, draw
class Pane:
    def __init__(self, screen, pane_position, background_color, font_size=20) -> None:
        init()
        self.screen = screen
        self.pane_position = pane_position
        self.font = font.SysFont("Arial", font_size)
        self.background_color = background_color
        self.rect_outline = None

    def draw_rect(self) -> None:
        """
        Draws the rectangle for the pane.
        """
        self.rect = draw.rect(self.screen, self.background_color, self.pane_position)

    def draw_rect_outline(self, foreground_color=(255, 255, 255)) -> None:
        """
        Draws the outline of the rectangle for the pane.

        Args:
            foreground_color (tuple): The color of the outline.
        """
        self.rect_outline = draw.rect(self.screen, foreground_color, self.pane_position, 1)

    def display_text(self, text: str, centered: bool, foreground_color=(0, 0, 0)) -> None:
        """
        Displays the text within the pane. Supports multiline text.

        Args:
            text (str): The text to display.
            centered (bool): Whether the text should be centered or not.
            foreground_color (tuple): The color of the text.
        """
        lines = text.split('\n')
        line_height = self.font.get_linesize()
        max_lines = (self.pane_position[3] // line_height)  # Calculate how many lines fit in the pane
        num_lines = min(len(lines), max_lines)
        
        total_text_height = num_lines * line_height
        start_y = self.pane_position[1] + (self.pane_position[3] - total_text_height) / 2

        for i, line in enumerate(lines[:max_lines]):  # Render only the lines that fit in the pane
            text_surface = self.font.render(line, True, foreground_color)
            if centered:
                text_rect = text_surface.get_rect(
                    center=(
                        self.pane_position[0] + self.pane_position[2] / 2,
                        start_y + i * line_height + line_height / 2
                    )
                )
            else:
                text_rect = text_surface.get_rect(
                    topleft=(
                        self.pane_position[0] + 5,  # Adding some padding
                        start_y + i * line_height
                    )
                )
            self.screen.blit(text_surface, text_rect)