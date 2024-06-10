from pygame import init, font, draw
class Pane:
    def __init__(self, screen, pane_position, background_color, font_size=20) -> None:
        init()
        self.screen = screen
        self.pane_position = pane_position
        self.font = font.SysFont("Arial", font_size)
        self.background_color = background_color

        self.rect_outline = None

    def draw_rect(self):
        self.rect = draw.rect(self.screen, self.background_color, self.pane_position)

    def draw_rect_outline(self, foreground_color=(255, 255, 255)):
        self.rect_outline = draw.rect(self.screen, foreground_color, self.pane_position, 1)

    def display_text(self, text, centered, foreground_color=(0, 0, 0)):
        text_surface = self.font.render(text, True, foreground_color)
        if centered:
            text_rect = text_surface.get_rect(
                center=(
                    self.pane_position[0] + self.pane_position[2] / 2,
                    self.pane_position[1] + self.pane_position[3] / 2
                )
            )
            self.screen.blit(text_surface, text_rect)
        else:
            text_rect = text_surface.get_rect(
                topleft=(
                    self.pane_position[0],
                    self.pane_position[1]
                )
            )
            self.screen.blit(text_surface, text_rect)