from utils.pane import Pane

class ConsoleLog:
    def __init__(self) -> None:
        self.text = ""
        self.pane = None
        #self.pane.display_text(self.text, True)

    def add_text(self, text):
        self.text = text
        self.pane.display_text(text, False, (255, 255, 255))

    def draw_log(self, screen, x_position, y_position, sidebar_width):
        position = (x_position + 10, y_position + 500, sidebar_width - 20, 90)
        background_color = (0, 0, 0)
        self.pane = Pane(screen, position, background_color, 10)
        self.pane.draw_rect()
        self.pane.draw_rect_outline()
        self.add_text(self.text)
