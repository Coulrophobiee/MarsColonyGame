from utils.pane import Pane

class ConsoleLog:
    def __init__(self, screen, x_position, y_position, sidebar_width) -> None:
        self.text = ""
        position = (x_position + 10, y_position + 500, sidebar_width - 20, 40)
        background_color = (255, 255, 255)
        self.pane = Pane(screen, position, background_color, 10)
        self.pane.draw_rect()
        #self.pane.display_text(self.text, True)

    def add_text(self, text):
        self.text = text
        self.pane.display_text(text, False)
