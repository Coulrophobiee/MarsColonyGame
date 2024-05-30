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
        self.screen.blit(self.font.render(text, True, (0, 255, 0)), self.pane_position)