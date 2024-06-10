from threading import Thread
from time import sleep
from pygame import draw

class Cell:
    
    def __init__(self, pos_x, pos_y, size) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

        self.color = (139, 69, 19)
        self.is_occupied = False
        self.is_powered = False
        self.is_manpowered = False
        self.occupied_with = None

        self.icon = None

    def change_color(self, color):
        self.color = color

    def set_icon(self, icon):
        self.icon = icon

    def draw(self, screen):
        draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size, self.size))
        if self.icon:
            screen.blit(self.icon, (self.pos_x, self.pos_y))
        draw.rect(screen, (0, 0, 0), (self.pos_x, self.pos_y, self.size, self.size), 1)
    
    def reset_color(self):
        self.color = (139, 69, 19)

    def show_info(self):
        return f"\nIs occupied: {self.is_occupied}\n is occupied with: {self.occupied_with}, is powered: {self.is_powered}, is manpowered: {self.is_manpowered}"

    def set_is_powered(self, powered):
        self.is_powered = powered
        self.color = (100, 100, 100)
        Thread(target=self._reset_color_after_delay, args=(2, )).start()

    def set_is_man_powered(self, manpowered):
        self.is_manpowered = manpowered
        self.color = (150, 150, 150)
        Thread(target=self._reset_color_after_delay, args=(2, )).start()

    def _reset_color_after_delay(self, delay):
        sleep(delay)
        self.reset_color()