from pygame import init, font, draw
class Pane():
    def __init__(self, screen, pane_position, background_color) -> None:
        init()
        self.screen = screen
        self.pane_position = pane_position
        self.font = font.SysFont("Arial", 25)
        self.background_color = background_color

    def add_rect(self):
        self.rect = draw.rect(self.screen, self.background_color, self.pane_position)

    def add_text(self, text):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(
                self.pane_position[0] + self.pane_position[2] / 2,
                self.pane_position[1] + self.pane_position[3] / 2
            )
        )
        self.screen.blit(text_surface, text_rect)