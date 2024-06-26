from threading import Thread
from time import sleep, time
from typing import Any, Optional
from pygame import draw, Surface

class Cell:
    """
    Represents a cell in the grid of the MarsColony game.
    """

    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        """
        Initialize a Cell object.

        Args:
            pos_x (int): The x-coordinate of the cell's top-left corner.
            pos_y (int): The y-coordinate of the cell's top-left corner.
            size (int): The size (width and height) of the cell.
        """
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.size: int = size

        self.color: tuple = (139, 69, 19)
        self.is_occupied: bool = False
        self.is_powered: bool = False
        self.is_manpowered: bool = False
        self.occupied_with: Any = None
        self._last_color_set_time = time()
        self.icon = None

    def damage_occupier(self):
        if self.occupied_with.object_name in ["Bio Dome", "Ore Mine"]:
            console_msg = f"A meteorite has damaged one\nof your {self.occupied_with.object_name}'s!"
        else:
            console_msg = f"A meteorite has damaged\na {self.occupied_with.object_name}!"
        self.icon = None
        self.occupied_with = None
        self.is_occupied = False
        return console_msg
        

    def change_color(self, color: tuple) -> None:
        """
        Change the color of the cell.

        Args:
            color (tuple): The new color of the cell.
        """
        self.color = color

    def set_icon(self, icon: Optional[Surface]) -> None:
        """
        Set the icon for the cell.

        Args:
            icon (Optional[Surface]): The icon to be displayed on the cell.
        """
        self.icon = icon

    def draw(self, screen: Surface) -> None:
        """
        Draw the cell on the screen.

        Args:
            screen (Surface): The surface to draw the cell on.
        """
        draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size, self.size))
        if self.icon:
            screen.blit(self.icon, (self.pos_x, self.pos_y))
        draw.rect(screen, (0, 0, 0), (self.pos_x, self.pos_y, self.size, self.size), 1)

    def reset_color(self) -> None:
        """Reset the color of the cell."""
        self.color = (139, 69, 19)


    def show_info(self) -> str:
        """
        Get a string containing information about the cell.

        Returns:
            str: A string containing information about the cell.
        """
        if self.occupied_with:
            return f"Is occupied: {self.is_occupied}\nwith: {self.occupied_with.object_name}\nis powered: {self.is_powered}\nis manpowered: {self.is_manpowered}"
        else:
            return f"Is occupied: {self.is_occupied}\nis powered: {self.is_powered}\nis manpowered: {self.is_manpowered}"

    def set_is_powered(self, powered: bool) -> None:
        """
        Set the powered state of the cell.

        Args:
            powered (bool): The new powered state of the cell.
        """
        self.is_powered = powered
        self.color = (100, 100, 100)
        self._last_color_set_time = time()
        Thread(target=self._reset_color_after_delay, args=(2, self._last_color_set_time)).start()

    def set_is_man_powered(self, manpowered: bool) -> None:
        """
        Set the man-powered state of the cell.

        Args:
            manpowered (bool): The new man-powered state of the cell.
        """
        self.is_manpowered = manpowered
        self.color = (150, 150, 150)
        self._last_color_set_time = time()
        Thread(target=self._reset_color_after_delay, args=(2, self._last_color_set_time)).start()

    def _reset_color_after_delay(self, delay: float, color_set_time:float) -> None:
        """
        Reset the color of the cell after a delay.

        Args:
            delay (float): The delay (in seconds) before resetting the color.
        """
        sleep(delay)
        if color_set_time == self._last_color_set_time:
            self.reset_color()