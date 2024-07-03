from pygame import font, Surface, display, event, QUIT, quit, KEYDOWN
from ui_elements.screen import Screen

class Popup:

    def __init__(self, screen:Screen, message):
        self.screen = screen
        self.message = message
        self.font = font.SysFont(None, 48)
        self.popup_width, self.popup_height = 400, 200
        self.popup_surface = Surface((self.popup_width, self.popup_height))
        self.popup_surface.fill((255, 255, 255))
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.popup_width//2, self.popup_height//2))
        self.popup_surface.blit(self.text, self.text_rect)
        self.popup_rect = self.popup_surface.get_rect(center=(self.screen.width // 2, self.screen.height //2))
    
    def display(self):
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